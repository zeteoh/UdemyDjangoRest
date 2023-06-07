from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

"""Pagination only works with viewsets or generic view classes
"""
class WatchListPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class WatchListCPagination(CursorPagination):
    """Cursor pagination loads the latest number of items on the page.
    for instance if my page size is 5, it loads the top 5 latest -created by
    item. To make it start from ascending as in from the oldest item, use created

    Args:
        CursorPagination (_type_): _description_
    """
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'