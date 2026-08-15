def get_odd_numbers(numbers: list[int]) -> list[int]:
    odds = []
    for number in numbers:
        if number % 2 != 0:
            odds.append(number)
    return odds 

