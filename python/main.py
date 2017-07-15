# Tested only in python 3

import signal
import sys
from speeto import speeto



def help():
    # help section for program usage & options
    print('Usage: main.py args')
    print('Args: blabla')


def start():  # interactive mode, including listener & client setup
    print('Hi lets get started from the beginning')

def bad_args():
    print('Bad Arguments')

def console(obj):
    while True:
        inp = input(">>> ")
        inp_splitted = inp.split()

        if inp == 'help':
            help()
        elif inp == 'start':
            start()
        elif inp == 'exit':
            print("\nSee ya later")
            exit()
        elif inp_splitted[0] == 'connect':
            if len(inp_splitted) != 3:
                bad_args()
                print('Example: connect 127.0.0.1 8989')
                continue

            try:
                PORT = int(inp_splitted[2])
            except:
                bad_args()
                continue

            HOST = inp_splitted[1]
            obj.connect_socket(HOST,PORT)

        elif inp_splitted[0] == 'listen':
            obj.create_socket()
        else:
            print('Bad command')


def exit_gracefully(signum,frame):
    signal.signal(signal.SIGINT, original_sigint)
    print("\nBye Bye, see ya later")
    sys.exit(1)
    signal.signal(signal.SIGINT,exit_gracefully)

def main():
    a = speeto()
    print('Welcome to Speeto console')
    print('Multiplatform speed test')
    print('')
    print('try to type "help" or "status"')
    print('type "start" for interactive mode')
    print('------------------------')

    console(a)


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    
    main()
