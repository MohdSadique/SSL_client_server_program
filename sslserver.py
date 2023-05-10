import socket
import ssl
import os

BUFFER_SIZE = 1024


def server_program():
    # get the hostname
    host = 'localhost'  # socket.gethostname()
    port = 5000  # initiate port no above 1024

    # getting context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'private.key')

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure the server for 1 client
    server_socket.listen(1)
    s_soc = context.wrap_socket(server_socket, server_side=True)

    conn, address = s_soc.accept()  # accept new connection
    print("Connection from: " + str(address))

    # set authentication to false
    auth = False

    # receive data stream. it won't accept data packet greater than 1024 bytes

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("\n\n-----closing server---------\n\n")
            break

        if auth is False:
            passwords = open('password', 'r')
            for credentials in passwords:
                if data in credentials:
                    auth = True
                    conn.send(f'correct ID and password'.encode())
                    print(f'authentication passed for {data}')
            passwords.close()
            # data = conn.recv(1024).decode()
            if not auth:
                conn.send(f'incorrect ID and password'.encode())
                print(f'authentication failed for {data}')
        else:
            # PUT operation
            filename = data
            # remove absolute path if there is
            filename = os.path.basename(filename)
            # filename = filename + '_copy.txt'

            # start receiving and writing the file
            # Write File in binary
            file = open(filename, 'wb')

            # Keep receiving data from the server
            line = conn.recv(1024)
            while line != b'end':
                file.write(line)
                line = conn.recv(1024)

            file.close()
            print(f'{filename} copied')
            conn.send(f'file copied'.encode())

    s_soc.close()  # close the connection


if __name__ == '__main__':
    server_program()
