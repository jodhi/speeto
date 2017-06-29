def help(): #help section for program usage & options
    print('Usage: main.py args')
    print('Args: blabla')

def init(): #load/check saved configuration (last/saved session) from local storage
    #check whether local saved session available
    print('checking')

def start(): #interactive mode, including listener & client setup
    print('Hi lets get started from the beginning')

def console():
    while True:
        print('')
        inp = input(">>> ")
        if(inp=='help'):
            help()
        if(inp=='start'):
            start()

def main():
    print('Welcome to Speeto console')
    print('Multiplatform speed test')
    print('')
    print('try to type "help" or "status"')
    print('type "start" for interactive mode')
    print('------------------------')

    console()




if __name__ == '__main__':
    init()
    main()
