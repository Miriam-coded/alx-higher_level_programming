#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    first = sentence[0]

    if not sentence:
        return 0, None

    return count, first
