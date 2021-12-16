#!/usr/bin/env python3

import socket
import sys
import random

HOST = "codechallenge-daemons.0x14.net"
PORT = 4321
BUF_SIZE = 1024

IS_EXIT = "is exit?\n"
LOOK = "look\n"

LOOK_RESPONSE = "Well, well, well, my friend. You could do these movements:"

def find_oposite(direction: str) -> str:
    if direction == "north":
        return "south"
    elif direction == "south":
        return "north"
    elif direction == "west":
        return "east"
    return "west"

def main() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(BUF_SIZE)
        print(data)
        last_movement = ""
        while True:
            s.sendall(IS_EXIT.encode())
            data = s.recv(BUF_SIZE)
            if not data or data != b'No. Sorry, traveller...\n':
                print(data)
                return 0
            s.sendall(LOOK.encode())
            data = s.recv(BUF_SIZE)
            available_movements = data.decode()[len(LOOK_RESPONSE):].split()
            print(data)
            if not data:
                return 0
            elif len(last_movement) and len(available_movements) > 1:
                available_movements.remove(last_movement)
            next_movement = random.choice(available_movements)
            last_movement = find_oposite(next_movement)
            s.sendall(next_movement.encode())
            data = s.recv(BUF_SIZE)
            print(data)
            if not data:
                return 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
