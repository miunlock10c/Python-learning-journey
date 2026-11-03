import re

def reverse_words(s):
    parts = re.split(r"(\s+)", s)
    reversed_parts = [part[::-1] if not part.isspace() else part for part in parts]
    result = ''.join(reversed_parts)
    return result

