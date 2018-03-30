import socket
import sys

if __name__ == '__main__':
	PORT = 8888
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
	    s.bind(("", PORT))
	except socket.error as msg:
	    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	    sys.exit()

	s.listen(10)
	while 1:
	    conn, addr = s.accept()
	    print('Connected with ' + addr[0] + ':' + str(addr[1]))

	s.close()