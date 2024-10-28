#!/usr/bin/env python3
"""
Generates index range for particular page
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Gives index range based on pagination parameters

    Args:
        page: Current page
        page_size: No of elements in a page

    Returns:
        (tuple): range of indexes within current page
    """
    max_index = page * page_size
    min_index = (page - 1) * page_size
    return (min_index, max_index)
