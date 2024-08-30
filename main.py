
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)  # to cancel the timer that we set up previously
    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label "Timer"
    label_timer.configure(text="Timer", fg=GREEN)
    # reset check marks
    tick.configure(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        print("break")
        countdown(long_break_sec)
        label_timer.configure(text="Break", fg=RED)

    if reps % 2 == 0:
        print("break")
        label_timer.configure(text="Break", fg=PINK)
        countdown(short_break_sec)

    else:
        print("work time")
        label_timer.configure(text="Timer", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(work_seconds):
    count_minutes = work_seconds//60
    count_seconds = work_seconds % 60

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if work_seconds > 0:
        global timer
        timer = window.after(1000,  countdown, work_seconds-1)

    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        tick.configure(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",
                                fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Timer
label_timer = Label(text="Timer", font=(
    "papyrus", 42, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# reset
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# tick marks
tick = Label(text="", fg=GREEN, bg=YELLOW, font=("", 16, ""))
tick.grid(row=2, column=1)

window.mainloop()
