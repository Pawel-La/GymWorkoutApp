import pytest
from ExerciseSet import ExerciseSet


@pytest.fixture
def exercise_set() -> ExerciseSet:
    weight = "Pull ups"
    expected_number_of_reps = 12
    exercise_set = ExerciseSet(weight, expected_number_of_reps)
    return exercise_set
