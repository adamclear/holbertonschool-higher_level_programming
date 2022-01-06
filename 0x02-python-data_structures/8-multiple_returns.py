#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuplestherapy = (len(sentence), sentence[0])
    else:
        tuplestherapy = (len(sentence), None)
    return tuplestherapy
