import pytest
from Exercise import Exercise


@pytest.fixture
def exercise() -> Exercise:
    name = "Pull ups"
    number_of_sets = 3
    exercise = Exercise(name, number_of_sets)
    return exercise


def test_correct_name_setter(exercise):
    name = "Push ups"
    exercise.name = name
    assert exercise.name == name


def test_incorrect_name_setter(exercise):
    name = 10
    with pytest.raises(Exception):
        exercise.name = name
    assert exercise.name != name


def test_non_integer_number_of_exercise_sets(exercise):
    number_of_exercise_sets = "wrong input"
    with pytest.raises(Exception):
        exercise.number_of_exercise_sets = number_of_exercise_sets
    assert exercise.number_of_exercise_sets != number_of_exercise_sets


def test_non_positive_number_of_exercise_sets(exercise):
    number_of_exercise_sets = -3
    with pytest.raises(Exception):
        exercise.number_of_exercise_sets = number_of_exercise_sets
    assert exercise.number_of_exercise_sets != number_of_exercise_sets


def test_too_big_number_of_exercise_sets(exercise):
    number_of_exercise_sets = 6
    with pytest.raises(Exception):
        exercise.number_of_exercise_sets = number_of_exercise_sets
    assert exercise.number_of_exercise_sets != number_of_exercise_sets


# def test_correct_number_of_exercise_sets(exercise):
#     number_of_exercise_sets = 4
#     exercise.number_of_exercise_sets = number_of_exercise_sets
#
#     assert exercise.number_of_exercise_sets == number_of_exercise_sets
#     assert len(exercise.exercise_sets) == number_of_exercise_sets

def test_init_to_none_expected_number_of_reps_in_each_set():
    name = "Pull ups"
    number_of_sets = 3
    exercise = Exercise(name, number_of_sets)
    assert exercise.expected_number_of_reps_in_each_set is None


def test_none_expected_number_of_reps_in_each_set(exercise):
    with pytest.raises(Exception):
        exercise.expected_number_of_reps_in_each_set = None


def test_incorrect_expected_number_of_reps_in_each_set(exercise):
    x = "wrong number"
    y = 2.4124
    z = -512
    with pytest.raises(Exception):
        exercise.expected_number_of_reps_in_each_set = x
    with pytest.raises(Exception):
        exercise.expected_number_of_reps_in_each_set = y
    with pytest.raises(Exception):
        exercise.expected_number_of_reps_in_each_set = z


def test_correct_expected_number_of_reps_in_each_set(exercise):
    x = 10
    exercise.expected_number_of_reps_in_each_set = x
    assert exercise.expected_number_of_reps_in_each_set == x
