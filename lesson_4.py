from random import randint, choice, random


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        hero: Hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss: Boss):
        boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss: Boss, heroes: list):
        crit = randint(2, 5) * self.damage
        boss.health -= crit
        print(f'Warrior {self.name} hit critically {crit}')


class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, damage=0, ability='REVIVE') # Урон 0 - он/она не атакует
        self.has_revived = False # может оживить только один раз
    def attack(self, boss: Boss):
        pass

    def apply_super_power(self, boss: Boss, heroes, dead_heroes, round_number: list):
        if not self.has_revived and dead_heroes:
           hero_to_revive = dead_heroes[0]
        if hero_to_revive <= 0:
            print(f"{self.name} жертвует собой ради {hero_to_revive.name}!")
            hero_to_revive.hp = 100
            self.hp = 0 # сам/сама умирает
            self.has_revived = True
            dead_heroes.remove(hero_to_revive)
        dead_heroes = []
        for hero in heroes:
            if hero.health <= 0 and hero not in dead_heroes:
                dead_heroes.append(hero)

class Magic(Hero):
    def __init__(self, name, health, damage, boost_amount):
        super().__init__(name, health, damage, 'BOOST')
        self.boost_amount = boost_amount

    def apply_super_power(self, boss: Boss, heroes, *args: list):
        if round_number <= 4:
            print(f"{self.name} усиливает атаку всех героев на {self.boost_amount}!")
            for hero in heroes:
               if hero.health > 0 and hero is not self:
                   hero.damage += self.boost_amount


class Hacker(Hero):
    def __init__(self, name, health, damage, steal_amount):
        super().__init__(name, health, damage)

    def apply_super_power(self, boss: Boss, heroes, round_number, *args: list):
        if round_number % 2 == 0 and self.hp > 0 and boss.health > 0:
            boss.health -= self.steal_amount
            if boss.health < 0:
                boss.health = 0

                alive_heroes = [hero for hero in heroes if hero.health > 0 and hero is not self]
                if alive_heroes:
                    chosen_hero = random.choice(alive_heroes)
                    chosen_hero.health += self.steal_amount

                    print(f"{self.name} украл {self.steal_amount} Health у босса и передал {chosen_hero.name}.")

class Druid(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, ability='SUMMON')
        self.helper_summoned = False

    def apply_super_power(self, boss: Boss, heroes: list):
        if not self.helper_summoned:
            self.helper_summoned = True
            choice = random.choice(["angel", "crow"])

            if choice == "angel":
                print("Druid призвал ангела! Healer лечит сильнее.")
                for hero in heroes:
                    if isinstance(hero, Healer):
                        hero.heal_bonus += 20
                    elif choice == "crow":
                        if boss.health < boss.max_health / 2:
                            print("Druid призвал ворона! Босс стал агрессивнее.")
                            boss.damage = int(boss.damage * 1.5)

class Healer(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage} damage to boss.')

class Samurai(Hero):
    def __init__(self, name, health, damage, shuriken_power):
        super().__init__(name, health, damage, ability='SHURIKEN')
        self.shuriken_power = shuriken_power

    def apply_super_power(self, boss: Boss, heroes: list):
        shuriken_type = random.choice(["virus", "vaccine"])

        if shuriken_type == "virus":
            print(f"Samurai кидает вирус-шурикен! Босс теряет {self.shuriken_power} Health.")
            boss.take_damage(self.shuriken_power)
        else:
            print(f"Samurai кидает вакцину-шурикен! Босс восстанавливает {self.shuriken_power} Health.")
            boss.health += self.shuriken_power
            if boss.health > boss.max_health:
                boss.health = boss.max_health


round_number = 0




def play_round(boss: Boss, heroes: list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss: Boss, heroes: list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def start_game():
    boss = Boss('Fuse', 1000, 50)

    warrior_1 = Warrior('Anton', 280, 10)
    warrior_2 = Warrior('Akakii', 270, 15)
    magic = Magic('Itachi', 290, 10, 10)
    doc = Healer('Aibolit', 250, 5, 15)
    assistant = Healer('Dulittle', 300, 5, 5)
    berserk = Berserk('Guts', 260, 10)
    witcher = Witcher("Morgana", 230)
    druid = Druid("Malfurion", 248, 7)
    samurai = Samurai("Jack", 239, 11, 8)
    hacker = Hacker("Zero", 220, 8, 10)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def show_statistics(boss: Boss, heroes: list):
    print(f'ROUND {round_number} -----------------')
    print(boss)
    for hero in heroes:
        print(hero)


start_game()
