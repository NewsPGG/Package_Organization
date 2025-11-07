from Sorting.Bubble_sort import bubble_sort
import pytest

@pytest.mark.parametrize(
    ["input", "output"],
    [
        ([9, 1, 6, 5, 7, 12], [1, 5, 6, 7, 9, 12]),
        ([-4, -1, -18, -9, -8, -3], [-18, -9, -8, -4, -3, -1]),
        ([101, -98, 34, 52, 0, 17, 91, -32, -44], [-98, -44, -32, 0, 17, 34, 52, 91, 101]),
    ],
)

def test_bubble_sort(input, output):
    assert bubble_sort(input) == output

def test_bubble_sort_one_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_zero_element():
    assert bubble_sort([]) == []

def test_bubble_sort_same_elements():
    assert bubble_sort([2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]

def test_bubble_sort_correct_sorting():
    assert bubble_sort([-9, -2, 0, 1, 4, 8, 17]) == [-9, -2, 0, 1, 4, 8, 17]