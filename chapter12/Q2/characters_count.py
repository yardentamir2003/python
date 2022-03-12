import socket

URL = input("Enter URL: ")
splitted_URL = URL.split("/")
host_name = splitted_URL[2]
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect((host_name, 80))
except:
    print("Non-existent URL.")


cmd = ("GET {} HTTP/1.0\r\n\r\n".format(URL)).encode()
mysocket.send(cmd)

enter_here = True
characters_count = 0
while True:
    limit = 999
    data = mysocket.recv(100)
    if len(data) == 0:
        break
    characters_count += len(data)
    if characters_count < 999:
        print(data.decode(), end='')
    else:
        if enter_here:
            dont_print = characters_count - limit
            print(data[:-dont_print].decode(), end='')
            enter_here = False
print("\ncharacters count = ", characters_count)
mysocket.close()




