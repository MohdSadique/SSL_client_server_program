# import modules
import os
import socket
import ssl
import sys

BUFFER_SIZE = 1024  # for file transfer send 1024 bytes each time step
# getting domain name and port from argv
domain = str(sys.argv[1])
port = int(sys.argv[2])


def client_program():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('cert.pem')

    client_socket = socket.socket()  # instantiate
    c_soc = context.wrap_socket(client_socket, server_hostname=domain)
    c_soc.connect((domain, port))  # connect to the server

    # message and authentication initialization
    message = ""
    auth = False

    while message.lower().strip() != 'exit':
        if auth is False:
            user_id = input("User ID:")
            password = input("Password:")
            message = user_id + " " + password
            c_soc.send(message.encode())  # send message
            data = c_soc.recv(1024).decode()  # receive response
            print(data)  # show in terminal

            if data == "correct ID and password":
                auth = True

        else:
            message = input("\nsftp>")  # again take input

            if message == "lls":
                dir_list = os.listdir(os.getcwd())
                print(*dir_list, sep='\n')

            elif message == "exit":
                pass

            elif "put" in message:
                filename = message[4:]
                # start sending the file
                c_soc.send(f"{filename}".encode())

                # Read File in binary
                file = open(filename, 'rb')
                line = file.read(1024)
                # Keep sending data to the client
                while line:
                    c_soc.send(line)
                    line = file.read(1024)

                file.close()
                c_soc.send(b'end')
                data = c_soc.recv(1024).decode()  # receive response
                print(data)

            else:
                print("Invalid Command")

    c_soc.close()  # close the connection


if __name__ == '__main__':
    client_program()
