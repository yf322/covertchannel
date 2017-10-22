import psutil
import threading
import multiprocessing
import time
import socket
import sys
import urllib2
import sched
import libtorrent as lt

class NetworkJam:

	def __init__(self):
		self.threads = []
		self.s = sched.scheduler(time.time, time.sleep)

	def http(self):
		#print "start downloading 100mb"
		url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
		request = urllib2.Request(url, headers={'User-Agent': "Magic Brw"})
		response = urllib2.urlopen(request)
		html = response.read()
		self.s.enter(20, 1, sys.exit, ())
		self.s.run()
		

	def p2p(self):
		ses = lt.session()
		ses.listen_on(6881, 6891)

		e = lt.bdecode(open("test.torrent", 'rb').read())
		info = lt.torrent_info(e)

		params = { 'save_path': '.', 'storage_mode': lt.storage_mode_t.storage_mode_sparse, 'ti': info }
		h = ses.add_torrent(params)

		s = h.status()
		while (not s.is_seeding):
	        	s = h.status()
			state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
        		print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state])
        	time.sleep(1)

	def shutdown(self):
		print("shut down")
		for t in self.threads:
			t.terminate()
			t.join()
		



if __name__ == "__main__":
	nj = NetworkJam()
	n = 50
	print 'downloading 100mb for', n, 'times'
	for i in range(1, n):
		t = multiprocessing.Process(target=nj.http)
		nj.threads.append(t)
		t.start()
	
	time.sleep(10)
	nj.shutdown()

