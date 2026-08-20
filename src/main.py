def count_word_frequency(words: list[str]) -> dict[str, int]:
    frequency = {}
    for item in words:
        frequency[item] = frequency.get(item, 0) + 1 
    return frequency

def reverse_string(text: str) -> str:
    return text[::-1]