import re
from datetime import datetime

class messageReader:

	def __init__(self, msg):
		self.msg = msg

	def get_location(self):
		keywords = [" in ", " around ", " near "]
		for kw in keywords:
			if kw in self.msg:
				return self.msg[self.msg.find(kw)+len(kw):len(self.msg)]

	def get_time(self):
		p = re.compile('[0-2]?[0-9]:[0-9][0-9][AP]M')
		if (p.search(self.msg)):
			current = datetime.now()
			requestdate = datetime.strptime(str(current.year) + " " + str(current.month) + " " + str(current.day) + " " + p.findall(self.msg)[0], '%Y %m %d %I:%M%p')
			return str(requestdate.year) + "-" + ("0" if requestdate.month<10 else "") + str(requestdate.month) + "-" + ("0" if requestdate.day<10 else "") + str(requestdate.day) + "T" + ("0" if requestdate.hour<10 else "") + str(requestdate.hour) + ":" + ("0" if requestdate.minute<10 else "") + str(requestdate.minute) + ":" + ("0" if requestdate.second<10 else "") + str(requestdate.second) + "Z"
