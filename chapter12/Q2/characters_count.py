



while True:
    data = mysocket.recv(3000)
    if len(data) < 1:
        break
    print(data.decode(), end='')