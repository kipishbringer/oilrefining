class AuthorQuerySetMixin:
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(author=self.request.user)