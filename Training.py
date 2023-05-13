from datetime import datetime
from typing import Any, List, Dict
from Exercise import Exercise


# def get_dict_of_exercises_names_and_exercises_from_exercises_list(
#         list_of_exercises: List[Exercise]) -> Dict[str, Exercise]:
#     dict_of_exercises_names_and_exercises = dict()
#
#     for exercise in list_of_exercises:
#         if not isinstance(exercise, Exercise):
#             raise Exception("All exercises must be Exercise class objects!")
#         if exercise.name in dict_of_exercises_names_and_exercises:
#             raise Exception("Different exercises in the same training must "
#                             "have different names!")
#         dict_of_exercises_names_and_exercises[exercise.name] = exercise
#
#     return dict_of_exercises_names_and_exercises


class Training:
    def __init__(self,
                 date: datetime = datetime.now(),
                 list_of_exercises: List[Exercise] = None) -> None:
        self.date = date
        self.dict_of_exercises = dict()
        # if list_of_exercises is not None:
        #     self.add_multiple_exercises(list_of_exercises)

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, date: Any) -> None:
        if not isinstance(date, datetime):
            raise Exception("Data must be of type datetime!")
        self._date = date

    @property
    def dict_of_exercises(self) -> Dict[str, Exercise]:
        return self._dict_of_exercises

    @dict_of_exercises.setter
    def dict_of_exercises(self, dict_of_exercises: Dict) -> None:
        if hasattr(self, 'dict_of_exercises'):
            raise Exception("Exercises are already set, setting them again "
                            "would cause lost of data. "
                            "Try other methods instead ie. add_one_exercise, "
                            "add_multiple_exercises or remove_all_exercises.")
        self._dict_of_exercises = dict_of_exercises

    def add_one_exercise(self, exercise: Exercise) -> None:
        if not isinstance(exercise, Exercise):
            raise Exception("Exercise must be Exercise class object!")
        if exercise.name in self.dict_of_exercises:
            raise Exception("Exercise with this name already exists "
                            "in current training!")
        self.dict_of_exercises[exercise.name] = exercise

    # def add_multiple_exercises(self, exercises: List[Exercise]) -> None:
    #     if not isinstance(exercises, List):
    #         raise Exception("Exercises must be list!")
    #     for exercise in exercises:
    #         self.add_one_exercise(exercise)
