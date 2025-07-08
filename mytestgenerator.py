import re


def process_and_replace(text: str, processor_func: callable) -> str:
    """
    Finds all occurrences of 'asdfasdfasdf(text)' and replaces them.

    Args:
        text: The input string to search within.
        processor_func: The function to call on the captured text.

    Returns:
        The modified string.
    """
    # This regex finds 'asdfasdfasdf(' followed by any characters '.*?'
    # until the next ')' and captures the content inside the parentheses.
    # The '.*?' is a non-greedy match.
    pattern = re.compile(r"num_with_checksum\(\"(.*?)\"\)")

    # re.sub() finds all matches and replaces them.
    # The lambda function receives the match object 'm'.
    # m.group(1) is the captured content (the 'IMPORTANT' part).
    # We call the processor_func on it and format the replacement string.
    return pattern.sub(lambda m: f'"{processor_func(m.group(1))}"', text)


# code adopted from wikipedia pseudocode of Luhn Algorithm
# https://en.wikipedia.org/wiki/Luhn_algorithm
def create_checksum(num):
    """Calculates the final checksum of a number as a string."""
    sum = 0
    i = len(num) - 1
    other_i = 0
    while True:
        if i < 0:
            break
        # selectively double characters depending on position
        n = 2 * int(num[i]) if other_i % 2 == 0 else int(num[i])
        # if doubling character results in > 9, subtract 9
        if n > 9:
            n -= 9
        # add number to working sum
        sum += n
        # update position and parity
        other_i += 1
        i -= 1
    return (10 - sum % 10) % 10


def num_with_checksum(num):
    """Creates a number with a checksum."""
    checksum = create_checksum(num)
    return num + str(checksum)


# 1. Define a function to process the captured text
def my_processing_function(captured_text: str) -> str:
    """Example function that converts text to uppercase."""
    return num_with_checksum(captured_text)


with open("tests_template.py") as f:
    input_string = f.read()

    # 3. Call the main function
    result = process_and_replace(input_string, my_processing_function)

    # 4. Print the result
    print("\nOriginal:", input_string)
    print("Result:  ", result)

    with open("tests.py", "w") as f:
        f.write(result)
