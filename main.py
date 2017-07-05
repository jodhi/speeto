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

    def create_socket(self, PORT = 8989):
        HOST = ''

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

    def connect_socket(self, HOST , PORT):
        print('Connecting.... to ',HOST, ' with port ',PORT)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.sendall(b'helllo')
                data = sock.recv(1024)
        except ConnectionRefusedError:
            print('Server refusing connection')
            print('maybe the listener not run yet')

            return -1
        print('get ', data)



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
        inp_splitted = str.split(inp)

        if inp == 'help':
            help()
        elif inp == 'start':
            start()
        elif inp == 'exit':
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
