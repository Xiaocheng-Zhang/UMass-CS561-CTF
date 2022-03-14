# Writeup for Misc/guess password?

Authors: [Xiaocheng Zhang](https://github.com/Xiaocheng-Zhang/UMass-CS561-CTF)

## Description

Start a Ncat listener and exacute python file that will generate a 4-digit random password from ASCII letters and 0~9. It will wait for two seconds for client to enter the password and give feedback as hints of wrong password (your input has n letters included in the correct password, but there are m letters matched with the position of them). If client entered correct password, the flag is printed out. 

## Exploit

The number of prompts is in the order of hundreds. It will take substantial amount of time and patience if the participant tries to solve the problem by typing the server prompt. Instead, we write a script that can do it for us. Done in python, the script opens a TCP connection with the netcat server and follows the server prompt till the flag is finally printed out. 
s
```python3
#!/usr/bin/env python3
import socket
import string

from sympy import Q

HOST = '127.0.0.1'
PORT = 12345
DATA = string.digits + string.ascii_letters

def guess_passwd(client):
    start_msg = client.recv(1024)
    passwd = DATA[0:4]
    correct_digits = [None, None, None, None]
    correct = 0
    i = 0
    while correct < 4:
        client.send(passwd.encode() + b'\n')
        hint = client.recv(1024)
        num_correct = int(hint.decode()[0])
        if num_correct != 0:
            for n in range(4):
                p = passwd[n] * 4
                client.send(p.encode() + b'\n')
                hint = client.recv(1024)
                remain_correct = int(hint.decode()[0])
                if remain_correct > 0:
                    for k in range(4):
                        p = list(p)
                        p[k] = '-'
                        p = "".join(p)
                        client.send(p.encode() + b'\n')
                        hint = client.recv(1024)
                        # print(hint.decode())
                        temp_correct = int(hint.decode()[19])
                        if temp_correct < remain_correct:
                            correct_digits[k] = passwd[n]
                            correct += 1
                            remain_correct -= 1

        if i < 60:
            i += 4
            passwd = DATA[i:i+4]
        else:
            passwd = DATA[i-2:i+2]
    passwd = correct_digits[0] + correct_digits[1] + correct_digits[2] + correct_digits[3]
    client.send(passwd.encode() + b'\n')
    hint = client.recv(1024)
    print(hint.decode())
        
def work(addr):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    guess_passwd(client)

if __name__ == "__main__":
    work((HOST, PORT))

```