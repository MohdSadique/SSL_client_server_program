# SSL_client_server_program
This is SSL implementation for communication of client and server

> How to build the program:
>>	1)generate public key certificate in server directory
>>>  if using OpenSSL:
>>>
>>>		1. openssl genrsa -aes256 -out private.key 2048
>>>
>>>		2. openssl rsa -in private.key -out private.key
>>>
>>>		3. openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500
>>>
>>>		4. openssl req -x509 -new -nodes -key private.key -sha1 -days 36500 -out new.pem

2)copy cert.pem in cleint directory
> How to execute the program:
>>
>>		1. server : python ./sslserver.py
>
>>		2. client : python ./sslclient.py
>>	
>>	3)for put command give relative path of file from rootfolder of client

------------------------------------------------

the client prints “sftp >”, which allows the user to execute the put, lls, and exit commands.

sftp > put <filename> // transfer a text file <filename> from the client to the server.

 sftp > lls // list files and sub-directories of the directory on the client side

  sftp > exit // terminates the sftp session (to make it easier for the TA to grade the assignment, please 
terminate both the client and the server in this assignment)

  If a user enters a command other than the above three commands, then the client prints “Invalid 
Command” and “sftp >”, prompting the user to enter a different command.
