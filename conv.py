try:
	import requests
except:
	print ("No Module Named Requests")
	quit()
import os
import json
import re
import urllib
import sys

C  = '\033[36m' # cyan\
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue

print (""+O+"")
def banner():
	print ("""
		>     GHOSTBLACK     <

╔═╗╔═╗╔═╗╦╔═╦  ╦╔═╗╦═╗╔╦╗╔═╗╦═╗  ╔╦╗╦ ╦╔═╗╦╔═╗ Cod3d By : Zekkel Hax0r
╔═╝║╣ ║  ╠╩╗╚╗╔╝║╣ ╠╦╝ ║ ║╣ ╠╦╝  ║║║║ ║╚═╗║║  
╚═╝╚═╝╚═╝╩ ╩ ╚╝ ╚═╝╩╚═ ╩ ╚═╝╩╚═  ╩ ╩╚═╝╚═╝╩╚═╝

Thanks To : Aalex, Faisal, Ago Oeng, Dani, Sulton, Jainudin, Magribisya
   """)

class a:
	def __init__(self):
		self.apa = input(""+C+"Link YouTube => ")
	def zek(self):
		try:
			gpp = ('https://www.convertmp3.io/fetch/?video={}'.format (self.apa))
			nama = input("Nama File => ")
			r = requests.get(gpp, stream=True)
			if r.status_code == 200:
				print ("[*] Downloading..../ ")
				with open(nama + '.mp3','wb') as f:
					for i in r.iter_content(1024):
						if i:
							f.write(i)
							f.flush
			else :
				print ("Error")
				quit()


			print ("[*] done, Saved %s" % nama + '.mp3')

		except KeyboardInterrupt:
			print ("CTRL + C")



if __name__ == "__main__":
	os.system("clear")
	banner()
	zek = a()
	zek.zek()