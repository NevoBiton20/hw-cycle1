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
        # Simple cycle with product < 1
        (
            "two-node cycle product smaller than 1",
            [(1, 2, 0.5), (2, 1, 0.5)],
            True
        ),

        # Simple cycle with product > 1
        (
            "two-node cycle product greater than 1",
            [(1, 2, 2), (2, 1, 3)],
            False
        ),

        # Product exactly 1, should be False because we need smaller than 1
        (
            "cycle product exactly 1",
            [(1, 2, 0.5), (2, 1, 2)],
            False
        ),

        # Three-node cycle with product < 1: 2 * 0.1 * 3 = 0.6
        (
            "three-node cycle product smaller than 1",
            [(1, 2, 2), (2, 3, 0.1), (3, 1, 3)],
            True
        ),

        # Directed path, no cycle
        (
            "directed graph with no cycle",
            [(1, 2, 0.1), (2, 3, 0.1), (3, 4, 0.1)],
            False
        ),

        # Has a cycle, but product is not smaller than 1
        (
            "cycle exists but product too large",
            [(1, 2, 2), (2, 3, 2), (3, 1, 2)],
            False
        ),

        # Larger graph with one hidden good cycle:
        # 3 -> 4 -> 5 -> 3 has product 0.5 * 0.5 * 2 = 0.5
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

        # Larger graph with cycles, but none with product < 1
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

        # Self-loop with weight < 1 is itself a cycle
        (
            "self loop product smaller than 1",
            [(1, 1, 0.7)],
            True
        ),

        # Self-loop with weight exactly 1 is not enough
        (
            "self loop product exactly 1",
            [(1, 1, 1)],
            False
        ),
    ]

    for name, edges, expected in new_cases:
        graph = WeightedDiGraph(edges)
        actual = has_cycle1(graph)

        assert actual == expected, (
            f"{name}: expected {expected}, got {actual}"
        )
