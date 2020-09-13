#Pokemon class

#self is a reference to the current instance of the class, used to access variables that belongs to the class.
class Pokemon:
  def __init__(self, name, level, type):
    self.name = name
    self.level = level
    self.type = type
    self.knocked_out = False
    self.max_health = self.level
    self.health = self.max_health
    self.xp = 0
    
  
  def __repr__(self):
    return "Pokemon: {}, current level: {}, type: {}, current health: {}.\n".format(self.name, self.level, self.type, self.health)
  
  def lose_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      self.knock_out()
  
  def gain_health(self, gained_value):
    self.health += gained_value
    print("{} gained {} health".format(self.name, gained_value))
    print("{}'s health: {}".format(self.name, self.health))
  
  def knock_out(self):
    #checking that health is 0
    if self.health != 0:
      self.health = 0
      self.knocked_out = True
      print("{name} is knocked out!".format(name = self.name))
   
  
  def revive(self):
    if self.knocked_out:
      self.knocked_out = False
      self.health = 3
      print("{name} has been revived with {health} health!".format(name = self.name, health = self.health))
    else:
      print("{name} is not knocked out.".format(name = self.name))
  

  #attack method (damage is equal to twice pokemon level if advantage and half the level if disadvantage)
  def attack(self, other):
    #check if pokemon is knocked out
    if self.knocked_out == True:
      print("{pokemon} is knocked out!, You cannot fight, you must revive!".format(pokemon = self.name))
    #check fire
    if self.type == 'Fire' and other.type == 'Grass' or other.type == 'Electric':
        other.lose_health(self.level * 2)
    else:
        other.lose_health(self.level / 2)
    #check water
    if self.type == 'Water' and other.type == 'Fire' or other.type == 'Electric':
        other.lose_health(self.level * 2)
    else:
        other.lose_health(self.level / 2)
    #check grass
    if self.type == 'Grass' and other.type == 'Fire' or other.type == 'Electric':
        other.lose_health(self.level / 2)
    else:
        other.lose_health(self.level * 2)
    #check electric
    if self.type == 'Electric' and other.type == 'Fire' or other.type == 'Water':
        other.lose_health(self.level / 2)
    else:
        other.lose_health(self.level * 2)
    print("{name} attacked {other}".format(name = self.name, other = other.name))
    print("{other} health is now {health}.".format(other = other.name, health = other.health))
    #gain XP 
    self.gain_xp(1)
  

  #gain xp method
  def gain_xp(self, xp_value):
    self.xp += xp_value
    print("{} gained {} xp.\n".format(self.name, xp_value))
    if self.xp >= 5:
      self.gain_level()
  

  #pokemon level increase method
  def gain_level(self):
    #set experience back to 0
    self.exp = 0
    #increase level of Pokemon
    self.level += 1
    #setting health to max
    self.health = self.max_health
    print("{} leveled up to level {}! Max health reset {}.\n".format(self.name, self.level, self.max_health))
    #evolve pokemon if over level 15
    if self.level >= 15:
      self.name = 'Super ' + self.name
    else:
      self.name = self.name
      
    

    

#Trainer Class
class Trainer:
  def __init__(self, name, pokemons, potions, current_pokemon):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon
    
  
  def __repr__(self):
    return "Trainer info. {name}, has pokemons: {pokemons}, has {potions} potions, current pokemon is {current_pokemon}.".format(name = self.name, pokemons = self.pokemons, potions = self.potions, current_pokemon = self.current_pokemon)
  
#use potion 
  def use_potion(self):
    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
        self.current_pokemon.gain_health(1)
        self.potions -= 1
        print("{} has {} potions left.\n".format(self.name, self.potions))
      else:
        print("{} failed to use a potion on {}. Your pokemon has maximum health.\n".format(self.name, self.current_pokemon.name))
    else:
      print("{}, you have no potions!\n".format(self.name))
  


#attack other pokemon
  def attack_other(self, other):
    self.current_pokemon.attack(other.current_pokemon)
   


#switch pokemon
  def switch_pokemon(self, pokemon):
    if pokemon.knocked_out == True:
      print("This Pokemon is knocked out! You cannot swap out")
    elif pokemon in self.pokemons:
      self.current_pokemon = pokemon
      print("{} switched in a new pokemon! {}'s current pokemon now is {}.\n".format(self.name, self.name, self.current_pokemon.name))




#Inherit from Pokemon class - subclass
class Charmander(Pokemon):
  def __init__(self, name, level, type):
    super().__init__(name, level, type)
  
  def obliterate(self, other):
    #full health lost for attack
    other.lose_health(other.health)
    print("{} obliterated {}!".format(self.name, other.name))



#play game - (instances of pokemon class)

bulbasaur = Pokemon("Bulbasaur", 10, 'Grass')
pikachu = Pokemon("Pikachu", 10, 'Electric')
magneto = Pokemon("Magneto", 10, 'Electric')
firefox = Pokemon("Firefox", 10, 'Fire')
whirlpool = Pokemon("Whirlpool", 10, 'Water')
squirtle = Pokemon("Squirtle", 10, 'Water')
charmander = Charmander("Charmander", 10, 'Fire')


#trainers (name, list of pokemon, potions, currentP)

george = Trainer('George', [squirtle, charmander], 4, squirtle)
tom = Trainer('Tom', [pikachu, whirlpool], 3, pikachu)
sally = Trainer('Sally', [bulbasaur, squirtle, magneto], 5, bulbasaur)


 
print(charmander)


#firefox.gain_xp(5)
whirlpool.gain_level()

firefox.attack(whirlpool)

magneto.attack(bulbasaur)
#george.attack_other(tom)
tom.switch_pokemon(pikachu)

