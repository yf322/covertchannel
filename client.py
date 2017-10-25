from timeout import timeout
import time
import sys
import urllib2
import timeit
import pyspeedtest


class Detecter:

    def __init__(self, timeout):
        self.calibrate_n = 5
        self.read = ''
        self.timeout = timeout

    def downloadSpeed(self):
        url = 'http://speedtest.ftp.otenet.gr/files/test1Mb.db'
        request = urllib2.Request(url, headers={'User-Agent': "Magic Brw"})
        response = urllib2.urlopen(request)
        start = time.time()
        try:
            with timeout(seconds=self.timeout - 2):
                response.read()
                end = time.time()
        except:
            end = start + 8
        t = float(end - start)
        return 1024/t, t

    def calibrate(self):
        print("Testing the network speed for calibrate")
        result = 0
        for i in range(0, self.calibrate_n):
            start = time.time()
            _, runtime = self.downloadSpeed()
            result += runtime
            end = time.time()
            print "Calibrating #", i, "runtime", end - start
        return result/float(self.calibrate_n)

    def client(self):
        print "Read the network status"
        avg = self.calibrate()
        print "The average download speed is:", avg, "kb/s"
        while True:
            _, runtime = self.downloadSpeed()
            start = time.time()
            if (runtime - avg)/avg > 0.15:
                self.read += '1'
            else:
                self.read += '0'
            print self.read
            end = time.time()
            print "Runtime for this round:", runtime + end - start
            time.sleep(self.timeout - (runtime + end - start))


if __name__ == "__main__":
    f = open('inputStr', 'r')
    input_str = f.readline()
    detecter = Detecter(10)
    detecter.client()

