# Tested only in python 3
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



def help():
    # help section for program usage & options
    print('Usage: main.py args')
    print('Args: blabla')




def start():  # interactive mode, including listener & client setup
    print('Hi lets get started from the beginning')


def console():
    while True:
        print('')
        inp = input(">>> ")
        if inp == 'help':
            help()
        elif inp == 'start':
            start()
        elif inp == 'exit':
            exit()


def main():
    a = speeto()
    print('Welcome to Speeto console')
    print('Multiplatform speed test')
    print('')
    print('try to type "help" or "status"')
    print('type "start" for interactive mode')
    print('------------------------')

    console()


if __name__ == '__main__':
    main()
