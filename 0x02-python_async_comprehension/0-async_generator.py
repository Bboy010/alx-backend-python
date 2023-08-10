#!/usr/bin/env python3
""" write a coroutine called async_generator that takes no arguments
"""


import asyncio
import random
from typing import Generator


async def async_generator():
    """Define an async generator that yields random floats.

    Yields:
        float: A random float between 0 and 10.
    Raises:
        None: This function does not raise any specific exceptions.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
