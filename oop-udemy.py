import random

class DiceGame:

    _counter = 10

    def startGame(self):
        print("🎲🎲🎲🎲🎲🎲🎲Welcome player to the ultimate Dice Game🎲🎲🎲🎲🎲🎲🎲")
        while DiceGame._counter>0:
            self.startRound()
        
        
        
    def startRound(self):
        print(f"\nLet's Start with the Round ",end="\n"*2)
        self.player_choice = int(input("Enter a number between 1 to 6 : "))
        if(self.player_choice < 1 or self.player_choice > 6) or not isinstance(self.player_choice , int):
            print("Please enter a valide number")

        else:
            Die.display_computer_die_value(self)
            

        DiceGame._counter = DiceGame._counter - 1




class Die:
    

    def display_computer_die_value(self):
        self.__computer_die_value = random.randint(1,6)

        print(f"The computer choose the 🎲 value : {self.__computer_die_value}")

        

class Player:
    pass



dg = DiceGame()
dg.startGame()
