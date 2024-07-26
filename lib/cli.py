import os
import time
import random

class MaandamanoQuest:
    def __init__(self):
        self.player = {"influence": 0, "supporters": 0, "resources": 0}
        self.current_location = None
        self.locations = {}
        self.quests = []
        self.current_day = 1
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_ascii_art(self):
        art = """
 __  __                      _                                      ___                  _   
|  \/  | __ _  __ _ _ __  __| | __ _ _ __ ___   __ _ _ __   ___    / _ \ _   _  ___  ___| |_ 
| |\/| |/ _` |/ _` | '_ \/ _` |/ _` | '_ ` _ \ / _` | '_ \ / _ \  | | | | | | |/ _ \/ __| __|
| |  | | (_| | (_| | | | | (_| | (_| | | | | | | (_| | | | |  __/ | |_| | |_| |  __/\__ \ |_ 
|_|  |_|\__,_|\__,_|_| |_|\__,_|\__,_|_| |_| |_|\__,_|_| |_|\___|  \__\_\\__,_|\___||___/\__|

        """
        print(art)
    
    def colored_print(self, message, color_code):
        print(f"{color_code}{message}\033[0m")
        
    def main_menu(self):
        while True:
            self.clear_screen()
            self.display_ascii_art()
            print("\nWelcome to Maandamano Quest: The Journey for Change")
            print("\n1. New Game")
            print("2. Load Game")
            print("3. High Scores")
            print("4. Quit")
            
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                self.new_game()
            elif choice == '2':
                self.load_game()
            elif choice == '3':
                self.show_high_scores()
            elif choice == '4':
                self.colored_print("Thank you for playing Maandamano Quest!", "\033[92m")
                break
            else:
                self.colored_print("Invalid choice. Please try again.", "\033[91m")
                time.sleep(1)
                
    def new_game(self):
        self.clear_screen()
        self.colored_print("Starting a new quest for change...", "\033[92m")
        self.start_game()
        input("Press Enter to return to the main menu...")
        
    def load_game(self):
        self.clear_screen()
        self.colored_print("Loading your progress...", "\033[92m")
        # TODO: Implement game loading
        input("Press Enter to return to the main menu...")
        
    def show_high_scores(self):
        self.clear_screen()
        self.colored_print("Champions of Change:", "\033[92m")
        # TODO: Implement high score display
        input("Press Enter to return to the main menu...")

    def start_game(self):
        self.initialize_world()
        self.main_game_loop()

    def initialize_world(self):
        self.locations = {
            "City Center": {"description": "The heart of the city, bustling with activity."},
            "University Campus": {"description": "A hub of knowledge and student activism."},
            "Industrial District": {"description": "Factories and warehouses dominate this area."},
            "Residential Area": {"description": "Quiet streets lined with homes and small shops."},
            "Government Quarter": {"description": "Official buildings and heavy security presence."}
        }
        self.current_location = "City Center"
        self.generate_quests()

    def generate_quests(self):
        quest_templates = [
            {"name": "Organize a Protest", "description": "Gather supporters for a peaceful demonstration."},
            {"name": "Distribute Flyers", "description": "Spread awareness about an important issue."},
            {"name": "Negotiate with Officials", "description": "Attempt to make progress through official channels."},
            {"name": "Community Outreach", "description": "Build support in a local neighborhood."},
            {"name": "Fundraising Campaign", "description": "Raise resources for the cause."}
        ]
        self.quests = random.sample(quest_templates, 3)  # Start with 3 random quests

    def main_game_loop(self):
        while True:
            self.display_game_status()
            action = self.get_player_action()
            if action == "4":  # Quit game
                break
            self.process_action(action)
            self.advance_time()

    def display_game_status(self):
        self.clear_screen()
        print(f"Day: {self.current_day}")
        print(f"Location: {self.current_location}")
        print(f"Influence: {self.player['influence']}")
        print(f"Supporters: {self.player['supporters']}")
        print(f"Resources: ${self.player['resources']}")
        print("\n" + self.locations[self.current_location]['description'])

    def get_player_action(self):
        print("\nAvailable Actions:")
        print("1. Move to a new location")
        print("2. View quests")
        print("3. Rest")
        print("4. Quit game")
        while True:
            choice = input("Choose an action (1-4): ")
            if choice in ['1', '2', '3', '4']:
                return choice
            self.colored_print("Invalid choice. Please try again.", "\033[91m")

    def process_action(self, action):
        if action == '1':
            self.move_to_new_location()
        elif action == '2':
            self.view_quests()
        elif action == '3':
            self.rest()
        # '4' (Quit) is handled in the main game loop

    def move_to_new_location(self):
        print("\nAvailable locations:")
        for i, location in enumerate(self.locations.keys(), 1):
            print(f"{i}. {location}")
        while True:
            try:
                choice = int(input("Choose a location number: "))
                if 1 <= choice <= len(self.locations):
                    self.current_location = list(self.locations.keys())[choice - 1]
                    self.colored_print(f"You have moved to {self.current_location}.", "\033[92m")
                    break
                else:
                    self.colored_print("Invalid choice. Please try again.", "\033[91m")
            except ValueError:
                self.colored_print("Please enter a number.", "\033[91m")
        input("Press Enter to continue...")

    def view_quests(self):
        print("\nAvailable Quests:")
        for i, quest in enumerate(self.quests, 1):
            print(f"{i}. {quest['name']}: {quest['description']}")
        input("Press Enter to continue...")

    def rest(self):
        supporters_increase = random.randint(1, 5)
        resources_increase = random.randint(10, 50)
        self.player['supporters'] += supporters_increase
        self.player['resources'] += resources_increase
        self.colored_print("You take some time to rest and recuperate.", "\033[92m")
        self.colored_print(f"Supporters +{supporters_increase}, Resources +${resources_increase}", "\033[92m")
        input("Press Enter to continue...")

    def advance_time(self):
        self.current_day += 1
        if self.current_day % 7 == 0:
            self.weekly_update()

    def weekly_update(self):
        print("\nWeekly Update:")
        influence_change = random.randint(-5, 10)
        self.player['influence'] += influence_change
        self.colored_print(f"Your influence has changed by {influence_change}", "\033[92m")
        if random.random() < 0.3:  # 30% chance of a random event
            self.random_event()
        input("Press Enter to continue...")

    def random_event(self):
        events = [
            "A local newspaper publishes a story about your cause.",
            "A rival activist group challenges your methods.",
            "A wealthy donor offers to support your cause.",
            "Government officials increase scrutiny on activist groups."
        ]
        event = random.choice(events)
        self.colored_print(f"Random Event: {event}", "\033[92m")
        # TODO: Implement effects of random events

if __name__ == "__main__":
    game = MaandamanoQuest()
    game.main_menu()
