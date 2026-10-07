from main import base_solution, compute_cost, list_generater
import pytest

def test_baseline():
    files = list_generater(10, seed=10072026)
    answer = base_solution(files)
    assert answer == 9945


def test_alogrithem():
    files = list_generater(10, seed=10072026)
    answer = compute_cost(files)
    assert answer == 9945


def test_same_answer():
    files = list_generater(10, seed=10072026)
    answer1 = compute_cost(files[::])
    answer2 = base_solution(files[::])
    assert answer1 == answer2 
