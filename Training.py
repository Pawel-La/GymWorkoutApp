from datetime import datetime
from typing import Any, List, Dict
from Exercise import Exercise


class Training:
    def __init__(self,
                 date: datetime = datetime.now(),
                 list_of_exercises: List[Exercise] = None) -> None:
        self.date = date
        self.dict_of_exercises = dict()
        if list_of_exercises is not None:
            self.add_multiple_exercises(list_of_exercises)

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
    def dict_of_exercises(self,
                          dict_of_exercises: Dict[str, Exercise]) -> None:
        if hasattr(self, 'dict_of_exercises'):
            raise Exception("Exercises are already set, setting them again "
                            "would cause lost of data. "
                            "Try other methods instead ie. add_one_exercise, "
                            "add_multiple_exercises or remove_all_exercises.")
        self._dict_of_exercises = dict_of_exercises

    def add_one_exercise(self,
                         exercise: Exercise,
                         dict_of_exercises: Dict[str, Exercise] = None) -> None:
        if dict_of_exercises is None:
            dict_of_exercises = self._dict_of_exercises

        if not isinstance(exercise, Exercise):
            raise Exception("Exercise must be Exercise class object!")
        if exercise.name in dict_of_exercises:
            raise Exception("Exercise with this name already exists "
                            "in current training!")
        dict_of_exercises[exercise.name] = exercise

    def add_multiple_exercises(self, exercises: List[Exercise]) -> None:
        if not isinstance(exercises, List):
            raise Exception("Exercises must be list!")

        tmp_dict = self.dict_of_exercises.copy()
        try:
            for exercise in exercises:
                self.add_one_exercise(exercise, tmp_dict)
        except Exception:
            raise Exception("Error while adding one of exercises!")
        else:
            for exercise in exercises:
                self.add_one_exercise(exercise)
