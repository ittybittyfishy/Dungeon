''' An abstract class that describes a character in the game. 

Written by: Olivia Fishbough and Analicia Sosa

Functions:
  __init__(self, name, max_hp) – initializes each of the instance variables 
  take_damage(self, dmg) – subtracts the dmg from the hp, but does not allow the hp to drop below 0. 
  heal(self) – restores the entity’s hp to max_hp 
  __str__(self) – returns a string in the format ‘Name\nHP: hp/max_hp’. 
  attack(self, entity) – abstract method (no code) that all entity subclasses will override to attack and do damage to the opposing entity

Usage: Import the entity class. Create another class that extends it. Override its abstract methods.

Example Usage:

  import entity

  class Hero(entity.Entity):
    def __init__(self, name, max_hp):
      super().__init__(name, max_hp)
      self._loc = [0,0]

'''

# import statements
import abc

class Entity(abc.ABC):

  def __init__(self, name, max_hp):
    ''' Constructor initializes each of the instance variables 

    Args:
      self (Entity): assigns the method to the entity class
      name (string): the entity's name
      max_hp (int):  the entity's max hp, to which hp is initially set

    Returns: 
      None.
    '''
    self.name = name
    self.hp = max_hp
    self.max_hp = max_hp

  def take_damage(self, dmg):
    ''' Subtracts the dmg from the hp, but does not allow the hp to drop below 0. 

    Args:
      self (Entity): assigns the method to the entity class
      dmg (int): the amount of damage to be taken

    Returns:
      None.
    '''
    self.hp -= dmg
    # prevents hp from going under 0
    if self.hp < 0:
      self.hp = 0

  def heal(self):
    ''' Restores the entity’s hp to max_hp

    Args:
      self (Entity): assigns the method to the entity class

    Returns:
      None.
    '''
    self.hp = self.max_hp

  def __str__(self):
    ''' Returns a string in the format ‘Name\nHP: hp/max_hp’. 

    Args:
      self (Entity): assigns the method to the entity class
    
    Returns:
      self.name + "\nHP: " + str(self.hp) + " / " + str(self.max_hp) + "\n" (string): of the form: 
        Name
        Hp: hp/max_hp
    '''
    return self.name + "\nHP: " + str(self.hp) + " / " + str(self.max_hp) + "\n"

  @abc.abstractmethod
  def attack(self, entity):
    ''' abstract method that all entity subclasses will override to attack and do damage to the opposing entity

    Args:
      self (Entity): assigns the method to the entity class
      entity (Entity): the entity to be attacked

    Returns:
      None. 
    '''
    pass