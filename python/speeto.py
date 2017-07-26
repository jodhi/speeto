import socket,time

class speeto:
    def __init__(self):
        self.start = 0
        self.temp_file_name = '.speeto_temp'
        self.temp_file_use = False
        self.QUOTA_1 = 100000
        self.QUOTA_2 = 500000
        self.QUOTA_3 = 1000000
        self.QUOTA_4 = 2000000
        self.QUOTA_5 = 5000000
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
                    handshake = conn.recv(1024)
                    if not handshake: break;
                    if handshake.decode('utf-8') =="test_speed" :

                        conn.sendall(b'accept1')
                        data = conn.recv(1024)
                        data = conn.recv(10240)
                        data = conn.recv(102400)

                        conn.sendall(b'accept2')

                        # speed test 1
                        base_time_speed1 = time.time()
                        conn.sendall(b'.' * self.QUOTA_3)
                        self.speed_down1 = (self.QUOTA_3 / 1000) / (time.time() - base_time_speed1)
                        print('speed 1 is ', self.speed_down1, 'KBps')

                        # speed test 2
                        base_time_speed2 = time.time()
                        conn.sendall(b'.' * self.QUOTA_4)
                        self.speed_down2 = (self.QUOTA_4 / 1000) / (time.time() - base_time_speed1)
                        print('speed 2 is ', self.speed_down2, 'KBps')
                    sock.close()

    def connect_socket(self, HOST , PORT):
        # handshake



        base_time = time.time()
        print('Connecting.... to ',HOST, ' with port ',PORT)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.sendall(b'test_speed')
                acc = sock.recv(1024)
                if acc.decode('utf-8') == "accept1":
                    self.latency = time.time() - base_time
                    # test uplink speed
                    print("connected, testing upload speed...")
                    # speed test 1
                    base_time_speed1 = time.time()
                    sock.sendall(b'.' * self.QUOTA_1)
                    self.speed1 = (self.QUOTA_1/1000) / (time.time() - base_time_speed1)
                    print('speed 1 is ', self.speed1 , 'KBps')

                    # speed test 2
                    base_time_speed2 = time.time()
                    sock.sendall(b'.' * self.QUOTA_2)
                    self.speed2 =  (self.QUOTA_2/1000) / (time.time() - base_time_speed1)
                    print('speed 2 is ', self.speed2 , 'KBps')

                    # speed test 3
                    base_time_speed3 = time.time()
                    sock.sendall(b'.' * self.QUOTA_3)
                    self.speed3 =  (self.QUOTA_3/1000) / (time.time() - base_time_speed3)
                    print('speed 3 is ', self.speed3 , 'KBps')

                    # condition for more test if too fast

                if acc.decode('utf-8') == "accept1":
                    print("Testing Download Speed")
                    # Download Speed
                    data = sock.recv(102400)
                    data = sock.recv(102400)

                sock.close()
        except ConnectionRefusedError:
            print('Server refusing connection')
            print('maybe the listener not run yet')

            return -1

        print('latency is ', self.latency)

        return True

    def test_speed(self, HOST, PORT):
        # Send data packet for speed test
        print('Test Speed')


