# Tested only in python 3
import socket

class speeto:
    def __init__(self):
        self.start = 0
        self.temp_file_name = '.speeto_temp'
        self.temp_file_use = False
        # load/check saved configuration (last/saved session) from local storage
        try:
            with open(self.temp_file_name,'r') as temp_file:
                self.temp_file_use = True
                print("using session file\n")
        except FileNotFoundError:
            # raise
            with open(self.temp_file_name,'w') as temp_file:
                temp_file.write("[speeto_temp_file]\n")
                self.temp_file_use = True
                print('creating new session file\n')

    def write_file(self,data):
        if self.temp_file_use == False:
            return -1
        else:
            with open(self.temp_file_name,'a') as temp_file:
                temp_file.writelines(data)

    def create_socket(self):
        HOST = ''
        PORT = 50007
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            sock.listen(1)
            conn, addr = sock.accept()
            print('Listening .... \n')
            print('note: you can run \"ifconfig\" to know your IP address\n')
            with conn:
                print('connected to ', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    conn.sendall(data)

    def connect_socket(self):
        HOST = ''
        PORT = 50007
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(b'helllo')
            data = sock.recv(1024)
        print('get ', data)



def help():
    # help section for program usage & options
    print('Usage: main.py args')
    print('Args: blabla')




def start():  # interactive mode, including listener & client setup
    print('Hi lets get started from the beginning')


def console(obj):
    while True:
        print('')
        inp = input(">>> ")
        if inp == 'help':
            help()
        elif inp == 'start':
            start()
        elif inp == 'exit':
            exit()
        elif inp == 'connect':
            obj.connect_socket()
        elif inp == 'listen':
            obj.create_socket()


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
    main()
