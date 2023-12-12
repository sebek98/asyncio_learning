import unittest


async def add(x, y):
    return x + y

class TestCoro(unittest.IsolatedAsyncioTestCase):

    async def syncSetUp(self):
        return await super().asyncSetUp()
    async def test_add(self):
        res = await add(2, 3)
        self.assertEqual(res, 5)

    async def asyncTearDown(self) -> None:
        return await super().asyncTearDown()



if __name__ == "__main__":
    unittest.main()