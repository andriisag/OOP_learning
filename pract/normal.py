from multiprocessing.resource_sharer import stop


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

class Player(Person):
    def count(self):
             self.health -= self.damage - self.armor

    def win(self):
        if self.health < 0:
           return True         
        else:
          return  False

class Enemy(Person):
    def count(self):
            self.health -= self.damage - self.armor

    def win(self):
        if self.health < 0:
          return  True        
        else:
          return  False

player = Player(100, 50, 40)
enemy = Enemy(100, 50, 30)

class Atack:
    def fight():
        if player.win() == True:
            print("Enemy won")
        elif enemy.win() == True:
            print("Player won")             
        else:
            return True
    def game():
        a = atack.fight()
        if a == True:
            player.count()
            enemy.count()
            return True
        else:
            return a   
     
atack = Atack

a = atack.game()

while a == True:
    a = atack.game()

print(a)