''' Hero – extends entity - the user’s character in the maze game.

Written by: Olivia Fishbough and Analicia Sosa

Functions:
  __init__(self, name) – initializes the name and max_hp using super, sets the  hero’s starting location to row=0, col=0. 
  attack(self, entity) – hero attacks the enemy – randomize damage in the range 2-5, the enemy should take the damage and the method should return a string representing the event. 
  go_north/south/east/west(self) – update the hero’s location by adding or subtracting 1 to the row or column, but only if that location is within the bounds of the map (between 0 and the len(map)-1).  If it is, return the character at that location, if it isn’t, return an ‘x’ to signify that the direction is out of bounds. 

Usage: Import the hero class. Create an instance of hero and move around the map. Attack and be attacked by monsters

Example Usage:

  import hero

  player = hero.Hero("Samuel", 25)
  player.go_east()
  player.attack(monster)
  monster.attack(player)

'''

import entity
import random
import map

board = map.Map()

class Hero(entity.Entity):
  
  def __init__(self, name, max_hp):
    ''' Initializes the name and max_hp using super, sets the  hero’s starting location to row=0, col=0. 

    Args:
      self (Hero): assigns the method to the hero class
      name (string): the hero's name
      max_hp (int): the hero's maximum health points

    Returns:
      None. 
    '''
    super().__init__(name, max_hp)
    self._loc = [0,0]

  @property
  def location(self):
    '''Property accesses the hero's location

    Args: 
      self (Hero): assigns the method to the hero class

    Returns:
      self._loc (Tuple): 
    '''
    return self._loc
    
  def attack(self, entity):
    ''' Hero attacks the enemy – randomize damage in the range 2-5, the enemy should take the damage and the method should return a string representing the event. 

    Args:
      self (Hero): assigns the method to the hero function
      entity (Entity): the entity that the hero is attacking

    Returns: 
      self.name + " attacks " + entity.name + " for " + str(dmg) + " damage." (string): a description of the attack in the form:
        Hero attacks Enemy for 5 damage.
    '''
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    print()
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."

  def go_north(self):
    ''' Moves the hero one location upwards if that is a valid direction. Else returns 'x'
    
    Args:
      self (Hero): assigns the method to the hero class

    Returns: 
      'x' (char): if moving this direction would put the player out of bounds
    '''
    if self._loc[1] <= 0:
      return 'x'
    self._loc[1] -= 1

  def go_south(self):
    ''' Moves the hero one location downwards if that is a valid direction. Else returns 'x'
    
    Args:
      self (Hero): assigns the method to the hero class

    Returns: 
      'x' (char): if moving this direction would put the player out of bounds
    '''
    if self._loc[1] >= len(board) - 1:
      return 'x'
    self._loc[1] += 1
  
  def go_east(self):
    ''' Moves the hero one location rightwards if that is a valid direction. Else returns 'x'
    
    Args:
      self (Hero): assigns the method to the hero class

    Returns: 
      'x' (char): if moving this direction would put the player out of bounds
    '''
    if self._loc[0] >= len(board[0]) - 1:
      return 'x'
    self._loc[0] += 1

  def go_west(self):
    ''' Moves the hero one location leftwards if that is a valid direction. Else returns 'x'
    
    Args:
      self (Hero): assigns the method to the hero class

    Returns: 
      'x' (char): if moving this direction would put the player out of bounds
    '''
    if self._loc[0] <= 0:
      return 'x'
    self._loc[0] -= 1
