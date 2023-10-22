# utils.py

from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


def paginate_queryset(request, queryset, per_page=50):
    """
    Handles pagination and returns context for rendering templates.

    :param request: The HTTP request object.
    :param queryset: The queryset to paginate.
    :param per_page: Items per page (default is 50).
    :return: A dictionary containing paginated items and elided page range.
    """
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(page_number)
    elided_page_range = paginator.get_elided_page_range(number=page_number)

    return {
        'items': page_obj,
        'elided_page_range': elided_page_range
    }


def conditional_cache_page(timeout, key_prefix, condition):
    def decorator(view_func):
        def wrapper(*args, **kwargs):
            if condition:
                view = cache_page(timeout, key_prefix=key_prefix)(view_func)
            else:
                view = view_func
            return view(*args, **kwargs)
        return wrapper
    return decorator

