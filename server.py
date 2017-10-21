import psutil
import threading
import time
import socket
import sys
import urllib2
import libtorrent as lt

def http():
	print "start downloading 100mb"
	url = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
	request = urllib2.Request(url, headers={'User-Agent': "Magic Brw"})
	response = urllib2.urlopen(request)
	html = response.read()

def p2p():
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


threads = []	
for i in range(1, 10):
	t = threading.Thread(target=http)
	threads.append(t)
	t.start()


