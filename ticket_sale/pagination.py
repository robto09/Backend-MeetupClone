from rest_framework.pagination import (
    PageNumberPagination,
)

class AllPagePagination(PageNumberPagination):
    page_size = 1