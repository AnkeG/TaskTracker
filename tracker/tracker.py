import timer
import tkinter as tk

window = tk.Tk()
window.title("Task Tacker")

window.minsize(width = 300, height = 300)

watch =  tk.Label(window, text = "00:00:00", font="TimeNew 30 bold")
watch.pack()

window.mainloop()