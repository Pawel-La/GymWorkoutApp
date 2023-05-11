class ExerciseSet:
    def __init__(self,
                 weight: int,
                 expected_number_of_reps: int):
        self.weight = weight
        self.expected_number_of_reps = expected_number_of_reps
        self.number_of_completed_reps = 0

    def summary(self) -> str:
        return f"Weight: {self.weight}\n" \
               f"Expected number of reps: {self.expected_number_of_reps}\n" \
               f"Number of completed reps: {self.number_of_completed_reps}"
