from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 6  # Number of items per page
    page_size_query_param = 'limit'  # Query parameter for page size
    max_page_size = 10  # Maximum number of items per page