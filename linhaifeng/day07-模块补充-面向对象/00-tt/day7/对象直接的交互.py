class Garen:
    camp='Demacia'
    def __init__(self,nickname,life_value=100,aggresivity=80):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity

class Riven:
    camp = 'Noxus'
    def __init__(self, nickname, life_value=80, aggresivity=100):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


g1=Garen('草丛猥琐男')
r1=Riven('兔女郎')

print(r1.life_value)
g1.attack(r1)
print(r1.life_value)






