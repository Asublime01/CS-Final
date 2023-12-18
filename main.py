import time
import random

arena_trios_display = """
       (                         
    () |\                               
    <==|=@                                                                                                         
    [\ |/                                                    
    ||`(                                                            
    LL                                                                                                                            

    
                             _
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
        damage_to_enemy = (self.base_damage * 1.5) // 1
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
    

def arena_battle(knight, archer, mage, enemy1_dead, enemy2_dead, enemy3_dead, atk_list):
    print(arena_trios_display)
    print("Welcome to the Trios Arena!")
    print("Do anything you need to keep you and your team ALIVE.")
    alive = True
    global player_won
    global player_died
    player_won = False
    player_died = False
    while alive:
        attack_using = 0
        attacking = 0
        print("It is your turn. Who will you use?(archer, knight, mage)")
        char = input("*> ").lower()
        if char == "archer":
            char_using = 1 #1 is archer
            archer_attack_options = """
       .------------------------.
      /    Archer Attacks       |
     |--------------------------|
     | 1. Quick Shot           |
     | 2. Precise Aim          |
     | 3. Trick Shot           |
     |--------------------------|
      \________________________/
    """         
            print(archer_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Enemy 1  (2) Enemy 2 (3) Enemy 3: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Archer performs Quick Shot on Enemy 1. -{archer.quick_shot(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Archer performs Quick Shot on Enemy 2. -{archer.quick_shot(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy 2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Archer performs Quick Shot on Enemy 3. -{archer.quick_shot(enemy3)} DMG\n")
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
                        enemy3.health = 0
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Archer performs Precise Aim on Enemy 1. -{archer.precise_aim(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Archer performs Precise Aim on Enemy 2. -{archer.precise_aim(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy 2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Archer performs Precise Aim on Enemy 3. -{archer.precise_aim(enemy3)} DMG\n")
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
                        enemy3.health = 0
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
                    enemy1.health = 0
                    print("You defeated Enemy1")
                    enemy1_dead = True
                if enemy2.health <= 0:
                    enemy2.health = 0
                    print("You defeated Enemy2")
                    enemy2_dead = True
                if enemy3.health <= 0:
                    enemy3.health = 0
                    enemy3_dead = True
                    print("You defeated Enemy3")
            else:
                print("Invalid attack selection")
        elif char == "mage":
            char_using = 2
            mage_attack_options = """
       .------------------------.
      /       Mage Spells      |
     |--------------------------|
     | 1. Fireball             |
     | 2. Arcane Missile       |
     | 3. Mana Shield          |
     |--------------------------|
      \________________________/
    """ 
            print(mage_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Enemy 1  (2) Enemy 2 (3) Enemy 3: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Mage performs Fireball on Enemy 1. -{mage.fireball(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Mage performs Fireball on Enemy 2. -{mage.fireball(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Mage performs Fireball on Enemy 3. -{mage.fireball(enemy3)} DMG\n")
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
                        enemy3.health = 0
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Mage performs Arcane Missle on Enemy 1. -{mage.arcane_missle(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Mage performs Arcane Missle on Enemy 2. -{mage.arcane_missle(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Mage performs Arcane Missle on Enemy 3. -{mage.arcane_missle(enemy3)} DMG\n")
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
                        enemy3.health = 0
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
      /     Knight Attacks     |
     |--------------------------|
     | 1. Sword Slash          |
     | 2. Shield Bash          |
     | 3. Heavy Strike         |
     |--------------------------|
      \________________________/
    """         
            print(knight_attack_options)
            attack_using = int(input("Choose your attack: "))
            attacking = int(input("Who will you attack? (1) Enemy 1  (2) Enemy 2 (3) Enemy 3: "))
            if attack_using == 1:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Sword Slash on Enemy 1. -{knight.sword_slash(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Sword Slash on Enemy 2. -{knight.sword_slash(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Sword Slash on Enemy 3. -{knight.sword_slash(enemy3)} DMG\n")
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
                        enemy3.health = 0
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            elif attack_using == 2:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Shield Bash on Enemy 1. -{knight.shield_bash(enemy1)} Defense")
                    if enemy1.health <= 0:
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Shield Bash on Enemy 2. -{knight.shield_bash(enemy2)} Defense")
                    if enemy2.health <= 0:
                        enemy2.health = 0
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Shield Bash on Enemy 3. -{knight.shield_bash(enemy3)} Defense")
                    if enemy3.health <= 0:
                        enemy3.health = 0
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            elif attack_using == 3:
                if attacking == 1 and not enemy1_dead:
                    print(f"Knight performs Heavy Strike on Enemy 1. -{knight.heavy_strike(enemy1)} DMG\n")
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
                        enemy1.health = 0
                        print("You defeated Enemy 1!")
                        enemy1_dead = True
                elif attacking == 2 and not enemy2_dead:
                    print(f"Knight performs Heavy Strike on Enemy 2. -{knight.heavy_strike(enemy2)} DMG\n")
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
                        enemy2.health = 0
                        print("You defeated Enemy2")
                        enemy2_dead = True
                elif attacking == 3 and not enemy3_dead:
                    print(f"Knight performs Heavy Strike on Enemy 3. -{knight.heavy_strike(enemy3)} DMG\n")
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
                        enemy3.health = 0
                        print("You defeated Enemy 3")
                        enemy3_dead = True
                else:
                    print("Invalid target selection or your target is already dead :(")
            else:
                print("Invalid attack selection")
        time.sleep(1.5)
        enemy_options = ["Enemy1", "Enemy2", "Enemy3"]
        if enemy1_dead:
            enemy_options.remove("Enemy1")
        elif enemy2_dead:
            enemy_options.remove("Enemy2")
        elif enemy3_dead:
            enemy_options.remove("Enemy3")
        if len(enemy_options) == 0:
            player_won = True
            player_died = False
            return player_died, player_won
        
        #if len(atk_list) == 0:
        #    print("Game Over.")
        #    alive = False
        #    break
        
        enemy_atk = random.choice(atk_list)
        enemy_using = random.choice(enemy_options)
        
        if enemy_using == enemy_options[0]: #Enemy 1
            if enemy_atk == "mage": #Mage
                print(f"Enemy 1 attacks Mage. - {enemy1.attack(mage)} DMG\n")
                if mage.health <= 0:
                    mage.health = 0
                    if "mage" in atk_list:
                        atk_list.remove("mage")
                        
                    else:
                        pass
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
            elif enemy_atk == "archer": #Archer
                print(f"Enemy 1 attacks Archer. - {enemy1.attack(archer)} DMG\n")
                if archer.health <= 0:
                    archer.health = 0
                    if "archer" in atk_list:
                        atk_list.remove("archer")
                        
                    else:
                        pass
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
            elif enemy_atk == "knight": #Knight
                print(f"Enemy 1 attacks Knight. - {enemy1.attack(knight)} DMG\n")
                if knight.health <= 0:
                    knight.health = 0
                    if "knight" in atk_list:
                        atk_list.remove("knight")
                        
                    else:
                        pass
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
            if enemy_atk == "mage": #Mage
                print(f"Enemy 2 attacks Mage. - {enemy2.attack(mage)} DMG\n")
                if mage.health <= 0:
                    mage.health = 0
                    if "mage" in atk_list:
                        atk_list.remove("mage")
                        
                    else:
                        pass
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
            elif enemy_atk == "archer": #Archer
                print(f"Enemy 2 attacks Archer. - {enemy1.attack(archer)} DMG\n")
                if archer.health <= 0:
                    archer.health = 0
                    if "archer" in atk_list:
                        atk_list.remove("archer")
                        
                    else:
                        pass
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
            elif enemy_atk == "knight": #Knight
                print(f"Enemy 2 attacks Knight. - {enemy2.attack(knight)} DMG\n")
                if knight.health <= 0:
                    knight.health = 0
                    if "knight" in atk_list:
                        atk_list.remove("knight")
                        
                    else:
                        pass
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
            if enemy_atk == "mage": #Mage
                print(f"Enemy 3 attacks Mage. - {enemy3.attack(mage)} DMG\n")
                if mage.health <= 0:
                    mage.health = 0
                    if "mage" in atk_list:
                        atk_list.remove("mage")
                        
                    else:
                        pass
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
            elif enemy_atk == "archer": #Archer
                print(f"Enemy 3 attacks Archer. - {enemy3.attack(archer)} DMG\n")
                if archer.health <= 0:
                    archer.health = 0
                    if "archer" in atk_list:
                        atk_list.remove("archer")
                        
                    else:
                        pass
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
            elif enemy_atk == "knight": #Knight
                print(f"Enemy 3 attacks Knight. - {enemy3.attack(knight)} DMG\n")
                if knight.health <= 0:
                    knight.health = 0
                    if "knight" in atk_list:
                        atk_list.remove("knight")
                        
                    else:
                        pass
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
            player_died = True
            player_won = False
            return player_died, player_won
            




username = input("Enter your username: ")
print("\n" * 20)


print(f"Hello {username}.\n")


knight = Knight(100, 35, 28)
mage = Mage(75, 50, 30)
archer = Archer(120, 20, 25)
enemy1 = Enemy1(150, 60, 15)
enemy2 = Enemy2(200, 30, 20)
enemy3 = Enemy3(100, 15, 10)
global enemy1_dead
global enemy2_dead
global enemy3_dead 
global atk_list
enemy1_dead = False
enemy2_dead = False
enemy3_dead = False
atk_list = ["mage", "archer", "knight"]


help_message = """
Welcome to the Trios Arena!
In this game, you control a team of three heroes - Archer, Mage, and Knight. Your goal is to defeat the three enemy monsters (Enemy 1, Enemy 2, and Enemy 3) in the arena.

Here are some basics to get you started:

1. **Controls:**
   - Type the name of the character you want to use during your turn (Archer, Mage, or Knight).
   - Choose attacks and targets by following the on-screen instructions.

2. **Available Characters:**
   - Archer: Specializes in ranged attacks.
   - Mage: Uses powerful spells for various effects.
   - Knight: Excels in close combat and defense.

3. **Turns:**
   - It's your turn to choose actions for your team.
   - After your turn, the enemy monsters will attack.

4. **Attacks:**
   - Each character has different attacks.
   - Choose your attack and target wisely.

5. **Health Display:**
   - The display shows the health of your team and the enemy monsters.
   - Keep an eye on your team's health to avoid defeat.

6. **Winning:**
   - Defeat all three enemy monsters to win the game.

7. **Losing:**
   - If all your heroes (Archer, Mage, and Knight) run out of health, it's game over.

8. **Game Progress:**
   - The game will provide updates on defeated enemies and your team's status.

Good luck in the Arena!
"""
print(help_message)
   






run = True
while run:
    print("Type 'start battle' to begin.")
    user = input("*> ").lower()

    if user == "start battle":
        print("Prepare for battle!")
        time.sleep(3)
        player_died, player_won = arena_battle(knight, archer, mage, enemy1_dead, enemy2_dead, enemy3_dead, atk_list)
        if player_died:
            print("""\n
       _____          __  __ ______     ______      ________ _____  
      / ____|   /\   |  \/  |  ____|   / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__     | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|    | |  | |\ \/ / |  __| |  _  / 
     | |__| |/ ____ \| |  | | |____   | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|   \____/   \/   |______|_|  \_|

                        IT LOOKS LIKE YOU DIED :(
              MAYBE YOU SHOULD DO BETTER NEXT TIME :P
    """)
        elif player_won:
            print("""
__   __   ___     ___    _____    ___     ___   __   __ 
 \ \ / /  |_ _|   / __|  |_   _|  / _ \   | _ \  \ \ / / 
  \ V /    | |   | (__     | |   | (_) |  |   /   \ V /  
  _\_/_   |___|   \___|   _|_|_   \___/   |_|_\   _|_|_  

                GOOD JOB!! YOU BEAT THE GAME
                    THANKS FOR PLAYING!
""")
    elif user == "quit":
        break
    else:
        print("Try again.")
        continue
