#!/usr/bin/env python3
"""
type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple, first argument is k
    and second is the square of v
    """
    return (k, v ** 2)
