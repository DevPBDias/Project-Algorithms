def insertion_sort(string):
    word = list(string.lower())
    n = len(word)

    for index in range(1, n):
        key = word[index]

        new_position = index - 1
        while new_position >= 0 and word[new_position] > key:
            word[new_position + 1] = word[new_position]
            new_position = new_position - 1

        word[new_position + 1] = key
    return word


def is_anagram(first_string, second_string):
    first_case = insertion_sort(first_string)
    second_case = insertion_sort(second_string)
    first_word = "".join(first_case)
    second_word = "".join(second_case)

    if len(first_string) == 0 or len(second_string) == 0:
        return (first_word, second_word, False)
    if first_word != second_word:
        return (first_word, second_word, False)
    if first_word == second_word:
        return (first_word, second_word, True)
