import socket
import time
import sys
ip, port = "127.0.0.1", 80
Finish = False
while (True):
 try:
  a = ["print('connecting...')", "client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)", "client.connect((ip, port))",
"print('sending data...')" , "client.send(b'yeahhh')", "print(client.recv(1024))", "client.close()"]

  for i in a:
   exec(i)
 except KeyboardInterrupt as e:
  print(str(e), "KELUAR..")
 break

