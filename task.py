#!/usr/bin/env python3

import random
import string
from interruptingcow import timeout

# only ascii and digit
def run():
    passwd = "".join(random.choices(string.ascii_letters + string.digits, k=4))
    while True:
        with timeout(2):
            try:
                print(f"enter 4-digit password:")
                # print(passwd)
                i = input()
                if len(i) != 4:
                    print("invalid input")
                    continue
                out = 0
                match = 0
                if passwd[0] in i:
                    out += 1
                if passwd[1] in i:
                    out += 1
                if passwd[2] in i:
                    out += 1
                if passwd[3] in i:
                    out += 1
                if passwd[0] == i[0]:
                    match += 1
                if passwd[1] == i[1]:
                    match += 1
                if passwd[2] == i[2]:
                    match += 1
                if passwd[3] == i[3]:
                    match += 1
                if match == 4:
                    with open("flag.txt") as f:
                        print(f.read())
                    break
                print(f"{out} letter included, {match} matched")
            except RuntimeError:
                print("out of time")

if __name__ == "__main__":
    run()