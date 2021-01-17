import time
from datetime import datetime
import tkinter as tk

startstamp = 0
run = False

def updatewatch():
	now = time.time()
	delta = now-startstamp
	string = time.strftime("%H:%M:%S",time.gmtime(delta))
	watch['text'] = str(string)
	if run:
		watch.after(1000, updatewatch)

def start():
	global startstamp, run
	tstamp = time.time()
	startstamp = tstamp
	run = True
	updatewatch()

def stop():
	global startstamp, run
	tstamp = time.time()
	startstamp = tstamp
	run = False

window = tk.Tk()
window.title("Task Tacker")

window.minsize(width = 300, height = 300)

watch =  tk.Label(window, text = "00:00:00", font="TimeNew 30 bold")
btn_frame = tk.Frame(window)
start_btn = tk.Button(btn_frame, text = "start", command = start)
stop_btn = tk.Button(btn_frame, text = "stop", command = stop)

start_btn.grid(row = 0, column = 0, padx = 10)
stop_btn.grid(row = 0, column = 1, padx = 10)

watch.pack()
btn_frame.pack()

window.mainloop()