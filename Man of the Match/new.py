import tkinter as tk
from tkinter import simpledialog

class FantasyCricketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fantasy Cricket")
        self.teams = []
        self.current_team = None
        
        # Create a menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        self.team_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Manage Teams", menu=self.team_menu)
        self.team_menu.add_command(label="Create New Team", command=self.create_new_team)
        self.team_menu.add_command(label="Open Existing Team", command=self.open_existing_team)
        self.team_menu.add_command(label="Save Team", command=self.save_team)
        self.team_menu.add_command(label="Evaluate Score", command=self.evaluate_score)

        # Create the opening screen
        self.create_opening_screen()

    def create_opening_screen(self):
        self.team_selection = tk.StringVar()
        self.team_selection.set("Select Team")
        
        self.label = tk.Label(self.root, text="Fantasy Cricket")
        self.label.pack()
        
        self.team_label = tk.Label(self.root, text="Select a Team:")
        self.team_label.pack()
        
        self.team_dropdown = tk.OptionMenu(self.root, self.team_selection, "Select Team")
        self.team_dropdown.pack()
        self.team_dropdown.config(state=tk.DISABLED)
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()
        
    def create_new_team(self):
        team_name = simpledialog.askstring("Team Name", "Enter the name of your new team:")
        if team_name:
            self.teams.append({"Team Name": team_name, "Players": []})
            self.team_selection.set(team_name)
            self.team_dropdown['menu'].delete(0, 'end')
            for team in self.teams:
                self.team_dropdown['menu'].add_command(label=team["Team Name"], command=tk._setit(self.team_selection, team["Team Name"]))
            self.team_dropdown.config(state=tk.NORMAL)
    
    def open_existing_team(self):
        team_name = simpledialog.askstring("Team Name", "Enter the name of your existing team:")
        if team_name:
            for team in self.teams:
                if team["Team Name"] == team_name:
                    self.current_team = team
                    self.team_selection.set(team_name)
                    print(f"Opened {team_name} team.")
                    return
            print(f"Team '{team_name}' not found.")
    
    def save_team(self):
        if self.current_team:
            # Implement the code to save the team and its players to a file
            print(f"Saved {self.current_team['Team Name']} team.")
        else:
            print("No team selected to save.")
    
    def evaluate_score(self):
        if self.current_team:
            # Implement the code to evaluate the score of the current team
            print(f"Evaluating the score for {self.current_team['Team Name']} team.")
        else:
            print("No team selected to evaluate.")

    def start_game(self):
        if self.current_team:
            # Implement the code to start the game with the selected team
            print(f"Starting the game with {self.current_team['Team Name']} team.")
        else:
            print("No team selected to start the game.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FantasyCricketApp(root)
    root.mainloop()
