import pytest
from ExerciseSet import ExerciseSet


@pytest.fixture
def exercise_set() -> ExerciseSet:
    weight = 10
    expected_number_of_reps = 12
    exercise_set = ExerciseSet(weight, expected_number_of_reps)
    return exercise_set


def test_non_numeric_weight_setter(exercise_set):
    weight = "a"
    with pytest.raises(Exception):
        exercise_set.weight = weight


def test_negative_number_weight_setter(exercise_set):
    weight = -100
    with pytest.raises(Exception):
        exercise_set.weight = weight


def test_correct_weight_setter(exercise_set):
    weight = 100.75
    exercise_set.weight = weight
    assert exercise_set.weight == weight
