#!/usr/bin/env python3

"""
This module provides a coroutine that returns a tasks object.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object that wraps the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: Task object representing the execution of wait_random.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
