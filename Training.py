from datetime import datetime
from typing import Any, List
# from multipledispatch import dispatch
from Exercise import Exercise


class Training:
    def __init__(self,
                 date: datetime = datetime.now()) -> None:
        self.date = date
        self.exercises = []

    @property
    def date(self) -> datetime:
        return self._date

    @date.setter
    def date(self, date: Any) -> None:
        if not isinstance(date, datetime):
            raise Exception("Data must be of type datetime!")
        self._date = date

    @property
    def exercises(self) -> List[Exercise]:
        return self._exercises

    @exercises.setter
    def exercises(self, exercises: Any) -> None:
        if not isinstance(exercises, List):
            raise Exception("Exercises must be a list!")

        for exercise in exercises:
            if not isinstance(exercise, Exercise):
                raise Exception("All exercises must be Exercise class objects!")

        self._exercises = exercises

    # @dispatch(Exercise)
    def add_exercise(self, exercise: Exercise) -> None:
        if not isinstance(exercise, Exercise):
            raise Exception("Exercise must be Exercise class object!")
        self.exercises.append(exercise)
