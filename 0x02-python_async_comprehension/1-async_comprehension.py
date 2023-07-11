#!/usr/bin/env python3
"""
Async Comprehensions
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine collects 10 random numbers using async comprehensing
    over async_generator

    Returns:
        List[float]: List of 10 random numbers
    """
    return [num async for num in async_generator()][:10]
