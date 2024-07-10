''' Game in which a user must nagivate a maze of monsters to find the exit and escape.

Written by: Olivia Fishbough and Analicia Sosa

Functions:
  Main – prompt the user to enter their name, then construct the hero and a map object.  Create a loop that repeats until the hero dies, the hero finds the finish, or the user quits the game.  Present a menu that allows the user to choose a direction to move in (north, south, east, west), move the hero in that direction, reveal that spot,  and then present the encounter at that location as follows: 
    a. ‘m’ – monster – construct an enemy and display its information.  Create a loop that allows the user to either attack or run away.  If they attack, the hero attacks the monster, and if the monster has hp left, then the monster attacks back.  If the monster is dead, then display a message and remove the ‘m’ from the map.  If the user chooses to run away, then choose a random direction to run in (reveal but don’t present the encounter for the new location) (‘m’ should remain on the map). 
    b. ‘x’ – invalid direction – display a message stating that they cannot move that direction. 
    c. ‘n’ – nothing – display a message stating that this room is empty. 
    d. ‘s’ – start – display a message that they wound up back at the start of the dungeon. 
    e. ‘i' – item room – display a message stating that they found a health potion.  Heal the hero and remove the ‘i' from the map so they can’t get it again (not required, but you can add a check to see if the hero has full hp, if they do, then you can leave the ‘i' on the map to save it for later). 
    f. ‘f’ – finish – display a congratulatory message stating that they found the way out of the maze and won the game. 

Usage: Run the main() function

Example Usage:

	main()

''' 

# import statements
import hero
import check_input
import map
import enemy
import random

def main():
  ''' Prompt the user to enter their name, then construct the hero and a map object.  Create a loop that repeats until the hero dies, the hero finds the finish, or the user quits the game.  Present a menu that allows the user to choose a direction to move in (north, south, east, west), move the hero in that direction, reveal that spot,  and then present the encounter at that location.

  Args:
    none

  Returns:
    None
  
  '''
  # constants
  menu = "1. Go North \n2. Go South \n3. Go East \n4. Go West \n5. Quit \n\nEnter choice: "

  # set up the game
  board = map.Map()
  name = input("What is your name, traveler?\n")
  player = hero.Hero(name, 15)
  board.reveal(player.location)
  space = 'o'

  # loops until player dies, quits, or wins
  while True:
    # if the player dies
    if player.hp == 0:
      print("\nThe valient traveler, ", player.name, ", was slain by the monsters in this maze.")
      return

    # gets user input given the menu
    print()
    print(player)
    print(board.show_map(player.location))
    choice = check_input.get_int_range(menu, 1, 5)
    if choice == 1:
      space = player.go_north()
    elif choice == 2:
      space = player.go_south()
    elif choice == 3:
      space = player.go_east()
    elif choice == 4:
      space = player.go_west()
    else:
      print("\nThe hero decides to evacuate, to tackle the maze at a later date...")
      return

    # if invalid direction, prompt again
    if space == 'x':
      print("You cannot go that way...")
      pass

    # update board with player's location
    board.reveal(player.location)
    space = board[player.location[1]][player.location[0]]

    # if there's a monster, give the user the choice to fight or flee
    if space == 'm':
      monster = enemy.Enemy()
      print("\nYou encounter " + str(monster))
      print("1. Run away\n2. Attack " + monster.name)
      while player.hp > 0:
        if check_input.get_int_range("\nEnter choice: ", 1, 2) == 1:
          # continues generating random directions until a valid one is selected
          direction = 'x'
          while direction == 'x': 
            number = random.randint(0,3)
            if number == 0:
              direction = player.go_north()
            elif number == 1:
              direction = player.go_south()
            elif number == 2:
              direction = player.go_east()
            else:
              direction = player.go_west()
          board.reveal(player.location)
          break
        # else user choice is to fight
        print(player.attack(monster))
        # if monster is dead
        if monster.hp <= 0:
          print("You have slain " + monster.name)
          board.remove_at_loc(player.location)
          break
        print(monster.attack(player))

    # if this is the starting space
    elif space == 's':
      print("\nThis is where your journey started! If you leave now your trip will have been wasted!\n")

    # if this is the finish
    elif space == 'f':
      print("\n Congratulations! You found the exit, ", player.name, "!")
      return

    # if there's a healing elixir, restore health and remove it from the board
    elif space == 'i':
      print("\nYou found a Health Potion!  You drink it to restore your health.\n")
      player.hp = player.max_hp
      board.remove_at_loc(player.location)

    # if there's nothing
    elif space == 'n':
      print("\nThere is nothing here... \n")

main()