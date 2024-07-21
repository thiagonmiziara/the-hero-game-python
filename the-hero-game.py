# character: class player
# Hero: user controlled
# Enemy: user opponent

class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level
        
    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
      
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"\nName: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"  
      
class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_skill()}\n"  


class Enemy(Character):
    def __init__(self, name, life, level, kind):
        super().__init__(name, life, level)
        self.__kind = kind
    
    def get_kind(self):
        return self.__kind
      
    def show_details(self):
        return f"{super().show_details()}\nKind: {self.get_kind()}\n"
      
class Game:
    """ the game's orchestrator class """   
    def __init__(self):
        self.hero = Hero(name="Batman", life=100, level=5, skill="fly")
        self.enemy = Enemy(name="Joker", life=80, level=5, kind="Villain")
    
    def start_game(self):
        """ the game's start method """
        print("Welcome to the Hero Game")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nShwowing details")
            print(f"\n{self.hero.show_details()}")
            print(f"{self.enemy.show_details()}")
           
            input("Press Enter to continue attack...")
            choice = input("Choose your attack: (1) Attack (2) Especial Attack: ")
        
        
# Create game instance and start game 
game = Game()
game.start_game()
