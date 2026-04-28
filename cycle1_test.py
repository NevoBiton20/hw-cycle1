import pytest
from cycle1 import has_cycle1, WeightedDiGraph
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    graph = WeightedDiGraph(*input)
    return has_cycle1(graph)
    

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    new_cases = [
        (
            "two-node cycle product smaller than 1",
            [(1, 2, 0.5), (2, 1, 0.5)],
            True
        ),
        (
            "two-node cycle product greater than 1",
            [(1, 2, 2), (2, 1, 3)],
            False
        ),
        (
            "cycle product exactly 1",
            [(1, 2, 0.5), (2, 1, 2)],
            False
        ),
        (
            "three-node cycle product smaller than 1",
            [(1, 2, 2), (2, 3, 0.1), (3, 1, 3)],
            True
        ),
        (
            "directed graph with no cycle",
            [(1, 2, 0.1), (2, 3, 0.1), (3, 4, 0.1)],
            False
        ),
        (
            "cycle exists but product too large",
            [(1, 2, 2), (2, 3, 2), (3, 1, 2)],
            False
        ),
        (
            "larger graph with hidden product smaller than 1 cycle",
            [
                (1, 2, 10),
                (2, 3, 10),
                (3, 4, 0.5),
                (4, 5, 0.5),
                (5, 3, 2),
                (5, 6, 10),
                (6, 7, 10),
            ],
            True
        ),
        (
            "larger graph with no product smaller than 1 cycle",
            [
                (1, 2, 2),
                (2, 3, 2),
                (3, 1, 2),
                (3, 4, 1.5),
                (4, 5, 2),
                (5, 3, 2),
                (5, 6, 0.5),
            ],
            False
        ),
        (
            "self loop product smaller than 1",
            [(1, 1, 0.7)],
            True
        ),
        (
            "self loop product exactly 1",
            [(1, 1, 1)],
            False
        ),
    ]

    for name, edges, expected in new_cases:
        graph = WeightedDiGraph(*edges)
        actual = has_cycle1(graph)

        assert actual == expected, (
            f"{name}: expected {expected}, got {actual}"
        )
