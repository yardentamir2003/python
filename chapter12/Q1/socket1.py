import socket

URL = input("Enter URL: ")
splitted_URL = URL.split("/")
host_name = splitted_URL[2]
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect((host_name, 80))
except:
    print("Non-existent URL.")


cmd = ("GET #{} HTTP/1.0\r\n\r\n".format(URL)).encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysocket.close()




