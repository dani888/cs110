# reminder.py
# Bill Campbell 
# Homework 6: A Reminder App based on Objects
# By Daniel Werminghausen
# 11/28/2016

from clock import Clock
from calendar import Calendar
import time 
import copy
import ast

class Event:
	def __init__(self, date, time, description):
		"""
		pass in date, time, description into the
		constructor in the Event class
		
		Args:
		    date (str): initializing the instance variable 
		    which is part of class Event
		    time (str): initializing the instance variable
		    which is part of class Event
		    description (str): initializing the instance variable
		    which is part of class Event
		"""
		self.date = date
		self.time = time
		self.description = description

	def allStringInDescription(self,strList):
		"""
		checks if there is a string 
		and returns it as description
		Args:
		    strList (str): Description of event
		
		Returns:
		    str: description of event
		"""
		for string in strList:
			if string not in self.description:
				return False
		return True

	def __str__(self):
			"""
			defines string for class Event 
			
			Returns:
			    str: a combination of strings for date,time,and description
			    seperated by a ","
			"""
			return self.date + ", " + self.time + ", " + self.description	


class Reminder(Clock, Calendar):
	def __init__(self):
		"""
		passes in self for all varaibles into Reminder class
		initializing all the instance variable
		"""
		t = time.localtime()[:6]   # t = (year, month, day, hour, min, sec)
		Clock.__init__(self, t[3], t[4], t[5])
		Calendar.__init__(self, t[1], t[2], t[0])
		self.events = []
		self.interact()
		

	def __str__(self):
		"""
		defines string for class Reminder
		"""
		return Calendar.__str__(self) + " " + Clock.__str__(self)

	def save(self,file):
		"""
		saves events into a file
		
		Args:
		    file (str): name the file 
		
		Returns:
		    str: saves file into the  txt file
		"""
		open(file, 'w').close();
		with open(file, 'a') as the_file:
			for event in self.events:
				the_file.write(str(event) + '\n')
			the_file.close()

	def load(self, file):
		"""
		load file
		
		Args:
		    file (str): name of the file
		
		Returns:
		    str: loads in the saved file 
		"""
		with open(file) as f:
			lines = f.readlines()
			for event in lines:
				if self.validDateTime(event):
					values = event.split(',')
					self.events.append(Event(values[0],values[1],values[2].rstrip()))

	def validDateTime(self,event):
		"""
		checks if the date and time is before its own date and time
		
		Args:
		    event (str): the event you have scheduled
		
		"""
		values = event.split(',')
		date = values[0].replace(" ","").split('/')
		time = values[1].replace(" ","").split(':')
		if self.isValidEventDate(date[1],date[0],date[2],time[0],time[1],0):
			return True
		return False

	def isValidEventDate(self,day,month,year,hours,minutes,seconds):
		"""
		checks if the event date is valid
		
		Args:
		    day (str): what was passed in for event scheduled
		    month (str): what was passed in for event scheduled
		    year (str): what was passed in for event scheduled
		    hours (str): what was passed in for event scheduled
		    minutes (str): what was passed in for event scheduled
		    seconds (str): what was passed in for event scheduled
		
		Returns:
		    str: return True or false
		"""
		day = int(day)
		month = int(month)
		year = int(year)
		hours = int(hours)
		minutes = int(minutes)
		seconds = int(seconds)

		if year < self.year() or month > 12 or month < 1 or  day > self.months[month-1] or day < 1:
			# print("Fail year")
			return False
		if year > self.year():
			return True
		# year == self.year
		if month < self.month():
			# print("Fail month")
			return False
		if month > self.month():
			return True
		# month == self.month
		if day < self.day():
			# print("Fail day")
			return False
		if day > self.day():
			return True
		return self.isValidEventTime(hours,minutes,seconds)

	def isValidEventTime(self, hours, minutes, seconds):
		"""
		checks if the event time is valid
		
		Args:
		    hours (str): what was passed in for event scheduled
		    minutes (str): what was passed in for event scheduled
		    seconds (str): what was passed in for event scheduled
		
		Returns:
		    str: True or False
		"""
		if hours > 23 or hours < 0 or minutes > 59 or minutes < 0 or seconds > 59 or seconds < 0:
			return False
		if hours > self.hours():
			return True
		if hours < self.hours():
			return False
		if minutes > self.minutes():
			return True
		if minutes < self.minutes():
			return False	
		if seconds < self.seconds():
			return False
		return True 

	def announceEvents(self):
		"""
		announces Events that have expired and removes event
	
		"""
		eventsCopy = self.events[:]
		for event in eventsCopy:
			if not self.validDateTime(str(event)):
				print("Event " + str(event) + " has expired")
				self.events.remove(event);

	def interact(self):
		"""
		Interact with a user to schedule events that the user
		might like to be reminded of by putting in commands 
		such as,
		Reminder Commands:
	 q       [for quit]
	 ?       [ask for help]
	 t       [print 'current' time]
	 e       [schedule event]
	 s       [search for event with all strings]
	 x       [delete found event]
	 p       [print scheduled events]
	 m       [advance time  minutes, one if no ]
	 h       [advance time  hours, one if no ]
	 d       [advance time  days, one if no ]
	 w       [write scheduled events to the named file.]
	 r       [read and schedule events from the named file.]

		"""
		try:
			self.load("init.txt")
		except: 
			print("No init.txt file found to load")
		while True:
			line = raw_input("Enter Command (? for help): ")
			try:
				command = line[0]
				if command == 'q':
					self.save("init.txt")
					break;
				if command == 't':
					# [print 'current' time]
					print(str(self))
				elif command == 'e':
					# [schedule event]
					try:
						values = line[1:].split(',')
						date = values[0].split("/")
						if len(date) == 2:
							date = date + ["2016"]
						date = '/'.join(date)
						if not self.validDateTime(date + ", " + values[1] + ", " + values[2]):
							print("Event is past due and can't be scheduled anymore")
						else: 
							self.events.append(Event(date,values[1],values[2]))
					except:
						print("Invalid e command. Failed to load the Event.")
				elif command == 's':
					# [search for event with all strings]
					try:
						strList = ast.literal_eval(line[1:].replace(" ",""))
						self.lastSearchedEvents = []
						for event in self.events:
							if(event.allStringInDescription(strList)):
								print(event)
								self.lastSearchedEvents.append(event)
					except:
						print("Search Failed. Please try to search again.")
				elif command == 'x':
					# [delete found event]
					try:
						for event in self.lastSearchedEvents:
							self.events.remove(event)
					except:
						print("Failed to delete searched events.")
				elif command == 'p':
					# [print scheduled events]
					for event in self.events:
						print(event)
				elif command == 'm':
					# [advance time  minutes, one if no ]
					try:
						if not line[1:].replace(" ",""):
							addMins = 1
						else:
							addMins = int(line[1:].replace(" ",""))
						if addMins:
							mins = self.minutes() + addMins
							hrs = self.hours()
							if mins > 59:
								hrs = hrs + int(mins/60)
								mins = mins % 60
							if hrs > 23:
								hrs = hrs % 24
							self.set_Clock(hrs, mins, self.seconds())
						self.announceEvents()
					except:
						print("invalid m command could not increment minutes")
				elif command == 'h':
					# [advance time  hours, one if no ]
					try:
						if not line[1:].replace(" ",""):
							addHrs = 1
						else:
							addHrs = int(line[1:].replace(" ",""))
						if addHrs:
							hrss = self.hours() + addHrs
						# else:
						# 	addHrs == 1
							if hrss > 23:
								hrss = hrss % 24
							self.set_Clock(hrss, self.minutes(), self.seconds())
						self.announceEvents()
					except:
						print("invalid h command could not increment hours")
				elif command == 'd':
					# [advance time  days, one if no ]
					try:
						if not line[1:].replace(" ",""):
							addDay = 1
						else:
							addDay = int(line[1:].replace(" ",""))
						if addDay:
							addDays = self.day() + addDay
						# else:
						# 	addDays == 1
		    				self.set(addDays, self.month(), self.year())
						self.announceEvents()
					except:
						print("invalid d command could not increment days")
				elif command == 'w':
					# [write scheduled events to the named file.]
					try:
						file = line[1:]
						self.save(file)
						print("File has been udated")
					except:
						print("Invalid w command could not save file")
				elif command == 'r':
					# [read and schedule events from the named file.]
					try:
						file = line[1:]
						self.load(file)
					except:
						print("Invalid r commoand could not load from file")
				elif command == '?':
					print(""" 
	Reminder Commands:
	 q       [for quit]
	 ?       [ask for help]
	 t       [print 'current' time]
	 e       [schedule event]
	 s       [search for event with all strings]
	 x       [delete found event]
	 p       [print scheduled events]
	 m       [advance time  minutes, one if no ]
	 h       [advance time  hours, one if no ]
	 d       [advance time  days, one if no ]
	 w       [write scheduled events to the named file.]
	 r       [read and schedule events from the named file.]
					""")
				else:
					print("Not a valid command")
			except:
				print("please provide a command!")
		print "Reminder app shut down!\n"
	
	

r = Reminder()