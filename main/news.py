from email.utils import parsedate_to_datetime
from html import unescape
from xml.etree import ElementTree

import requests
from django.conf import settings


DEFAULT_NEWS_RSS_URLS = [
    'https://news.google.com/rss/search?q=%D0%BD%D0%B5%D1%84%D1%82%D0%B5%D1%85%D0%B8%D0%BC%D0%B8%D1%8F%20OR%20%D0%9D%D0%9F%D0%97%20OR%20%D0%BD%D0%B5%D1%84%D1%82%D0%B5%D0%BF%D0%B5%D1%80%D0%B5%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0&hl=ru&gl=RU&ceid=RU:ru',
    'https://www.interfax.ru/rss.asp',
    'https://tass.ru/rss/v2.xml',
]

NEWS_KEYWORDS = (
    'нефтехим', 'нпз', 'нефтепереработ', 'нефтегаз', 'нефтян', 'нефтепродукт',
    'нефть', 'газпром нефть', 'сибур', 'лукойл', 'роснефть', 'brent',
)

ALLOWED_NEWS_DOMAINS = (
    'neftegaz.ru',
    'oilcapital.ru',
    'interfax.ru',
    'tass.ru',
    'ria.ru',
    'rbc.ru',
    'kommersant.ru',
    'rg.ru',
    'vedomosti.ru',
)


def get_news(limit=3):
    news = []

    for url in get_news_sources():
        try:
            news.extend(filter_news(parse_feed(url)))
        except Exception:
            continue

        if len(news) >= limit:
            break

    news = dedupe_news(news)
    news.sort(key=lambda item: item.get('published_at') or '', reverse=True)
    return news[:limit]


def get_news_sources():
    raw_sources = getattr(settings, 'NEWS_RSS_URLS', '')

    if not raw_sources:
        return DEFAULT_NEWS_RSS_URLS

    return [source.strip() for source in raw_sources.split(',') if source.strip()]


def parse_feed(url):
    response = requests.get(
        url,
        timeout=12,
        headers={'User-Agent': 'OperatorBear/1.0 (+https://localhost)'},
    )
    response.raise_for_status()

    root = ElementTree.fromstring(response.content)
    items = root.findall('.//item')

    if items:
        return [parse_rss_item(item, url) for item in items]

    entries = root.findall('{http://www.w3.org/2005/Atom}entry')
    return [parse_atom_entry(entry, url) for entry in entries]


def parse_rss_item(item, source_url):
    title = get_text(item, 'title')
    link = get_text(item, 'link')
    published = get_text(item, 'pubDate')
    description = get_text(item, 'description')
    source_node = item.find('source')
    source = source_node.text if source_node is not None and source_node.text else get_host(source_url)
    source_link = source_node.attrib.get('url', '') if source_node is not None else source_url

    return {
        'title': clean_text(title),
        'url': link,
        'source': clean_text(source),
        'source_url': source_link,
        'published_at': format_date(published),
        'description': clean_text(description),
    }


def parse_atom_entry(entry, source_url):
    title = get_namespaced_text(entry, 'title')
    published = get_namespaced_text(entry, 'published') or get_namespaced_text(entry, 'updated')
    link = ''

    for child in entry:
        if child.tag.endswith('link'):
            link = child.attrib.get('href', '')
            break

    return {
        'title': clean_text(title),
        'url': link,
        'source': get_host(source_url),
        'source_url': source_url,
        'published_at': format_date(published),
        'description': '',
    }


def get_text(item, tag):
    child = item.find(tag)
    return child.text if child is not None and child.text else ''


def filter_news(items):
    filtered = []

    for item in items:
        haystack = f"{item.get('title', '')} {item.get('description', '')}".lower()

        if is_allowed_source(item) and any(keyword in haystack for keyword in NEWS_KEYWORDS):
            item['title'] = strip_google_source(item.get('title', ''))
            item.pop('source_url', None)
            item.pop('description', None)
            filtered.append(item)

    return filtered


def is_allowed_source(item):
    source_url = item.get('source_url') or item.get('url') or ''
    source_host = get_host(source_url) if '://' in source_url else source_url.lower()
    source_name = item.get('source', '').lower()

    return any(domain in source_host or domain in source_name for domain in ALLOWED_NEWS_DOMAINS)


def dedupe_news(items):
    seen = set()
    result = []

    for item in items:
        key = item.get('url') or item.get('title')

        if not key or key in seen:
            continue

        seen.add(key)
        result.append(item)

    return result


def strip_google_source(title):
    if ' - ' not in title:
        return title

    return title.rsplit(' - ', 1)[0]


def get_namespaced_text(item, tag):
    child = item.find(f'{{http://www.w3.org/2005/Atom}}{tag}')
    return child.text if child is not None and child.text else ''


def clean_text(value):
    return unescape(value or '').strip()


def format_date(value):
    if not value:
        return ''

    try:
        return parsedate_to_datetime(value).isoformat()
    except Exception:
        return value


def get_host(url):
    return url.split('/')[2].replace('www.', '')
