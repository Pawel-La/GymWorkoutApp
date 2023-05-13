from Training import Training
from Exercise import Exercise
from datetime import datetime
import pytest


@pytest.fixture
def training() -> Training:
    year = 2023
    month = 5
    day = 8
    hour = 9
    minute = 45

    date = datetime(year=year,
                    month=month,
                    day=day,
                    hour=hour,
                    minute=minute)
    training = Training(date)
    return training


def test_exercises_initialized(training):
    assert training.dict_of_exercises == dict()


def test_correct_date_setter(training):
    date = datetime.now()
    training.date = date
    assert date == training.date


def test_incorrect_class_object_date_setter(training):
    date = 10
    with pytest.raises(Exception):
        training.date = date
    assert training.date != date


# def test_correct_exercises_list_setter(training):
#     exercises = [Exercise(name="Pull up", number_of_exercise_sets=5),
#                  Exercise(name="Push up", number_of_exercise_sets=4)]
#     training.exercises = exercises
#     assert exercises == training.exercises


# def test_incorrect_exercises_list_setter(training):
#     exercises = [Exercise(name="Pull up", number_of_exercise_sets=5),
#                  Exercise(name="Push up", number_of_exercise_sets=4),
#                  512412]
#
#     with pytest.raises(Exception):
#         training.exercises = exercises
#     assert training.exercises != exercises


def test_correct_add_one_exercise(training):
    exercise = Exercise(name="Pull up", number_of_exercise_sets=5)
    training.add_one_exercise(exercise)
    assert training.dict_of_exercises[exercise.name] == exercise


def test_incorrect_class_object_add_one_exercise(training):
    exercise = 10
    with pytest.raises(Exception):
        training.add_one_exercise(exercise)


def test_already_exists_add_one_exercise(training):
    exercise1 = Exercise(name="Pull up", number_of_exercise_sets=5)
    exercise2 = Exercise(name="Pull up", number_of_exercise_sets=4)
    training.add_one_exercise(exercise1)
    with pytest.raises(Exception):
        training.add_one_exercise(exercise1)
    with pytest.raises(Exception):
        training.add_one_exercise(exercise2)
    assert len(training.dict_of_exercises) == 1
    assert training.dict_of_exercises[exercise1.name] == exercise1
