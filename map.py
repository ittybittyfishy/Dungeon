''' Map – singleton – the map of the dungeon maze. 

Written by: Olivia Fishbough and Analicia Sosa

Functions:
  __new__(cls) – if the map hasn’t been constructed, then construct it and store it in the instance class variable and return it.  If it has, then just return the instance. 
  __init__(self) – create and fill the 2D map list from the file contents.  Create and fill the 2D revealed list with all False values.  The map stores the contents of the file and the revealed list is used to determine whether the contents of the map are displayed or not (‘x’ if not displayed). 
  __getitem__(self, row) – overloaded [] operator – returns the specified row from the map.  (Note: this operator can be used to access a row (ex. m[r]) or can be used to access a value at a row and column (ex. m[r][c]). 
  __len__(self) – returns the number of rows in the map list.  (Note: if you want to know the number of rows, use len(m), if you need the number of columns, use len(m[r])). 
  show_map(self, loc) – returns the map as a string in the format of a 5x5 matrix of characters where revealed locations are the characters from the map, unrevealed locations are ‘x’s, and the hero’s location is a ‘*’. 
  reveal(self, loc) – sets the value in the 2D revealed list at the specified location to True. 
  remove_at_loc(self, loc) – overwrites the character in the map list at the specified location with an ‘n’.

Usage: Import the map class. Create an instance of map. Use its functions to allow the player to interact with the map and discover it as they travel.

Example Usage:

  import map

  map.reveal([0,0])
  print(map.show([0,0])
  if map[3][4] == 'm'
    map.remove([3, 4])

'''


class Map():
  _instance = None
  _initialized = False

  def __new__(cls):
    ''' If the map has yet to be constructed, this constructs it and returns it
    Args: 
      cls (new constructor): allows the map to be constructed
    Returns:
      cls._instance (Constructed map): stores the constructed map
    '''
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__ (self):
    ''' Constructs a 2D list of the information in a text file 
    
    Args: 
      self (Map): Assigns the method to the Map class 
      
    Returns: 
      None
    '''
    # initiallizes
    if not Map._initialized:
      self._file = open("map.txt","r")
      self._initialized = True
      self._map = []
      # turns it into 2D list
      for row in self._file:
        holder = []
        for item in row:
          if item != ' ' and item != '\n':
            holder.append(item)
        self._map.append(holder)
      
      # the revealed 2d list of x's
      self._revealed = [[False for x in range(len(self._map[0]))]for y in range(len(self._map))]

  def __getitem__(self, row):
    ''' Oversides the [] operator to allow up to acces the location on the map, m[r] accesses the row and m[r][c] allows access to the column
    Args:
      self (Map): makes it a method of the Map Class 
      row (int): specified row (or coloumn) from the map

    Returns: 
    self._map[row] (int): value at specifed row/col
    '''
    return self._map[row]

  def __len__(self):
    ''' Returns the number of rows on the map
    Args:
      self (Map): makes it a method of the Map class

    Returns: 
      len(self._map) (int): number of rows in the map
    
    '''
    return len(self._map)

  def show_map(self, loc):
    ''' Returns the contructed map as a string in a 5 by 5 matrix grid. Revealed locations show to character from the map while unrevealed locations are marked with the character 'x' and the players position with a '*'

    Args:
      self (Map): assigns the method to the map class
      loc (tuple): the x and y coordinates where the player is

    Returns:
      mapString (string): a string of the form "snnmx\nxnx*\nxxxxx\nxxxxx\nxxxxx"
    '''
    mapString = ""
    # iterate through the 2D list
    for x in range(len(self._map)):
      for y in range(len(self._map[0])):
        # if this location is where the player is
        if loc == [y,x]:
          mapString += '*'
        # if it should be revealed
        elif self._revealed[x][y] == True:
          mapString += self._map[x][y]
        # else it is still unknown
        else:
          mapString += 'x'
      mapString += "\n"
    return mapString

  def reveal(self, loc):
    ''' Sets the value in the 2D revealed list at the specified location to True. 

    Args:
      self (Map): assigns the method to the map class
      loc (tuple): the x and y coordinates of the location which is to be revealed

    Returns:
      None. Modifies self._revealed directly.    
    '''
    self._revealed[loc[1]][loc[0]] = True

  def remove_at_loc(self, loc):
    ''' Overwrites the character in the map list at the specified location with an ‘n’.

    Args:
      self (Map): assigns the method to the map class
      loc (tuple): the x and y coordinates of the location which is to be reset

    Returns: 
      None. Modifies self._map directly.
    
    '''
    self._map[loc[1]][loc[0]] = 'n'