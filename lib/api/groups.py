#
#  group.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
from bs4 import *
import html5lib
import urllib.request

class Groups:

	def getShout(groupid):
		a = str(groupid)
		#ctl00_cphRoblox_GroupStatusPane_StatusTextField
		page = "https://www.roblox.com/My/Groups.aspx?gid="+a
		source = urllib.request.urlopen(page)
		_a = BeautifulSoup(source)
		_b = 
		#_h = html5lib.parse(source,"ctl00_cphRoblox_GroupStatusPane_StatusTextField")
		#_s = BeautifulSoup(source.read(), "html.parser")

		#q = _s.find("div", attrs={'id': 'ctl00_cphRoblox_GroupStatusPane_status'})
		#w = q.find("div", attrs={'id': "ctl00_cphRoblox_GroupStatusPane_StatusView", "class": "StatusView"})
		#e = w.find("div", attrs={'class': "top"})
		#r = e.find("span", attrs={"id": "ctl00_cphRoblox_GroupStatusPane_StatusTextField", "class": "StatusTextField linkify"})
		#post2 = _s.find("ctl00_cphRoblox_GroupStatusPane_StatusTextField", attrs={'class': 'StatusTextField linkify'})
		#post3 = _s.find("div", attrs={'class': 'top'})
		#post1 = post_1.text
		#post2 = post_2.text
		print("From Roblox : "+str())
		#print("From Roblox : "+str(post2))
		#print("From Roblox : "+str(post3))



"""
from bs4 import BeautifulSoup
import urllib.request

webpage = "http://www.masslottery.com/games/lottery/large-winningnumbers.html"

websource = urllib.request.urlopen(webpage)
soup = BeautifulSoup(websource.read(), "html.parser")

span = soup.find("span", {"id": "winning_num_0"})
print (span)

Output is here...
<span id="winning_num_0"></span> 
"""