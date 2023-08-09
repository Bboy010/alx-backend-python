#!/usr/bin/env python3
"""
write a concurrent coroutines
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
