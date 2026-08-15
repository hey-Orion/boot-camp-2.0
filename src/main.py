def get_odd_numbers(numbers: list[int]) -> list[int]:
    odds = []
    for number in numbers:
        if number % 2 != 0:
            odds.append(number)
    return odds 

def count_char_frequency(text: str) -> dict[str, int]:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1 
    return counts 

def sum_key_values(dict_list: list[dict], target_key: str) -> int:
    total = 0 
    for item in dict_list:
        if target_key in item:
            total += item[target_key]
    return total

def remove_duplicates(items: list[str]) -> list[str]:
    cleaned = []

    for item in items:
        if item not in cleaned:
            cleaned.append(item)
    return cleaned

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    return " ".join(reversed(words))