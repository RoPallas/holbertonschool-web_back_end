#!/usr/bin/env python3
"""Coroutine"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import random


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather
    measure total runtime and return it."""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
