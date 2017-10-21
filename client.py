from threading import Thread
import threading
import socket
import time
import sys
#import psutil


def messWithCpu():
	print("Messing with Cpu")
	timeout = time.time() + 10
	x = 2
        while True:
                x *= x
		if time.time() > timeout:
			break
	threading.Timer(10, messWithCpu).start()


def client():
	print("read from cpu usage")
	messWithCpu()
#	for i in range(0,5):
#		print(psutil.cpu_percent(interval=10))

if __name__ == "__main__":
	client()
