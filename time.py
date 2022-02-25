import time
 
now = time.localtime()
print("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))


