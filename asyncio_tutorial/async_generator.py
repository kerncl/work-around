import asyncio

# @asyncio.coroutines
# def py34_coro():
#     """Generator-based coroutine"""
#     # No need to build these yourself but be aware of what they are
#     s = yield from stuff()
#     return s

async def py35_coro():
    s = await stuff()
    print(s)
    return s


async def stuff():
    return 0x10, 0x20, 0x30

if __name__ == '__main__':
    print()
    py35_coro()