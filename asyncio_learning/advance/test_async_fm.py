import asyncio

import contextlib
import pytest
from unittest import mock

from asyncio_learning.advance.async_file_manager import AsyncFile

file_content = """Ala
ma
kota"""


@pytest.mark.asyncio
async def test_async_filemanager_type():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        async with AsyncFile("async_file_manger.py") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)

@pytest.mark.asyncio
async def test_async_file_manager():
    async with AsyncFile("async_file_manager.py") as f:
        assert asyncio.iscoroutinefunction(f.read)

@pytest.mark.asyncio
async def test_async_file_content():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        async with AsyncFile("zupa.py") as f:
            res = await f.read()
            assert res == file_content

