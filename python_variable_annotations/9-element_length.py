#!/usr/bin/env python3
"""
Duck type
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with an element and
    the element's length
    """
    return [(i, len(i)) for i in lst]
