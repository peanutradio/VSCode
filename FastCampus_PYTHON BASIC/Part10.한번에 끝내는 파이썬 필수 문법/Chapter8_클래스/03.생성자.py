# 상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해 사용.

# 부모 클래스
class Monster:
    def __init__(self, health, attack, speed):  # self = 인스턴스 # 그외: 매개변수
        self.health = health   # 인스턴스의 health 
        self.attack = attack   # 인스턴스의 attack
        self.speed = speed     # 인스턴스의 speed
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)  #
goblin.decrease_health(100)
print(goblin.get_health())

#늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
wolf.decrease_health(1000)
print(wolf.get_health())