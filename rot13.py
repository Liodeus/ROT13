#!/usr/bin/env Python3
# -*- encoding:utf_8 -*-

import alphabet

text = "Why did the chicken cross the road ?"
text2 = "Jul qvq gur puvpxra pebff gur ebnq ?"


def encode(string):
    encodeString = ""

    for letter in string:
        if letter == " ":
            encodeString += " "
        elif letter in alphabet.alpha:
            encodeString += alphabet.alpha[letter]
        elif letter in alphabet.lower:
            encodeString += alphabet.lower[letter]
        else:
            encodeString += letter

    return encodeString


def decode(string):
    decodeString = ""

    for letter in string:
        if letter == " ":
            decodeString += " "
        elif letter in alphabet.betaReverse:
            decodeString += alphabet.betaReverse[letter]
        elif letter in alphabet.lower:
            decodeString += alphabet.betaReverseLower[letter]
        else:
            decodeString += letter

    return decodeString


print(encode(text))
print(decode(text2))
