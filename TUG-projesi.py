import time
import urllib.request
url1="http://msrv3.tug.tubitak.gov.tr/tug_allsky_full.jpg"
say = 0
while True:
	say += 1
	urllib.request.urlretrieve(url1,"Resim"+str(say)+".jpg")
	print("Hazır Resim",say)
	time.sleep(300) #5 dk arayla çalışacak 
