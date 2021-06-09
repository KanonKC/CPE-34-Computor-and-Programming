import numpy as np

# print(np.random.RandomState(1).randint(1, 40))

X = np.random.RandomState(1)

#print(X.randint(1,40))

class Prince:
    def __init__(self,hp,atk):
        self.maxHp = hp
        self.hp = hp
        self.atk = atk

    def hpLeft(self):
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def attack(self,ene):
        ene.hp -= self.atk
        self.atk += 2

    def heal(self):
        self.hp += 20
        self.atk = 10
        if self.hp > self.maxHp:
            self.hp = self.maxHp

class Monster:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    def hpLeft(self):
        if self.hp < 0:
            self.hp = 0
        return self.hp
        
    def attack(self,ene):
        self.atk = X.randint(1,40)
        ene.hp -= self.atk


shp = int(input("Blood Start: "))
p = Prince(shp,10)
m = Monster(shp,0)

while True:
    end = False # TURN COUNTER

    # YOUR TURN
    act = input("Attack(a) or Heal(h): ")
    if act == "a":
        end = True
        p.attack(m)
        print(f"Monster's HP left {m.hpLeft()}")
        if m.hpLeft() == 0:
            print("You win.(^_^)")
            break
    elif act == "h":
        end = True
        p.heal()
        print(f"Your HP left {p.hpLeft()}")

    # MONSTER TURN
    if end:
        m.attack(p)
        print(f"Monster's turn : Your HP left {p.hpLeft()}")
        if p.hpLeft() == 0:
            print("You lose and die.(T_T)")
            break
