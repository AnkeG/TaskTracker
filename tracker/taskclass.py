class Tasks:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.span = 0


def initTasks(names, colors):
	if len(names) != len(colors):
		return None

	tasks = list();
	for name, color in zip(names, colors):
		task = Tasks(name, color)
		tasks.append(task)

	return tasks

if __name__ == '__main__':
	tasks = ['work', 'study', 'relax', 'reading', 'custom1', 'custom2']
	piecolors = ['red', 'blue', 'green', 'yellow', 'brown', 'purple']

	taskslist = initTasks(tasks, piecolors)

	print(taskslist[0].name, taskslist[0].color)