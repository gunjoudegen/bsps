from tkinter import *

class ShotClockTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shot Clock Timer")

        self.time_left = 24
        self.is_running = False

        self.label = Label(root, font=("Arial", 50), text=self.time_left)
        self.label.pack(pady=20)

        self.start_button = Button(root, text="Start", font=("Arial", 14), command=self.start_timer)
        self.start_button.pack(pady=10)

        self.pause_button = Button(root, text="Pause", font=("Arial", 14), command=self.pause_timer, state=DISABLED)
        self.pause_button.pack(pady=10)

        self.pass_button = Button(root, text="Pass", font=("Arial", 14), command=self.reset_timer, state=DISABLED)
        self.pass_button.pack(pady=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

            self.start_button.config(state=DISABLED)
            self.pause_button.config(state=NORMAL)
            self.pass_button.config(state=NORMAL)

    def pause_timer(self):
        if self.is_running:
            self.is_running = False

            self.start_button.config(state=NORMAL)
            self.pause_button.config(state=DISABLED)
            self.pass_button.config(state=DISABLED)

    def reset_timer(self):
        if self.is_running:
            self.time_left = 24
            self.label.config(text=self.time_left)

    def update_timer(self):
        if self.is_running:
            if self.time_left > 0:
                self.time_left -= 1
                self.label.config(text=self.time_left)
                self.root.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.label.config(text="Time's up!")

                self.start_button.config(state=NORMAL)
                self.pause_button.config(state=DISABLED)
                self.pass_button.config(state=DISABLED)

root = Tk()
shot_clock_timer = ShotClockTimer(root)
root.mainloop()
