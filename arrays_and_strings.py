def check_permutation(s1: str, s2: str) -> bool:
    """
    Question 1.2
    """

    if len(s1) != len(s2):
        return False

    s1_chars_count = {}

    # create map letter value of s1
    for letter in s1:
        if letter in s1_chars_count:
            s1_chars_count[letter] += 1
        else:
            s1_chars_count[letter] = 1

    # for every element in s2 remove an item from s1
    for letter in s2:
        if letter in s1_chars_count:
            if s1_chars_count[letter] == 0:
                return False
            else:
                s1_chars_count[letter] -= 1
        else:
            return False
    return True
