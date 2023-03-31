# 플레이어, 몬스터 정의 클래스 파일

import random
from time import sleep

# ========================== 플레이어 (직업) ==========================


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, magic_power, mp, exp, lv):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        self.point = 0
        self.exp = exp
        self.lv = lv

    # 공격 함수 - 플레이어의 일반공격과 몬스터의 공격에서 모두 사용
    def attack(self, other):
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

        if other.hp == 0:
            sleep(0.5)
            print(f"\n{other.name}이(가) 쓰러졌습니다.")

            self.exp += int(damage * 0.01)
            sleep(0.5)
            print(f"\n경험치 {int(damage * 0.01)} 증가!")

            if self.exp > 100:
                self.lv += 1
                sleep(0.5)
                print("레벨 1 증가")

                self.exp = self.exp - 100
                self.power += self.power*0.1  # 레벨업시 공격력, 최대 마력 ,최대 체력이 커지는 걸로
                self.max_hp += int(self.max_hp * 0.1)
                self.max_mp += int(self.max_mp * 0.1)

            elif self.exp < 100:
                self.lv = self.lv

        else:
            sleep(0.5)
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    # 상태창
    def show_status(self):
        sleep(0.5)
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")

    '''
    어차피 플레이어의 특수 공격 함수는 각 직업 클래스에 있기 때문에 이 함수는 필요 없습니다.
    참고가 될까 싶어 주석으로 남겨둡니다.
    
    def magic_attack(self,other):
        damage = random.randint(self.power * 0.8, self.power * 1.5)
        other.hp = max(other.hp - damage, 0)
        print(f"\033[38;2;161;196;255m\n .. 특수공격 | MP -50 | {other.name}에게 {damage}의 피해를 주었습니다!\033[0m")
        self.mp -= 50
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")   
    '''


# ---------- 직업 클래스 ----------

"""
마법사 클래스 : 체력 10000, 공격력 2000, 특수공격력 3000, 마력 400, 특수공격시 마력소모량 100
스킬 : 매직 익스플로전!!! >> 강한 공격
"""


class Wizard(Character):
    def __init__(self, name, hp, power, magic_power, mp, exp, lv):
        super().__init__(name, hp, power, magic_power, mp, exp, lv)

        self.job = '마법사'  # 콘솔 출력을 위한 문자열

    def attack(self, other):
        super().attack(other)  # 포인트를 제외한 부분은 부모 클래스의 attack 함수와 같음

        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

        self.point += round(damage*0.4)

        print(f"\n   포인트 +{round(damage*0.4)}")

        if other.hp == 0:
            sleep(0.5)
            print(f"\n{other.name}이(가) 쓰러졌습니다.")

            self.exp += int(damage * 0.01)
            sleep(0.5)
            print(f"경험치 {int(damage * 0.01)} 증가!")

            if self.exp > 100:
                self.lv += 1
                sleep(0.5)
                print("레벨 1 증가")

                self.exp = self.exp - 100
                self.power += self.power*0.1  # 레벨업시 공격력, 최대 마력 ,최대 체력이 커지는 걸로
                self.max_hp += int(self.max_hp * 0.1)
                self.max_mp += int(self.max_mp * 0.1)

            elif self.exp < 100:
                self.lv = self.lv

        else:
            sleep(0.5)
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")

    def magic_attack(self, other):  # 특수공격
        # 특수공격 데미지
        magic_damage = random.randint(
            self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)
        print(
            f"\033[38;2;161;196;255m\n .. 매직 익스플로전!!! | MP -100 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")

        self.mp -= 100  # mp 소모
        self.point += round(magic_damage*0.4)

        print(f"\n   포인트 +{round(magic_damage*0.4)}")

        if other.hp == 0:
            sleep(0.5)
            print(f"{other.name}이(가) 쓰러졌습니다.")

            self.exp += int(magic_damage * 0.01)
            sleep(0.5)
            print(f"경험치 {int(magic_damage * 0.01)} 증가!")

            if self.exp > 100:
                self.lv += 1
                sleep(0.5)
                print("레벨 1 증가")
                self.exp = self.exp - 100
                self.power += self.power*0.1
                self.max_hp += int(self.max_hp * 0.1)
                self.max_mp += int(self.max_mp * 0.1)

            elif self.exp < 100:
                self.lv = self.lv
        else:
            sleep(0.5)
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


"""
전사 클래스 : 체력 12000, 공격력 2500, 특수공격력 3000, 마력 250, 특수공격시 마력소모량 50
스킬 : 몸통박치기! >> 강한 공격
"""


class Warrier(Character):
    def __init__(self, name, hp, power, magic_power, mp, exp, lv):
        super().__init__(name, hp, power, magic_power, mp, exp, lv)

        self.job = '전사'  # 콘솔 출력을 위한 문자열

    def attack(self, other):
        super().attack(other)  # 포인트를 제외한 부분은 부모 클래스의 attack 함수와 같음

        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        self.point += round(damage*0.4)
        print(f"\n   포인트 +{round(damage*0.4)}")

    def magic_attack(self, other):
        magic_damage = random.randint(
            self.magic_power * 0.8, self.magic_power * 1.5)
        other.hp = max(other.hp - magic_damage, 0)

        print(
            f"\033[38;2;161;196;255m\n .. 몸통박치기! | MP -50 | {other.name}에게 {magic_damage}의 피해를 주었습니다!\033[0m")

        self.mp -= 70
        self.point += round(magic_damage*0.4)

        print(f"\n   포인트 +{round(magic_damage*0.4)}")

        if other.hp == 0:
            sleep(0.5)
            print(f"{other.name}이(가) 쓰러졌습니다.")

            self.exp += int(magic_damage * 0.01)
            sleep(0.5)
            print(f"경험치 {int(magic_damage * 0.1)} 증가!")

            if self.exp > 100:
                self.lv += 1
                sleep(0.5)
                print("레벨 1 증가")
                self.exp = self.exp - 100
                self.power += self.power*0.1
                self.max_hp += int(self.max_hp * 0.1)
                self.max_mp += int(self.max_mp * 0.1)

            elif self.exp < 100:
                self.lv = self.lv
        else:
            sleep(0.5)
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


"""
뱀파이어 클래스 : 체력 10000, 공격력 2000, 특수공격력 2000, 마력 250, 특수공격시 마력소모량 50
스킬 : 흡혈! >> 상대의 hp를 깎고 본인의 hp를 회복(hp소모량의 40%)
"""


class Vampire(Character):
    def __init__(self, name, hp, power, magic_power, mp, exp, lv):
        super().__init__(name, hp, power, magic_power, mp, exp, lv)

        self.job = '뱀파이어'  # 콘솔 출력을 위한 문자열

    def attack(self, other):
        super().attack(other)  # 포인트를 제외한 부분은 부모 클래스의 attack 함수와 같음

        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        self.point += round(damage*0.4)
        print(f"\n   포인트 +{round(damage*0.4)}")

    def magic_attack(self, other):
        # 특수공격 데미지
        magic_damage = random.randint(
            self.magic_power * 0.9, self.magic_power * 1.5)

        # 회복량 - 소모 체력에 비례
        heal_amount = int((self.max_hp-self.hp) * 0.4)

        other.hp = max(other.hp - magic_damage, 0)

        print(
            f"\033[38;2;161;196;255m\n .. 흡혈! | MP -50 | {other.name}에게 {magic_damage}의 피해를 주었습니다! \n .. 체력을 {heal_amount}만큼 회복했습니다.({self.hp}/{self.max_hp})\033[0m")

        self.hp += heal_amount  # 회복
        self.mp -= 70  # mp 소모
        self.point += round(magic_damage*0.4)
        print(f"\n   포인트 +{round(magic_damage*0.4)}")

        if other.hp == 0:
            sleep(0.5)
            print(f"{other.name}이(가) 쓰러졌습니다.")

            self.exp += int(magic_damage * 0.01)
            sleep(0.5)
            print(f"경험치 {int(magic_damage * 0.01)} 증가!")

            if self.exp > 100:
                self.lv += 1
                sleep(0.5)
                print("레벨 1 증가")
                self.exp = self.exp - 100
                self.power += self.power*0.1
                self.max_hp += int(self.max_hp * 0.1)
                self.max_mp += int(self.max_mp * 0.1)

            elif self.exp < 100:
                self.lv = self.lv

        else:
            sleep(0.5)
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


# ========================== 몬스터 ==========================
class Monster(Character):
    def __init__(self, name, hp, power, round):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.round = round

    def show_status(self):
        sleep(0.5)
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

    def wait(self):  # 회피함수
        sleep(0.5)
        print(f'\n\033[38;2;255;156;166m .. {self.name}의 공격이 빗나갔다!!\033[0m')
