import time
from datetime import datetime
import tkinter as tk

task = ''
startstamp = 0
run = False
btn_dict = dict()
tasks = ['work', 'study', 'relax', 'reading', 'custom1', 'custom2']

def updatewatch():
	now = time.time()
	delta = now-startstamp
	string = time.strftime("%H:%M:%S",time.gmtime(delta))
	watch['text'] = string
	if run:
		watch.after(1000, updatewatch)

def start(t):
	global startstamp, run, task
	startstamp = time.time()
	run = True
	task = t
	for t in tasks:
		btn_dict[t]['state'] = "disable"
	stop_btn['state'] = "normal"
	updatewatch()

def stop():
	global startstamp, run, task
	tstamp = time.time()
	endtime = time.strftime("%m/%d/%y %H:%M", time.localtime(tstamp))
	starttime = time.strftime("%m/%d/%y %H:%M", time.localtime(startstamp))
	tasklogs.insert(tk.END, task+': '+starttime+' ~ '+endtime+'\n')
	startstamp = tstamp
	run = False
	for t in tasks:
		btn_dict[t]['state'] = "normal"
	stop_btn['state'] = "disable"

window = tk.Tk()
window.title("Task Tacker")

window.minsize(width = 100, height = 130)

watch =  tk.Label(window, text = "00:00:00", font="TimeNew 30 bold")
tasklogs = tk.Text(window, height = 15, width=50)
tasklogs.insert(tk.END, "Tasks Logs\n")
btn_frame = tk.Frame(window)

for i,t in enumerate(tasks):
	btn_dict[t] = tk.Button(btn_frame, text = t, command = lambda t=t: start(t))
	btn_dict[t].grid(row = i//3, column = i%3, padx = 10)

stop_btn = tk.Button(btn_frame, text = "stop", command = stop, state = "disable")
stop_btn.grid(row = len(tasks)//6, column = 4, padx = 10)

watch.pack()
btn_frame.pack()
tasklogs.pack(pady = 10)

window.mainloop()