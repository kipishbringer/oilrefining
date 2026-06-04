from django.core.cache import cache
from rest_framework.response import Response


class AuthorQuerySetMixin:
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(author=self.request.user)


class CachedListAPIViewMixin:
    cache_timeout = 60 * 60 * 12
    cache_namespace = None

    def list(self, request, *args, **kwargs):
        cache_key = self.get_list_cache_key()
        cached_data = self.cache_get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            self.cache_set(cache_key, response.data)
            return response

        serializer = self.get_serializer(queryset, many=True)
        self.cache_set(cache_key, serializer.data)
        return Response(serializer.data)

    def get_list_cache_key(self):
        user = self.request.user
        version = self.get_cache_version()
        role = 'staff' if user.is_staff else 'user'
        return f'measurement:{self.cache_namespace}:list:{role}:{user.pk}:v{version}'

    def get_cache_version(self):
        version_key = self.get_cache_version_key()
        version = self.cache_get(version_key)

        if version is None:
            version = 1
            self.cache_set(version_key, version, None)

        return version

    def get_cache_version_key(self):
        return f'measurement:{self.cache_namespace}:version'

    def cache_get(self, key):
        try:
            return cache.get(key)
        except Exception:
            return None

    def cache_set(self, key, value, timeout=None):
        try:
            cache.set(key, value, self.cache_timeout if timeout is None else timeout)
        except Exception:
            pass


class CacheInvalidationMixin:
    cache_namespace = None

    def perform_create(self, serializer):
        instance = serializer.save()
        self.invalidate_list_cache()
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        self.invalidate_list_cache()
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        self.invalidate_list_cache()

    def invalidate_list_cache(self):
        version_key = f'measurement:{self.cache_namespace}:version'

        try:
            cache.incr(version_key)
        except Exception:
            try:
                cache.set(version_key, 1, None)
            except Exception:
                pass
