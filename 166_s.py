import socket
class echo:
    def __init__(self, host='0.0.0.0',port=2222):
        self.host = host
        self.port = port

    def serve(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host,self.port))
        sock.listen(10)
        while True:
            conn, addr = sock.accept()
            print('New connection:',addr)
            self.on_connect(conn, addr)

    def on_connect(self,conn,addr):
        data = conn.recv(1024)
        print('New data:',addr)
        print(data.decode('utf-8'))
        if data == b'close':
            conn.close()
        else:
            self.answer(conn, data, addr)


    def answer(self, conn, data, addr):
        conn.send(data)
        print ('Echo data!',addr)
        conn.close()


if __name__ == '__main__':
    server = echo()
    server.serve()


