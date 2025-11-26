def create_char_number_dict(start_char, end_char):
    """
    Creates dictionary with characters from start_char to end_char 
    as keys and numbers starting at 0 as values.
    Returns: dict
    """
    return {char: idx for idx, char in 
            enumerate(map(chr, range(ord(start_char), ord(end_char) + 1)))}

def create_unique_list(input_list):
    """
    list without duplicates using list comprehension.
    Returns: list
    """
    unique = []
    [unique.append(x) for x in input_list if x not in unique]
    return unique


def main():
    """Main function to execute the program"""
    start_char = 'a'
    end_char = 'z'

    alphabet_dict = create_char_number_dict(start_char, end_char)
    print(alphabet_dict)


if __name__ == '__main__':
    main()
