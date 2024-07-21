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
    
    def take_damage(self, damage):
        self.__life -= damage
        if self.__life <= 0:
            self.__life = 0
            print("===============================================================================")
            print(f"\n{self.get_name()} has been defeated! :(\n")
            print("===============================================================================")
            
    def attack(self, target):
        damage = self.__level * 2
        target.take_damage(damage)
        print("===============================================================================")
        print(f"\n{self.get_name()} attacks {target.get_name()} with {damage} points of damage!\n")
        print("===============================================================================")
        
class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_skill()}\n"  

    def especial_attack(self, target):
        damage = self.get_level() * 5
        target.take_damage(damage)
        print("===============================================================================")
        print(f"\n{self.get_name()} used *{self.get_skill()}* in {target.get_name()} with {damage} points of damage!\n")
        print("===============================================================================")

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
        self.hero = Hero(name="Batman", life=100, level=5, skill="Bat-rang")
        self.enemy = Enemy(name="Joker", life=80, level=5, kind="Villain")
    
    def start_game(self):
        """ the game's start method """
        print("Welcome to the Hero Game")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nShwowing details")
            print("---------------------------------------")
            print("**Hero**")
            print(f"{self.hero.show_details()}")
            print("---------------------------------------")
            print("**Enemy**")
            print(f"{self.enemy.show_details()}")
            print("---------------------------------------\n")
           
            input("Press Enter to continue attack...")
            print("||||||||||||||||||||||||||||||||||||||||||\n")
            choice = input("Choose your attack: (1) Attack (2) Especial Attack: ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.especial_attack(self.enemy)
            else:
                print("Void choice, choose again.")

            if self.enemy.get_life() > 0:
                # Enemy's turn
                self.enemy.attack(self.hero)
            
        if self.hero.get_life() > 0:
            print("**************************************\n")
            print(f"{self.hero.get_name()} wins the game!\n")
            print("**************************************")
        else:
            print("***************************************\n")
            print(f"{self.enemy.get_name()} wins the game!\n")
            print("***************************************")
# Create game instance and start game 
game = Game()
game.start_game()
