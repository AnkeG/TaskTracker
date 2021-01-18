import time
from datetime import datetime
import tkinter as tk

startstamp = 0
run = False

def updatewatch():
	now = time.time()
	delta = now-startstamp
	string = time.strftime("%H:%M:%S",time.gmtime(delta))
	watch['text'] = string
	if run:
		watch.after(1000, updatewatch)

def start():
	global startstamp, run
	tstamp = time.time()
	startstamp = tstamp
	run = True
	start_btn['state'] = "disable"
	stop_btn['state'] = "normal"
	updatewatch()

def stop():
	global startstamp, run
	tstamp = time.time()
	endtime = time.strftime("%m/%d/%y %H:%M", time.localtime(tstamp))
	starttime = time.strftime("%m/%d/%y %H:%M", time.localtime(startstamp))
	print(endtime, starttime)
	tasklogs.insert(tk.END, starttime+' ~ '+endtime+'\n')
	startstamp = tstamp
	run = False
	start_btn['state'] = "normal"
	stop_btn['state'] = "disable"

window = tk.Tk()
window.title("Task Tacker")

window.minsize(width = 100, height = 130)

watch =  tk.Label(window, text = "00:00:00", font="TimeNew 30 bold")
tasklogs = tk.Text(window, height = 15, width=50)
tasklogs.insert(tk.END, "Tasks Logs\n")
btn_frame = tk.Frame(window)
start_btn = tk.Button(btn_frame, text = "start", command = start)
stop_btn = tk.Button(btn_frame, text = "stop", command = stop, state = "disable")

start_btn.grid(row = 0, column = 0, padx = 10)
stop_btn.grid(row = 0, column = 1, padx = 10)

watch.pack()
btn_frame.pack()
tasklogs.pack(pady = 10)

window.mainloop()