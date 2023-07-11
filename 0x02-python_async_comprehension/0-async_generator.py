#!/usr/bin/env python3
"""
This module provides a coroutine that loops 10 times
asynchronously waiting 1 second and yielding a random number
between 0 and 10
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that yields a random number between 0 and 10
    asyncronously after a second's asyncronous wait

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
