import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()


def test_hello():
    expectedList = ["-1",
                    "-1",
                    "5",
                    "3",
                    "1",
                    "1",
    ]
    testList = [[4, 6, 8, 10, 12, 14],
                [-1, -2, -3, -4, -5, -6, -7],
                [2, 3, 5, 7, 11, 13, 17],
                [4, 6, 8, 11, 12, 14],
                [2, 11, 3, 5, 7, 11, 17, 11],
                [99999989, 99999971, 99999959, 99999941, 99999931],
    ]
    i=0
    for expected in expectedList:
        testArg = testList[i]
        print("Testing: Test case",testArg,"Expected",expected)
        expectedIO.print(expected)
        assert SCOPP_tester.test(testArg ,testIO = testIO,expectedIO = expectedIO)
        i+=1
        print("Test case Passed")
    print("Code is correct.All Test cases passed")
test_hello()