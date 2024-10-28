#!/usr/bin/env python3
"""
Gets page data through index range
"""
import csv
from typing import Tuple
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets entries on specific page

        Args:
            page: Page number. Defaults to 1.
            page_size: Number of elements in a page. Defaults to 10.

        Returns:
            (list): Elements for a specific page
        """
        assert isinstance(page, int) and page >= 1
        assert isinstance(page_size, int) and page_size >= 1
        page_indexes = index_range(page, page_size)

        dataset = self.dataset()
        try:
            res = dataset[page_indexes[0]: page_indexes[1]]
            return res
        except IndexError:
            return []
