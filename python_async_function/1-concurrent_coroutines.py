#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a list of random float numbers"""
    list_delay = []
    for i in range(n):
        list_delay.append(await wait_random(max_delay))
    return sorted(list_delay)
