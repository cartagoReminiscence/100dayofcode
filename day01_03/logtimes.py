from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
	loglines = f.readlines()
	loglines = [l for l in loglines if l.find(SHUTDOWN_EVENT) != -1]

def convert_to_datetime(line):
	#extract timestamp
	first_white_space = line.find(" ")
	second_white_space = line.find(" ", first_white_space + 1)
	line = line[first_white_space + 1:second_white_space]

	#convert to datetime object
	return datetime.fromisoformat(line)

def time_between_shutdowns(loglines):
	return loglines[-1] - loglines[0]

loglines = [convert_to_datetime(l) for l in loglines]
