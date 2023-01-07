from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sayfa"


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class CustomCursorPagination(CursorPagination):
    cursor_query_param = "imlec"
    page_size = 10
    ordering = "id"  # changing ordering style (we don't need created column anymore)