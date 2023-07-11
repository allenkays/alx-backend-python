#!/usr/bin/env python3
"""
This module provides a coroutine that measures runtime
of running async_comprehension four times
"""

import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine measures and returns the total runtime of executing
    async_comprehension 4 times

    Returns:
        float: Total runtime.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time

    return total_time
