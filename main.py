import random

knight_art = """
       ~O
     /~()'-{---
      /~)
      ~ ~

"""
mage_art = """
            ,    _
           /|   | |
         _/_\_  >_<
        .-\-/.   |
       /  | | \_ |
       \ \| |\__(/
       /(`---')  |
      / /     \  |
   _.'  \  ._/   |
   `----'`=-='   ' 

"""

archer_art = """
       (
    () |\ 
    <==|=@ 
    [\ |/       
    ||`( 
    LL 
"""
arena_squads_display = f"""
{knight_art}                                                                #


            
            {mage_art}                 VS                              #                    



{archer_art}                                                                #
"""
class Player:
    def __init__(self, health, defense, base_damage, name):
        self.health = health
        self.defense = defense
        self.base_damage = base_damage
        self.name = name

class Knight:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self. base_damage = base_damage
    
class Archer:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self. base_damage = base_damage
    
class Mage:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self. base_damage = base_damage


def arena_battle(player, knight, archer, mage):
    print("Welcome to the Squads Arena!")
    print("Do anything you need to keep you and your team ALIVE.\n\n\n\n\n")
    print(arena_squads_display)
    

username = input("Enter your username: ")
print("\n" * 20)
player = Player(150, 40, 30, username)

print(f"Hello {player.name}.\n")
print("Your task is to fight and survive in the Squad's Arena.")
print("Good luck.......")

knight = Knight(100, 35, 20)
mage = Mage(75, 50, 30)
archer = Archer(120, 20, 25)


arena_commands = ['attack top', 'attack middle', 'attack bottom', 'heal top', 'heal bottom', 'heal middle', 'heal self']
basic_commands = ['stats', 'help', 'quit', 'start battle']


run = True
while run:
    user = input("*> ").lower()

    if user == "start battle":
        arena_battle(player, knight, archer, mage)
    elif user == "quit":
        pass
    elif user == "stats":
        pass
    elif user == "help":
        pass