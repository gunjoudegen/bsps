from tkinter import *

class Scoreboard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Basketball Scoreboard")
        self.geometry("500x200")

        self.team1_score = 0
        self.team2_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Team 1 Score
        team1_label = Label(self, text="Team 1", font=("Arial", 16))
        team1_label.grid(row=0, column=0, padx=10, pady=5)

        team1_var = StringVar()
        team1_dropdown = OptionMenu(self, team1_var, "", "Foul", "1", "2", "3", command=lambda score: self.update_score(score, 1))
        team1_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Team 2 Score
        team2_label = Label(self, text="Team 2", font=("Arial", 16))
        team2_label.grid(row=1, column=0, padx=10, pady=5)

        team2_var = StringVar()
        team2_dropdown = OptionMenu(self, team2_var, "", "Foul", "1", "2", "3", command=lambda score: self.update_score(score, 2))
        team2_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Team 1 Score Deduction
        team1_deduct_label = Label(self, text="Deduct", font=("Arial", 16))
        team1_deduct_label.grid(row=0, column=3, padx=10, pady=5)

        team1_deduct_var = StringVar()
        team1_deduct_dropdown = OptionMenu(self, team1_deduct_var, "", "Foul", "1", "2", "3", command=lambda score: self.deduct_score(score, 1))
        team1_deduct_dropdown.grid(row=0, column=4, padx=10, pady=5)

        # Team 2 Score Deduction
        team2_deduct_label = Label(self, text="Deduct", font=("Arial", 16))
        team2_deduct_label.grid(row=1, column=3, padx=10, pady=5)

        team2_deduct_var = StringVar()
        team2_deduct_dropdown = OptionMenu(self, team2_deduct_var, "", "Foul", "1", "2", "3", command=lambda score: self.deduct_score(score, 2))
        team2_deduct_dropdown.grid(row=1, column=4, padx=10, pady=5)

        # Scoreboard
        self.team1_score_label = Label(self, text="0", font=("Arial", 32, "bold"), fg="blue")
        self.team1_score_label.grid(row=0, column=2, padx=10, pady=5)

        self.team2_score_label = Label(self, text="0", font=("Arial", 32, "bold"), fg="red")
        self.team2_score_label.grid(row=1, column=2, padx=10, pady=5)

    def update_score(self, selected_score, team):
        if selected_score == "Foul":
            score = 0
        else:
            score = int(selected_score)

        if team == 1:
            self.team1_score += score
            self.team1_score_label.config(text=str(self.team1_score))
        elif team == 2:
            self.team2_score += score
            self.team2_score_label.config(text=str(self.team2_score))

    def deduct_score(self, selected_score, team):
        if selected_score == "Foul":
            score = 0
        else:
            score = int(selected_score)

        if team == 1:
            self.team1_score -= score
            if self.team1_score < 0:
                self.team1_score = 0
            self.team1_score_label.config(text=str(self.team1_score))
        elif team == 2:
            self.team2_score -= score
            if self.team2_score < 0:
                self.team2_score = 0
            self.team2_score_label.config(text=str(self.team2_score))

if __name__ == "__main__":
    scoreboard = Scoreboard()
    scoreboard.mainloop()
