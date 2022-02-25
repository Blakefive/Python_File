import time

while(1):
    now = time.localtime()
    print(now.tm_year,' : ',now.tm_mon,' : ',now.tm_mday,' : ',now.tm_hour,' : ',now.tm_min,' : ',now.tm_sec)
    time.sleep(1)
