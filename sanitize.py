# sanitize.py
# Removes sensitive information from documents using a mark.
# Currently only works on entire lines -- two marks on the same
# line will break the program.

import sys
from collections import Counter

SENSITIVE_MARK = "<!!!>"

def sanitize(text):
    sanitized_text = []
    ignoring_text = False
    for line in text:
        should_ignore_line = False

        if contains_mark(line):
            ignoring_text = not ignoring_text
            should_ignore_line = True

        if not (ignoring_text or should_ignore_line):
            sanitized_text.append(line)

    return sanitized_text

def contains_mark(line):
    return contains(SENSITIVE_MARK, line)

# from http://stackoverflow.com/questions/3847386
def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("USAGE: sanitize.py <filename>")

    with open(sys.argv[1], 'r') as f:
        unsanitized_text = f.readlines()
        for sanitized_line in sanitize(unsanitized_text):
            print(sanitized_line),
