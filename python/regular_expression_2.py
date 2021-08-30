import re

PATTERN = "([349]{1})([0-9]{3}-?)([0-9]{2}-?){2}([0-9]{2})"


def is_valid_creditcard(sequence):
   
    for i, n in enumerate(sequence):
        try:
            if (sequence[i], 
                sequence[i+1], 
                sequence[i+2],
                sequence[i+3]
            ) == (n, n, n, n):
                return False
        except IndexError:
            pass
    return bool(re.match(PATTERN, sequence))

print(is_valid_creditcard("3412-1234-5678-2134"))
