from typing import Optional


# TODO -> add weight units like Kgs and Lbs
# TODO -> add ability to specify number of reps in each set
class Exercise:
    def __init__(self,
                 name: str,
                 number_of_exercise_sets: int,
                 expected_number_of_reps_in_each_set: int = None) -> None:
        self.name = name
        self.number_of_exercise_sets = number_of_exercise_sets
        self.expected_number_of_reps_in_each_set = \
            expected_number_of_reps_in_each_set

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
        return self._number_of_exercise_sets

    @number_of_exercise_sets.setter
    def number_of_exercise_sets(self, number_of_exercise_sets) -> None:
        if not isinstance(number_of_exercise_sets, int):
            raise Exception("Number of sets must be an integer!")
        if number_of_exercise_sets <= 0:
            raise Exception("Number of sets must be a positive number!")
        if number_of_exercise_sets > 5:
            raise Exception("Too many sets, more isn't always better!")
        self._number_of_exercise_sets = number_of_exercise_sets

    @property
    def expected_number_of_reps_in_each_set(self) -> Optional[int]:
        return self._expected_number_of_reps_in_each_set

    @expected_number_of_reps_in_each_set.setter
    def expected_number_of_reps_in_each_set(
            self,
            expected_number_of_reps_in_each_set) -> None:

        if not hasattr(self, 'expected_number_of_reps_in_each_set') and \
                expected_number_of_reps_in_each_set is None:
            self._expected_number_of_reps_in_each_set = None
            return

        if not isinstance(expected_number_of_reps_in_each_set, int):
            raise Exception("Expected number of reps in each set must "
                            "be an integer!")
        if expected_number_of_reps_in_each_set <= 0:
            raise Exception("Expected number of reps in each set must "
                            "be a positive number!")

        self._expected_number_of_reps_in_each_set = \
            expected_number_of_reps_in_each_set
