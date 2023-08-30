#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a list of random float numbers"""
    list_delay = []
    for i in range(n):
        list_delay.append(await task_wait_random(max_delay))
    return sorted(list_delay)
