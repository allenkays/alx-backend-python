#!/usr/bin/env python3
"""
This coroutine takes in an interger as its maximum delay and chooses
a wait time between 0 and the given number.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay

    Args:
        max_delay (int): Maximum delay in seconds(defaults:10)

    Returns:
        float: Random delay between 0 and max_delay (inclusive)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
