#!/usr/bin/env python3
"""index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range function"""
    return ((page - 1) * page_size, page * page_size)
