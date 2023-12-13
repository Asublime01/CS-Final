import random


arena_trios_display = """
       (
    () |\ 
    <==|=@ 
    [\ |/       
    ||`( 
    LL                                                                 


                        ,     _
                       /|   | |
                     _/_\_  >_<
                    .-\-/.   |
                   /  | | \_ |
                   \ \| |\__(/
                   /(`---')  |
                  / /     \  |
               _.'  \  ._/   |
               `----'`=-='   '                                     


       ~O
     /~()'-{---
      /~)
      ~ ~
                                                                
"""

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


def arena_battle(knight, archer, mage):
    print(arena_trios_display)
    print("Welcome to the Trios Arena!")
    print("Do anything you need to keep you and your team ALIVE.")
    alive = True
    while alive:
        char_using = 0 # Not using anything
        attack_using = 0
        attacking = 0
        print("It is your turn. Who will you use?")
        char = input("*> ").lower()
        if char == "archer":
            char_using = 1 #1 is archer
            archer_attack_options = """
   .------------------------.
  /    Archer Attacks     \
 |--------------------------|
 | 1. Quick Shot           |
 | 2. Precise Aim          |
 | 3. Trick Shot           |
 |--------------------------|
  \________________________/

"""
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Top  (2) Middle (3) Bottom: "))

            if attack_using == 1:
                if attacking == 1:
                    print("Archer performs Quick Shot on Top.")
                elif attacking == 2:
                    print("Archer performs Quick Shot on Middle")
                elif attacking == 3:
                    print("Archer performs Quick Shot on Bottom")
                else:
                    print("Invalid target selection")

            elif attack_using == 2:
                if attacking == 1:
                    print("Archer performs Precise Aim on Top")
                elif attacking == 2:
                    print("Archer performs Precise Aim on Middle")
                elif attacking == 3:
                    print("Archer performs Precise Aim on Bottom")
                else:
                    print("Invalid target selection")

            elif attack_using == 3:
                if attacking == 1:
                    print("Archer performs Trick Shot on Top")
                elif attacking == 2:
                    print("Archer performs Trick Shot on Middle")
                elif attacking == 3:
                    print("Archer performs Trick Shot on Bottom")
                else:
                    print("Invalid target selection")

            else:
                print("Invalid attack selection")

        elif char == "mage":
            char_using = 2
            mage_attack_options = """
   .------------------------.
  /       Mage Spells      \
 |--------------------------|
 | 1. Fireball             |
 | 2. Arcane Missile       |
 | 3. Mana Shield          |
 |--------------------------|
  \________________________/

"""
        elif char == "knight":
            char_using = 3
            knight_attack_options = """
   .------------------------.
  /     Knight Attacks     \
 |--------------------------|
 | 1. Sword Slash          |
 | 2. Shield Bash          |
 | 3. Heavy Strike         |
 | 4. Defensive Stance     |
 | 5. Counterattack        |
 |--------------------------|
  \________________________/
"""
        else:
            continue
 
username = input("Enter your username: ")
print("\n" * 20)


print(f"Hello {username}.\n")
print("Your task is to fight and survive in the Trios Arena.")
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
        arena_battle(knight, archer, mage)
    elif user == "quit":
        break
    elif user == "stats":
        pass
    elif user == "help":
        pass