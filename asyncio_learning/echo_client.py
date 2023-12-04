import socket as sc
import time

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.connect(("localhost", 25000))

while True:
    # start = time.time()
    sock.send(b"Hello from client")
    resp = sock.recv(1000)
    # end = time.time()
    # print(end - start)
    print(b"got: " + resp)
    time.sleep(1)

