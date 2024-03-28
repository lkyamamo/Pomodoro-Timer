import tkinter as tk
import time

paused = False
minute = 25
second = 0

def start_time():
    global paused
    paused = False
    countdown()

def pause_time():
    global paused 
    paused = True

def skip_session():
    print("skipped")

def countdown():
    global paused, minute, second
    
    if (second > 0 or minute > 0) and not paused:
        current_time = f"{minute:02d}:{second:02d}"
        clock.config(text=current_time)
        
        if second > 0:
            second -= 1
        else:
            minute -= 1
            second = 59

        clock.after(1000, countdown)
    else:
        paused = True
        

root = tk.Tk()
root.title("Digital Clock")

clock = tk.Label(root, font=('Helvetica', 48))
clock.grid(row=0, column=1)

# start button
start = tk.Button(root, text="Start", command=start_time)
start.grid(row=1, column=0)

# pause button
pause = tk.Button(root, text="Pause", command=pause_time)
pause.grid(row=1, column=1)

# skip button
skip = tk.Button(root, text="Skip", command=skip_session)
skip.grid(row=1, column= 2)

current_time = f"{minute:02d}:{second:02d}"
clock.config(text=current_time)

root.mainloop()



print("after main")
