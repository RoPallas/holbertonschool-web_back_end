#!/usr/bin/env python3
"""class Server"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """get_page function"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(self.__dataset) or end <= 0:
            return []
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get_hyper function"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
