import time
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
    def sword_slash(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    def shield_bash(self, enemy):
        damage_to_enemy = (self.base_damage - self.base_damage // 1.75)
        enemy.defense -= damage_to_enemy
        return damage_to_enemy
    def heavy_strike(self, enemy):
        damage_to_enemy = self.base_damage * 2
        enemy.health -= damage_to_enemy
        return damage_to_enemy


class Archer:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self. base_damage = base_damage
    def quick_shot(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    def precise_aim(self, enemy):
        damage_to_enemy = self.base_damage * 1.5
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    def trick_shot(self, enemy, enemy2, enemy3):
        damage_to_enemy = self.base_damage // 2
        enemy.health -= damage_to_enemy
        enemy2.health -= damage_to_enemy
        enemy3.health -= damage_to_enemy
        return damage_to_enemy


class Mage:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self.base_damage = base_damage
    def fireball(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    def arcane_missle(self, enemy):
        damage_to_enemy = self.base_damage * 3
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    def mana_shield(self):
        defense_restored = 5
        self.defense += defense_restored
        return defense_restored


class Enemy1:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self.base_damage = base_damage
    def attack(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    
        
class Enemy2:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self.base_damage = base_damage

    def attack(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    
        
class Enemy3:
    def __init__(self, health, defense, base_damage):
        self.health = health
        self.defense = defense
        self.base_damage = base_damage

    def attack(self, enemy):
        damage_to_enemy = self.base_damage
        enemy.health -= damage_to_enemy
        return damage_to_enemy
    

def arena_battle(knight, archer, mage, enemy1_dead, enemy2_dead, enemy3_dead):
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
            print(archer_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Top  (2) Middle (3) Bottom: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Archer performs Quick Shot on Top. -{archer.quick_shot(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Archer performs Quick Shot on Middle. -{archer.quick_shot(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy 2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Archer performs Quick Shot on Bottom. -{archer.quick_shot(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Archer performs Precise Aim on Top. -{archer.precise_aim(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Archer performs Precise Aim on Middle. -{archer.precise_aim(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy 2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Archer performs Precise Aim on Bottom. -{archer.precise_aim(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 3 and not enemy1_dead:
                print(f"Archer performs Trick Shot on all enemies. -{archer.trick_shot(enemy1, enemy2, enemy3)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
                player = False
                if enemy1.health <= 0:
                    print("You defeated Enemy1")
                    enemy1_dead = True
                if enemy2.health <= 0:
                    print("You defeated Enemy2")
                    enemy2_dead = True
                if enemy3.health <= 0:
                    enemy3_dead = True
                    print("You defeated Enemy3")
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
            print(mage_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Top  (2) Middle (3) Bottom: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Mage performs Fireball on Top. -{mage.fireball(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Mage performs Fireball on Middle. -{mage.fireball(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Mage performs Fireball on Bottom. -{mage.fireball(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Mage performs Arcane Missle on Top. -{mage.arcane_missle(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Mage performs Arcane Missle on Middle. -{mage.arcane_missle(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Mage performs Arcane Missle on Bottom. -{mage.arcane_missle(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 3:
                print(f"Mage performs Mana Shield on itself. +{mage.mana_shield()}")
            else:
                print("Invalid attack selection")
        elif char == "knight":
            char_using = 3
            knight_attack_options = """
      .------------------------.
      /     Knight Attacks     \
     |--------------------------|
     | 1. Sword Slash          |
     | 2. Shield Bash          |
     | 3. Heavy Strike         |
     |--------------------------|
      \________________________/
    """         
            print(knight_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Top  (2) Middle (3) Bottom: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Sword Slash on Top. -{knight.sword_slash(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Sword Slash on Middle. -{knight.sword_slash(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Sword Slash on Bottom. -{knight.sword_slash(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Shield Bash on Top. -{knight.shield_bash(enemy1)} Defense")
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Shield Bash on Middle. -{knight.shield_bash(enemy2)} Defense")
                    if enemy2.health <= 0:
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Shield Bash on Bottom. -{knight.shield_bash(enemy3)} Defense")
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            elif attack_using == 3:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Heavy Strike on Top. -{knight.heavy_strike(enemy1)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy1.health <= 0:
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Heavy Strike on Middle. -{knight.heavy_strike(enemy2)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy2.health <= 0:
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Heavy Strike on Bottom. -{knight.heavy_strike(enemy3)} DMG\n")
                    health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                    print(health_display)
                    if enemy3.health <= 0:
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            else:
                print("Invalid attack selection")
        
        atk_list = ["mage", "archer", "knight"]
        enemy_options = ["Enemy1", "Enemy2", "Enemy3"]
        if enemy1_dead:
            enemy_options.remove("Enemy1")
        elif enemy2_dead:
            enemy_options.remove("Enemy2")
        elif enemy3_dead:
            enemy_options.remove("Enemy3")
        if len(enemy_options) == 0:
            print("You won!!!!")
            break
        if mage.health <= 0:
            atk_list.remove("mage")
        elif knight.health <= 0:
            atk_list.remove("knight")
        elif archer.health <= 0:
            atk_list.remove("archer")
        if len(atk_list) == 0:
            print("Game Over.")
            alive = False
            break
        enemy_atk = random.choice(atk_list)
        enemy_using = random.choice(enemy_options)
        if enemy_using == enemy_options[0]: #Enemy 1
            if enemy_atk == atk_list[0]: #Mage
                print(f"Enemy 1 attacks Mage. - {enemy1.attack(mage)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[1]: #Archer
                print(f"Enemy 1 attacks Archer. - {enemy1.attack(archer)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[2]: #Knight
                print(f"Enemy 1 attacks Knight. - {enemy1.attack(knight)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
        elif enemy_using == enemy_options[1]: #Enemy 2
            if enemy_atk == atk_list[0]: #Mage
                print(f"Enemy 2 attacks Mage. - {enemy2.attack(mage)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[1]: #Archer
                print(f"Enemy 2 attacks Knight. - {enemy1.attack(knight)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[2]: #Knight
                print(f"Enemy 2 attacks Knight. - {enemy2.attack(knight)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
        elif enemy_using == enemy_options[2]: #Enemy 3
            if enemy_atk == atk_list[0]: #Mage
                print(f"Enemy 3 attacks Mage. - {enemy3.attack(mage)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[1]: #Archer
                print(f"Enemy 3 attacks Archer. - {enemy3.attack(archer)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
            elif enemy_atk == atk_list[2]: #Knight
                print(f"Enemy 3 attacks Knight. - {enemy3.attack(knight)} DMG\n")
                health_display = f"""
    ##################################################################################
    Archer| Health: {archer.health}         |          Enemy 1| Health: {enemy1.health}
                                            |
    Mage  | Health: {mage.health}           |          Enemy 2| Health: {enemy2.health}
                                            |
    Knight| Health: {knight.health}         |          Enemy 3| Health: {enemy3.health}
    ##################################################################################
"""
                print(health_display)
        
        if knight.health <= 0 and mage.health <= 0 and archer.health <= 0: 
            print("You died.")
            alive = False
            break



username = input("Enter your username: ")
print("\n" * 20)


print(f"Hello {username}.\n")
print("Your task is to fight and survive in the Trios Arena.")
print("Good luck.......")

knight = Knight(100, 35, 28)
mage = Mage(75, 50, 30)
archer = Archer(120, 20, 25)
enemy1 = Enemy1(150, 60, 15)
enemy2 = Enemy2(200, 30, 20)
enemy3 = Enemy3(100, 15, 10)
global enemy1_dead
global enemy2_dead
global enemy3_dead 
enemy1_dead = False
enemy2_dead = False
enemy3_dead = False


    






run = True
while run:
    user = input("*> ").lower()

    if user == "start battle":
        print("Prepare for battle!")
        time.sleep(3)
        arena_battle(knight, archer, mage, enemy1_dead, enemy2_dead, enemy3_dead)
    elif user == "quit":
        break
    elif user == "stats":
        pass
    elif user == "help":
        pass

