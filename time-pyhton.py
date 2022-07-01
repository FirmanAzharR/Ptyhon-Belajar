import time

ticks = time.time()
print(ticks)

localtime = time.localtime(time.time())
print ("Waktu lokal saat ini :", localtime)

localtimeFormat = time.asctime(time.localtime(time.time()) )
print(localtimeFormat)