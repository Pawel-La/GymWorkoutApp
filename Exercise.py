from typing import Optional


# TODO -> add weight units like Kgs and Lbs
# TODO -> add sets as new class because each set might have different weight
class Exercise:
    def __init__(self,
                 name: str,
                 number_of_exercise_sets: int) -> None:
        self.name = name
        self.number_of_exercise_sets = number_of_exercise_sets
        self.exercise_sets = [None for _ in range(number_of_exercise_sets)]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if not isinstance(name, str):
            raise Exception("Exercise name must be a string!")
        self._name = name

    @property
    def number_of_exercise_sets(self) -> int:
        return self._number_of_sets

    @number_of_exercise_sets.setter
    def number_of_exercise_sets(self, number_of_exercise_sets) -> None:
        if not isinstance(number_of_exercise_sets, int):
            raise Exception("Number of sets must be an integer!")
        if number_of_exercise_sets <= 0:
            raise Exception("Number of sets must be a positive number!")
        if number_of_exercise_sets > 5:
            raise Exception("Too many sets, more isn't always better!")
        self._number_of_sets = number_of_exercise_sets
        self.exercise_sets = [None for _ in range(number_of_exercise_sets)]

    # def add_exercise_set(self, ):
