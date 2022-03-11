#! /bin/sh

ncat -lvkp 12345 -e "/usr/local/bin/python3 task.py"