import time
import tkinter as tk
import loghandler

fname = 'logs.csv'

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
	global startstamp, run

	startstamp = time.time()
	starttime = time.strftime("%m/%d/%y %H:%M", time.localtime(startstamp))
	run = True

	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, t+': '+starttime+' ~ ')
	tasklogs['state'] = 'disable'

	for t in tasks:
		btn_dict[t]['state'] = "disable"
	stop_btn['state'] = "normal"
	save_btn['state'] = 'disable'

	updatewatch()

def stop():
	global startstamp, run

	run = False

	tstamp = time.time()
	endtime = time.strftime("%m/%d/%y %H:%M", time.localtime(tstamp))
	span = time.strftime("%H:%M", time.gmtime(tstamp-startstamp))

	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, endtime+'  '+span+'\n')
	tasklogs['state']="disable"
	
	for t in tasks:
		btn_dict[t]['state'] = "normal"
	stop_btn['state'] = "disable"
	save_btn['state'] = 'normal'

def save():
	text = tasklogs.get('2.0', tk.END)
	loghandler.savelogs(fname, text)
	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, 'log saved at ''logs.csv''\n')
	tasklogs['state']="disable"

if __name__ == '__main__':
	loghandler.initlogs(fname)

	window = tk.Tk()
	window.title("Task Tracker")

	window.minsize(width = 450, height = 430)

	watch =  tk.Label(window, text = "00:00:00", font="TimeNew 40 bold")

	btn_frame = tk.Frame(window)

	for i,t in enumerate(tasks):
		btn_dict[t] = tk.Button(btn_frame, text = t, command = lambda t=t: start(t))
		btn_dict[t].grid(row = i//3, column = i%3, padx = 10)
	stop_btn = tk.Button(btn_frame, text = "stop", command = stop, state = "disable")
	stop_btn.grid(row = len(tasks)//6, column = 4, padx = 10)

	tasklogs = tk.Text(window, height = 15, width=50)
	tasklogs.insert(tk.END, "Tasks Logs\n")
	tasklogs['state'] = 'disable'
	save_btn = tk.Button(window, text = "save", command = save)

	watch.pack()
	btn_frame.pack()
	tasklogs.pack(expand = True, fill = tk.BOTH, pady = 10)
	save_btn.pack(side = tk.LEFT, padx = 15, pady = 10)

	window.mainloop()