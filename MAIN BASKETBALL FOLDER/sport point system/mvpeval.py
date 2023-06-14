import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = [0, 0, 0, 0]
        self.total_score = 0
        self.mvp = False

class Scoreboard(tk.Tk):
    def __init__(self, team_a_players, team_b_players):
        super().__init__()

        self.title("Basketball Scoreboard")

        self.team_a_players = team_a_players
        self.team_b_players = team_b_players

        self.create_widgets()

    def create_widgets(self):
        # Create team A scoreboard
        team_a_label = tk.Label(self, text="Team A")
        team_a_label.grid(row=0, column=0)

        team_a_scores_label = tk.Label(self, text="Scores")
        team_a_scores_label.grid(row=1, column=0)

        self.team_a_widgets = []
        for row, player in enumerate(self.team_a_players, start=2):
            player_label = tk.Label(self, text=player.name)
            player_label.grid(row=row, column=0)

            scores_entry = []
            for col in range(4):
                score_entry = tk.Entry(self, width=5)
                score_entry.grid(row=row, column=col+1)
                scores_entry.append(score_entry)
            self.team_a_widgets.append(scores_entry)

        # Create team B scoreboard
        team_b_label = tk.Label(self, text="Team B")
        team_b_label.grid(row=0, column=6)

        team_b_scores_label = tk.Label(self, text="Scores")
        team_b_scores_label.grid(row=1, column=6)

        self.team_b_widgets = []
        for row, player in enumerate(self.team_b_players, start=2):
            player_label = tk.Label(self, text=player.name)
            player_label.grid(row=row, column=6)

            scores_entry = []
            for col in range(4):
                score_entry = tk.Entry(self, width=5)
                score_entry.grid(row=row, column=col+7)
                scores_entry.append(score_entry)
            self.team_b_widgets.append(scores_entry)

        # Calculate scores button
        calculate_button = tk.Button(self, text="Calculate MVPs", command=self.calculate_mvp)
        calculate_button.grid(row=len(self.team_a_players)+2, column=0, columnspan=11)

    def calculate_mvp(self):
        # Reset MVP status for all players
        for player in self.team_a_players + self.team_b_players:
            player.total_score = 0
            player.mvp = False

        # Update player scores and calculate total scores
        for row, player in enumerate(self.team_a_players):
            for col, score_entry in enumerate(self.team_a_widgets[row]):
                score = int(score_entry.get())
                player.scores[col] = score
                player.total_score += score

        for row, player in enumerate(self.team_b_players):
            for col, score_entry in enumerate(self.team_b_widgets[row]):
                score = int(score_entry.get())
                player.scores[col] = score
                player.total_score += score

        # Determine MVPs
        team_a_mvp = max(self.team_a_players, key=lambda player: player.total_score)
        team_a_mvp.mvp = True

        team_b_mvp = max(self.team_b_players, key=lambda player: player.total_score)
        team_b_mvp.mvp = True

        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear previous MVP status
        for row in self.team_a_widgets:
            for entry in row:
                entry.configure(bg="white")

        for row in self.team_b_widgets:
            for entry in row:
                entry.configure(bg="white")

        # Update MVP status
        for row, player in enumerate(self.team_a_players):
            if player.mvp:
                for entry in self.team_a_widgets[row]:
                    entry.configure(bg="green")

        for row, player in enumerate(self.team_b_players):
            if player.mvp:
                for entry in self.team_b_widgets[row]:
                    entry.configure(bg="green")

if __name__ == "__main__":
    # Create player objects
    team_a_players = [
        Player("Player1"),
        Player("Player2"),
        Player("Player3"),
        Player("Player4"),
        Player("Player5")
    ]

    team_b_players = [
        Player("Player6"),
        Player("Player7"),
        Player("Player8"),
        Player("Player9"),
        Player("Player10")
    ]

    # Create and run the scoreboard
    scoreboard = Scoreboard(team_a_players, team_b_players)
    scoreboard.mainloop()
