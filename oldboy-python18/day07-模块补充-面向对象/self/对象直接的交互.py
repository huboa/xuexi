class Garen:
    camp='Demacia'
    def __init__(self,nickname,life_value=100,aggresivity=20):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value -= self.aggresivity
class Riven:
    def __init__(self, nickname, life_value=80, aggresivity=100):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity

g1=Garen('boy')
r1=Riven('girl')
print(r1.life_value)
g1.attack(r1)
print(r1.life_value)
