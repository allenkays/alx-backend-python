#!/usr/bin/env python3

"""
This module provides a coroutine that works asynchronously with
tasks.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay and returns the list
    of all the delays (float values) in ascending order.

    Args:
        n (int): Number of times to spawn the task_wait_random task.
        max_delay (int): Maximum delay in seconds for each
        task_wait_random task.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in tasks:
        await task
        delays.append(task.result())

    return sorted(delays)
