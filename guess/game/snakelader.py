import random
import time

class SnakeAndLadder:
    def __init__(self):
        self.snakes = {
            17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79
        }
        self.ladders = {
            4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91
        }
        self.players = []
        self.positions = {}
        
    def add_player(self, name):
        self.players.append(name)
        self.positions[name] = 0
        
    def roll_dice(self):
        return random.randint(1, 6)
    
    def move_player(self, player):
        dice_roll = self.roll_dice()
        print(f"{player} rolled a {dice_roll}!")
        
        new_position = self.positions[player] + dice_roll
        
        if new_position > 100:
            print(f"{player} needs {100 - self.positions[player]} to win. Stay at {self.positions[player]}.")
            return False
        
        self.positions[player] = new_position
        print(f"{player} moved to {new_position}")
        
   
        if new_position in self.snakes:
            self.positions[player] = self.snakes[new_position]
            print(f"Oh no! Snake bite! {player} slides down to {self.positions[player]}")
        elif new_position in self.ladders:
            self.positions[player] = self.ladders[new_position]
            print(f"Yay! Ladder climb! {player} jumps up to {self.positions[player]}")
        
        return new_position == 100
    
    def play(self):
        print("Welcome to Snake and Ladder Game!")
        print("Snakes:", self.snakes)
        print("Ladders:", self.ladders)
        print()
        
        num_players = int(input("Enter number of players: "))
        for i in range(num_players):
            name = input(f"Enter player {i+1} name: ")
            self.add_player(name)
        
        print("\nGame starts!\n")
        
        while True:
            for player in self.players:
                input(f"{player}'s turn. Press Enter to roll the dice...")
                won = self.move_player(player)
                print(f"Current positions: {self.positions}\n")
                
                if won:
                    print(f"Congratulations {player}! You won the game!")
                    return
                
                time.sleep(1)  


if __name__ == "__main__":
    game = SnakeAndLadder()
    game.play()