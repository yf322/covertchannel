import psutil
import threading
import time
import socket
import sys

def server():
	for i in range(0, 5):
		print(psutil.cpu_percent(interval=10))
	
if __name__ == "__main__":
	server()

