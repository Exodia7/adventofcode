import os.path

from shared.challenge import DaySolutionDTO, Challenge


class ChallengeDay02(Challenge):
    @classmethod
    def id(cls):
        return "Day2"

    def _solve(self):
        # 1. read input data
        input_file = "input_day02.txt"  # "test_input.txt"
        input_file_path = os.path.join(os.path.dirname(__file__), input_file)
        input_data = self.parse_input_data(input_file_path)

        # 2. compute the solution
        num_valid_levels_part1 = sum(
            [self.__is_valid_level_part1(level) for level in input_data]
        )
        num_valid_levels_part2 = sum(
            [self.__is_valid_level_part2(level) for level in input_data]
        )

        # 3. set the solution
        self.set_solution(num_valid_levels_part1, num_valid_levels_part2)

    @staticmethod
    def parse_input_data(input_file_path: str) -> list[list[int]]:
        with open(input_file_path, "r") as file:
            lines = file.readlines()
            stripped_lines = [line.strip() for line in lines]
            valid_lines = [line for line in stripped_lines if line != ""]
            nums = [[int(item) for item in line.split()] for line in valid_lines]
        return nums

    def __is_valid_level_part1(self, level: list[int]) -> bool:
        level_is_all_increasing = self.__is_level_fully_increasing(level)
        level_is_all_decreasing = self.__is_level_fully_decreasing(level)
        level_has_increases_in_range = (
            self.__level_has_increases_and_decreases_in_range(
                level, lower_bound=1, upper_bound=3
            )
        )

        return (
            level_is_all_increasing or level_is_all_decreasing
        ) and level_has_increases_in_range

    def __is_valid_level_part2(self, level: list[int]) -> bool:
        if self.__is_valid_level_part1(level):
            return True
        else:
            # Can we remove 1 number from the level to make it work?
            for i in range(len(level)):
                if self.__is_valid_level_part1(level[:i] + level[i + 1 :]):
                    return True
            return False

    @staticmethod
    def __is_level_fully_increasing(level: list[int]) -> bool:
        return all([level[i + 1] - level[i] >= 0 for i in range(len(level) - 1)])

    def __is_level_fully_decreasing(self, level: list[int]) -> bool:
        return self.__is_level_fully_increasing([-elem for elem in level])

    @staticmethod
    def __level_has_increases_and_decreases_in_range(
        level: list[int], lower_bound: int = 1, upper_bound: int = 3
    ) -> bool:
        abs_differences = [abs(level[i + 1] - level[i]) for i in range(len(level) - 1)]
        return all([lower_bound <= diff <= upper_bound for diff in abs_differences])

    def _print_solution(self):
        print(f"Solution: ")
        print(f"- part 1: There are {self.solution_part1} valid levels in the input")
        print(
            f"- part 2: There are {self.solution_part2} valid levels in the input if you can remove a single number per level"
        )
