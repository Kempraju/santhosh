def first_non_repeated_char(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    for char in s:
        if char_counts[char] == 1:
            return char
    
    return None