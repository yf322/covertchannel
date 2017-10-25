import multiprocessing
import time
import sys
import urllib2
import sched
import timeit

class NetworkJam:
	def __init__(self, timeout):
		self.threads = []
		self.s = sched.scheduler(time.time, time.sleep)
		self.timeout = timeout

	def http(self):
		#print "start downloading 100mb"
		url = 'http://ipv4.download.thinkbroadband.com/512MB.zip'
		request = urllib2.Request(url, headers={'User-Agent': "Magic Brw"})
		response = urllib2.urlopen(request)
		response.read()

	def shutdown(self):
		print("shut down")
		for t in self.threads:
			t.terminate()
			t.join()

	def sendBits(self, string):
		n = 50
		for s in string:
			if s == '0':
				print "sending 0"
				time.sleep(self.timeout)
			else:
				start = timeit.default_timer()
				print "sending 1"
				for i in range(1, n):
					t = multiprocessing.Process(target=nj.http)
					nj.threads.append(t)
					t.start()
				end = timeit.default_timer()
				time.sleep(self.timeout - (end -start))
				self.shutdown()

if __name__ == "__main__":
	try:
		f = open('inputStr', 'r')
		input_str = f.readline()
		print input_str
		nj = NetworkJam(10)
		nj.sendBits(input_str)

	except KeyboardInterrupt:
		sys.exit(1)

