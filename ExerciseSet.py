class ExerciseSet:
    def __init__(self,
                 weight: int,
                 expected_number_of_reps: int):
        self.weight = weight
        self.expected_number_of_reps = expected_number_of_reps
        self.number_of_completed_reps = 0

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise Exception("Weight must be of numeric type!")
        if weight <= 0:
            raise Exception("Weight can't be a negative number!")
        self._weight = weight

    @property
    def expected_number_of_reps(self):
        return self._expected_number_of_reps

    @expected_number_of_reps.setter
    def expected_number_of_reps(self, expected_number_of_reps):
        if not isinstance(expected_number_of_reps, int):
            raise Exception("Expected number of reps must be an integer!")
        if expected_number_of_reps <= 0:
            raise Exception("Expected number of reps must be positive!")
        self._expected_number_of_reps = expected_number_of_reps

    @property
    def number_of_completed_reps(self):
        return self._number_of_completed_reps

    @number_of_completed_reps.setter
    def number_of_completed_reps(self, number_of_completed_reps):
        if not isinstance(number_of_completed_reps, int):
            raise Exception("Number of completed reps must be an integer!")
        if number_of_completed_reps < 0:
            raise Exception("Number of completed reps can't be negative!")
        if hasattr(self, 'number_of_completed_reps') and \
                self.number_of_completed_reps > 0:
            raise Exception("Number of completed reps has been already set!")
        self._number_of_completed_reps = number_of_completed_reps

    def summary(self) -> str:
        return f"Weight: {self.weight}\n" \
               f"Expected number of reps: {self.expected_number_of_reps}\n" \
               f"Number of completed reps: {self.number_of_completed_reps}"
