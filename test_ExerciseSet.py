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


def test_non_integer_expected_number_of_reps_setter(exercise_set):
    expected_number_of_reps = 1.244
    with pytest.raises(Exception):
        exercise_set.expected_number_of_reps = expected_number_of_reps


def test_negative_expected_number_of_reps_setter(exercise_set):
    expected_number_of_reps = -100
    with pytest.raises(Exception):
        exercise_set.expected_number_of_reps = expected_number_of_reps


def test_correct_expected_number_of_reps_setter(exercise_set):
    expected_number_of_reps = 10
    exercise_set.expected_number_of_reps = expected_number_of_reps
    assert exercise_set.expected_number_of_reps == expected_number_of_reps
