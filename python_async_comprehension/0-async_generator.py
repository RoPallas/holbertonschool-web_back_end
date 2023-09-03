#!/usr/bin/env python3
"""Coroutine"""
import asyncio
import random


async def async_generator() -> float:
    """yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
