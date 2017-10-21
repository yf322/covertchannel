from threading import Thread
import threading
import time
import sys
#import psutil
import pyspeedtest

st = pyspeedtest.SpeedTest()

def messWithNetwork():
	print("messing with network speed")

def client():
	print("read the network status")
	messWithNetwork()
	for i in range(0,5):
		print(st.download())


client()
