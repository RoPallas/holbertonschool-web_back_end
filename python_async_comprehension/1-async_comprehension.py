#!/usr/bin/env python3
"""Coroutine"""
async_generator = __import__('0-async_generator').async_generator
import asyncio
import random
import typing


async def async_comprehension() -> typing.List[float]:
    """collect 10 random numbers using an async comprehensing over async
    generator"""
    return [i async for i in async_generator()]
