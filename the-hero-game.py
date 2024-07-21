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
      
hero = Hero(name="Batman", life=100, level=5, skill="fly")
print(hero.show_details())

enemy = Enemy(name="Joker", life=80, level=5, kind="Villain")
print(enemy.show_details())