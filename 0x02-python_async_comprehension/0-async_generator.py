#!/usr/bin/env python3
""" write a coroutine called async_generator that takes no arguments
"""


import asyncio
import random
"""define async generator
"""


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
