import time
import tkinter as tk
import loghandler
import taskclass

fname = 'logs.csv'

totalspan = 0
startstamp = 0
runtask = None
tasknames = ['work', 'study', 'relax', 'reading', 'custom1', 'custom2']
taskcolors = ['red', 'blue', 'green', 'yellow', 'brown', 'purple']

def updatewatch():
	now = time.time()
	delta = now-startstamp
	string = time.strftime("%H:%M:%S",time.gmtime(delta))
	watch['text'] = string
	if runtask:
		watch.after(1000, updatewatch)

def start(t):
	global startstamp, runtask

	startstamp = time.time()
	starttime = time.strftime("%m/%d/%y %H:%M", time.localtime(startstamp))
	runtask = t

	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, t+': '+starttime+' ~ ')
	tasklogs['state'] = 'disable'

	for t in tasks:
		t.btn['state'] = "disable"
	stop_btn['state'] = "normal"
	save_btn['state'] = 'disable'

	updatewatch()

def stop():
	global startstamp, runtask, totalspan

	temptask = runtask
	runtask = None

	tstamp = time.time()
	endtime = time.strftime("%m/%d/%y %H:%M", time.localtime(tstamp))
	tspan = tstamp-startstamp
	span = time.strftime("%H:%M", time.gmtime(tspan))
	totalspan += tspan

	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, endtime+'  '+span+'\n')
	tasklogs['state']="disable"

	for t in tasks:
		if t.name == temptask:
			t.span = tspan
		t.btn['state'] = "normal"
		stop_btn['state'] = "disable"
		save_btn['state'] = 'normal'

	updatepie()

def save():
	text = tasklogs.get('2.0', tk.END)
	loghandler.savelogs(fname, text)
	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, 'log saved at ''logs.csv''\n')
	tasklogs['state']="disable"

def updatepie():
	lastend = 0
	for task in tasks:
		extent = task.span/totalspan*359.99
		pie.itemconfig(task.pieslice, start = lastend, extent = extent)
		lastend += extent

if __name__ == '__main__':
	loghandler.initlogs(fname)
	tasks = taskclass.initTasks(tasknames, taskcolors)

	window = tk.Tk()
	window.title("Task Tracker")

	window.minsize(width = 450, height = 630)

	watch =  tk.Label(window, text = "00:00:00", font="TimeNew 40 bold")

	btn_frame = tk.Frame(window)
	for i,t in enumerate(tasks):
		t.btn = tk.Button(btn_frame, text = t.name, 
			command = lambda t=t: start(t.name), bg = t.color)
		t.btn.grid(row = i//3, column = i%3, padx = 10)
	stop_btn = tk.Button(btn_frame, text = "stop", command = stop, state = "disable")
	stop_btn.grid(row = len(tasks)//6, column = 4, padx = 10)

	tasklogs = tk.Text(window, height = 15, width=50)
	tasklogs.insert(tk.END, "Tasks Logs\n")
	tasklogs['state'] = 'disable'
	save_btn = tk.Button(window, text = "save", command = save)

	pie = tk.Canvas(window, height = 230, width = 260)
	coord = 10, 20, 250, 210
	oval = pie.create_oval(coord)
	for t in tasks:
		t.pieslice = pie.create_arc(coord, start = 0, extent = 0, 
			fill = t.color, outline = t.color)

	watch.pack()
	btn_frame.pack()
	tasklogs.pack(expand = True, fill = tk.BOTH, pady = 10)
	save_btn.pack(side = tk.LEFT, padx = 15, pady = 10)
	pie.pack()

	window.mainloop()