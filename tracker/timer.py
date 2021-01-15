import time

def convert(secs):
	mins = secs//60
	secs = secs%60
	hours = mins//60
	mins = mins%60

	return hours, mins, secs