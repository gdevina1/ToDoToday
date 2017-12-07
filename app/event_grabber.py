import requests
import json
from message_reader import messageReader

TICKET_MASTER_URL = "https://app.ticketmaster.com/discovery/v2/events.json?"

class eventGrabber():

	def __init__(self, city, time):
		self.city = city
		self.time = time

	def get_event(self):
		r = requests.get(TICKET_MASTER_URL + "&city=" + self.city + "&startDateTime=" + self.time + "&apikey=5OY240GGemjfZrjV66o7OgePYReqJPcG")
		data = r.json()
		return(data["_embedded"]["events"][0]["url"])
