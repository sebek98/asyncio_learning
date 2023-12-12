import asyncio

import pytest
import unittest.mock as mock


async def add(x, y):
    return x + y

async def add_delayed(x, y):
    await asyncio.sleep(1)
    return x + y


@pytest.mark.asyncio
async def test_add():
    assert await add(2,3) == 5


@pytest.mark.asyncio
async def test_add_delayed():
    with mock.patch("asyncio.sleep", mock.AsyncMock(return_value=None)):
        assert await add_delayed(2, 3) == 5
