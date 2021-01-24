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
		watch.after(300, updatewatch)

def start(t):
	global startstamp, runtask

	startstamp = time.time()
	starttime = time.strftime("%m/%d/%y %H:%M", time.localtime(startstamp))
	runtask = t

	tasklogs.insert(tk.END, t+': '+starttime+' ~ ')

	for task in tasks:
		if task.name == runtask:
			task.btn['text'] = 'stop'
			task.btn['command'] = stop
		else:
			task.btn['state'] = "disable"
	report_btn['state'] = 'disable'

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

	tasklogs.insert(tk.END, endtime+'  '+span+'\n')

	for task in tasks:
		if task.name == temptask:
			task.span = tspan
			task.btn['text'] = task.name
			task.btn['command'] = command = lambda t=t: start(t.name)
		task.btn['state'] = "normal"
	report_btn['state'] = 'normal'

	updatepie()

def save():
	text = tasklogs.get('2.0', tk.END)
	loghandler.savelogs(fname, text)
	tasklogs['state'] = 'normal'
	tasklogs.insert(tk.END, 'log saved at ''logs.csv''\n')
	tasklogs['state']="disable"

def report():
	tasklogs['state']="disable"
	reportwindow.deiconify()

def close():
	reportwindow.withdraw()

def updatepie():
	lastend = 0
	for task in tasks:
		extent = task.span/totalspan*359.99
		pie.itemconfig(task.pieslice, start = lastend, extent = extent)
		lastend += extent

if __name__ == '__main__':
#initializing data log file and tasks
	loghandler.initlogs(fname)
	tasks = taskclass.initTasks(tasknames, taskcolors)

#main window
	window = tk.Tk()
	window.title("Task Tracker")

	window.minsize(width = 350, height = 120)

	watch =  tk.Label(window, text = "00:00:00", font="TimeNew 35 bold")

	btn_frame = tk.Frame(window)
	for i,t in enumerate(tasks):
		t.btn = tk.Button(btn_frame, text = t.name, font = "TimeNew 11",
			width = 8, command = lambda t=t: start(t.name))
		t.btn.grid(row = i//3, column = i%3, padx = 10, pady = 5)

	report_btn = tk.Button(window, text = "Statistic Summary", command = report)

	btn_frame.pack()
	watch.pack(pady = 20)
	report_btn.pack()

#report window
	reportwindow = tk.Tk()
	reportwindow.title("Statistic Summary")

	reportwindow.minsize(width = 450, height = 300)

	reportbtns = tk.Frame(reportwindow)
	save_btn = tk.Button(reportbtns, text = 'save', width = 5, command = save)
	save_btn.grid(row = 0, column = 0, padx = 5)

	close_btn = tk.Button(reportbtns, text = 'close', command = close)
	close_btn.grid(row = 0, column = 1, padx = 5)

	tasklogs = tk.Text(reportwindow, height = 15, width=50)
	tasklogs.insert(tk.END, "Tasks Logs\n")

	pie = tk.Canvas(reportwindow, height = 230, width = 260)
	coord = 10, 20, 250, 210
	oval = pie.create_oval(coord)
	for t in tasks:
		t.pieslice = pie.create_arc(coord, start = 0, extent = 0, 
			fill = t.color, outline = t.color)

	reportbtns.pack(side = tk.RIGHT, pady = 10, fill=tk.BOTH)
	tasklogs.pack(expand = True, fill = tk.BOTH)
	pie.pack()

	reportwindow.withdraw()

	window.mainloop()