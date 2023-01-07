from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sayfa"


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
