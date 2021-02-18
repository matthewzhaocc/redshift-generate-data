#!/usr/bin/python3

import sys

import json

import string
import random

def generate_random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(string.ascii_lowercase)
    return result

def generate_file(length):
    f = open("result.json", "a+")
    for i in range(length):
        pl = {
            "name": generate_random_string(7),
            "age": random.randint(1, 99),
            "email": generate_random_string(7)+"@"+generate_random_string(4)+".com"
        }
        f.write(json.dumps(pl)+"\n")
    f.close()

if __name__ == "__main__":
    generate_file(int(sys.argv[1]))