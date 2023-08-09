#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax
Write a function task_wait_random that takes
an integer max_delay and returns a asyncio.Task.
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int): [description]

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.create_task(wait_random(max_delay))
