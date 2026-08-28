def get_events(numbers: list[int]) -> list[int]:
    event_num = []
    for num in numbers:
        if num % 2 == 0:
            event_num.append(num)

    return event_num

