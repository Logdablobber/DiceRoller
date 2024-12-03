import random as rand
from os import system

class DiceResult:
    def __init__(self, rolls:list[int]):
        self.rolls: list[int] = rolls
        
        self.sum: int = 0
        for roll in rolls:
            self.sum += roll
            
    def PrintResult(self, prefix:str):
        rolls_as_string:list[str] = [str(roll) for roll in self.rolls]
        
        print_string:str = f"{prefix}{self.sum}: {', '.join(rolls_as_string)}"
        
        print(print_string)

class Dice:
    def __init__(self, sides, amount, include_zero:bool = False):
        self.sides = sides
        self.amount = amount
        self.has_zero = include_zero
        
    def roll(self, ignore_least_amount:int = 0) -> DiceResult:
        if (self.amount <= 0 or self.sides <= 0 or ignore_least_amount >= self.amount):
            return 0
        
        rolls:list[int] = []
        
        for _ in range(self.amount):
            value = rand.randint(1, self.sides) - (1 if self.has_zero else 0)
            
            rolls.append(value)
            
        if (ignore_least_amount > 0):
            rolls.sort()
            
            for _ in range(ignore_least_amount):
                rolls.pop(0)
            
        return DiceResult(rolls)
    
def PrintTitle():
    system("cls")
    print(r"________  .__               __________       .__  .__                ")
    print(r"\______ \ |__| ____  ____   \______   \ ____ |  | |  |   ___________ ")
    print(r" |    |  \|  |/ ___\/ __ \   |       _//  _ \|  | |  | _/ __ \_  __ \ ")
    print(r" |    `   \  \  \__\  ___/   |    |   (  <_> )  |_|  |_\  ___/|  | \/")
    print(r"/_______  /__|\___  >___  >  |____|_  /\____/|____/____/\___  >__|   ")
    print(r"        \/        \/    \/          \/                      \/       ")
    print()
    print()
    
def PrintError(error: str):
    PrintTitle()
    print(f"ERROR: {error}")
    print()
    input("--Press Enter to Continue--")
    
def ClearDice():
    dice_list.clear()
    print(f"Dice Clear Successfully")
    print()
    input("--Press Enter to Continue--")
    
def ListDice():
    PrintTitle()
    for die in dice_list:
        if (die.amount == 1):
            print(f" - 1 die of sides: {die.sides}")
        else:
            print(f" - {die.amount} dice of sides: {die.sides}")
            
    print()
    input("--Press Enter to Continue--\n")
    
def RollDice():
    PrintTitle()
    
    for dice in dice_list:
        dice.roll().PrintResult(f" - {dice.amount}d{dice.sides}: ")
        
    print()
    input("--Press Enter to Continue--")
    
def InputDice() -> list[Dice]:
    PrintTitle()
    
    print("Enter dice to roll in DND format:")
    print("(i.e. '1d6 2d10' or '2d20 3d10')")
    
    inp:list[str] = input('\n').split()
    
    dice:list[Dice] = []
    
    for dice_inp in inp:
        dice_split:list[str] = dice_inp.lower().split('d')
        
        if (len(dice_split) != 2):
            continue
        
        amount = 0
        sides = 0
        
        try:
            amount = int(dice_split[0])
            sides = int(dice_split[1])
        except:
            continue
        
        if (amount <= 0 or sides <= 0):
            continue
        
        new_dice = Dice(sides, amount)
        
        dice.append(new_dice)
    
    PrintTitle()
    print("Added:")
    print()
    for die in dice:
        if (die.amount == 1):
            print(f" - 1 die of sides: {die.sides}")
        else:
            print(f" - {die.amount} dice of sides: {die.sides}")
            
    print()
    confirmed:str = input("--Enter Y or YES to Confirm--\n")
    
    if (confirmed.lower() in ["y", "yes"]):
        return dice
    
    else:
        PrintError("FAILED TO CONFIRM")
        return []
    

dice_list:list[Dice] = []

def Run():
    
    while True:
        system("cls")
        
        PrintTitle()
        print("CMDS:")
        print(" - LIST ----- list all current dice")
        print(" - ROLL ----- roll all dice")
        print(" - ADD ------ add new dice")
        print(" - CLR ------ to clear current dice")
        print(" - EXIT ----- exit DiceRoller")
        print()
        inp = input(" - ")
        
        match (inp.lower()):
            case "list":
                ListDice()
                
            case "add":
                dice_list.extend(InputDice())
                
            case "clr":
                ClearDice()
                
            case "roll":
                RollDice()
                
            case "exit":
                break
                
            case _:
                PrintError("COMMAND NOT FOUND")
                
            
if (__name__ == "__main__"):
    Run()