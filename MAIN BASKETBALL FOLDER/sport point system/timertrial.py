from tkinter import *
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, minutes):
        self.root = Tk()
        self.root.title("Countdown Timer")

        # Set the window size and position it in the center
        window_width = 1080
        window_height = 720

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.total_seconds = minutes * 60
        self.remaining_seconds = self.total_seconds
        self.is_paused = True

        self.label = Label(self.root, font=("Helvetica", 48), text="")
        self.label.pack(padx=50, pady=20)

        self.start_button = Button(self.root, text="Start", relief=FLAT, command=self.start_timer)
        self.pause_button = Button(self.root, text="Pause", relief=FLAT, command=self.pause_timer)
        self.reset_button = Button(self.root, text="Reset", relief=FLAT, command=self.reset_timer)

        self.start_button.pack(side=TOP, padx=10, pady=10)
        self.pause_button.pack(side=TOP, padx=10, pady=10)
        self.reset_button.pack(side=TOP, padx=10, pady=10)

        self.update_timer()

        self.root.mainloop()

    def update_timer(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_string)

        if not self.is_paused:
            if self.remaining_seconds > 0:
                self.remaining_seconds -= 1
                self.root.after(1000, self.update_timer)
            else:
                messagebox.showinfo("Time's up!", "The countdown timer has ended.")

    def start_timer(self):
        if self.is_paused:
            self.is_paused = False
            self.update_timer()

    def pause_timer(self):
        self.is_paused = True

    def reset_timer(self):
        self.is_paused = True
        self.remaining_seconds = self.total_seconds
        self.label.config(text="")

# Create a CountdownTimer object with 12 minutes (720 seconds)
timer = CountdownTimer(12)
