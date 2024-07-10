''' Enemy class for the maze game. Enemy – extends entity - monster character that the hero encounters in the maze. 

Written by: Olivia Fishbough and Analicia Sosa

Functions:
  __init__(self) – randomizes a name from a list of names (ex. ‘Goblin’, ‘Troll’, ‘Ghoul’, ‘Skeleton’, ‘Kobold’, etc) and randomizes the monster’s hp (4-8). 
  attack(self, entity) – enemy attacks hero – randomize damage in the range 1-4. The hero should take the damage and the method should return a string representing the event. 

Usage: in your program, import enemy. Use the attack and take damage functions to fight the hero. 

Example Usage:

	monster = enemy.Enemy()
    print("\nYou encounter " + str(monster))
    player.attack(monster)
    if monster.hp <= 0:
      print("You have slain " + monster.name)
      board.remove_at_loc(player.location)
      break
    monster.attack(player)

''' 

# import statements
import entity
import random

class Enemy(entity.Entity):
  def __init__(self):
    ''' Constructor randomizes a name from a list of names (ex. ‘Goblin’, ‘Troll’, ‘Ghoul’, ‘Skeleton’, ‘Kobold’, etc) and randomizes the monster’s hp (4-8). 

    Args:
      self (Enemy): assigns the method to the Enemy class

    Returns:
      None
  
  '''
    self.name = random.choice(['Nazgul','Ringwraiths', 'Sauron', 'Death Eater', 'Sith Lord', 'Voldemort', 'Darth Vader', 'Smaug', 'Clickers','Sephiroth','Lingering Will', 'Itty Bitty Fishy'])
    self.max_hp = random.randint(4,8)
    self.hp = self.max_hp

  def attack(self, hero):
    '''enemy attacks hero – randomize damage in the range 1-4. The hero should take the damage and the method should return a string representing the event. 
    
    Args:
      self (Enemy): assigns the method to the Enemy class
      hero (Hero): the hero that the enemy is atacking

    Returns:
      self.name + " attacks " + hero.name + " for " + str(dmg) + " damage." (string): a description of the attack of the form "Voldemort attacks Harry for 3 damage."
      '''
    dmg = random.randint(1,4)
    hero.take_damage(dmg)
    print()
    return self.name + " attacks " + hero.name + " for " + str(dmg) + " damage."