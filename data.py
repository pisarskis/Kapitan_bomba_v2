import random


class Ships:
    def __init__(self, ships, user_choice, items):
        self.ships = ships
        self.user_choice = user_choice
        self.ship_choice = 0
        self.items = items
        self.hp = ships[self.ship_choice][0]
        self.hp_max = ships[self.ship_choice][0]
        self.sh = ships[self.ship_choice][1]
        self.sh_max = ships[self.ship_choice][1]
        self.dmg_low = ships[self.ship_choice][2] - 5
        self.dmg_high = ships[self.ship_choice][2] + 5
        self.name = ships[self.ship_choice][3]
        self.desc = ships[self.ship_choice][4]
        self.cost = ships[self.ship_choice][5]
        self.res = 0

    def ship_stats(self):
        stats = (self.hp, self.hp_max, self.sh, self.sh_max, self.ship_choice, self.name, self.desc, self.res, self.name,
                 self.desc, self.cost)
        return stats

    def ship_choice(self, new_ship):
        self.ship_choice = new_ship

    def calc_dmg(self):
        return random.randint(self.dmg_low, self.dmg_high)

    def get_damage(self, dmg):
        if dmg <= self.sh:
            self.sh -= dmg
        elif dmg > self.sh:
            rest = self.sh - dmg
            self.sh = 0
            self.hp += rest
        elif self.sh == 0 and self.hp > 0:
            self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def sh_self_restore(self):
        self.sh += 10

    def stats_restore(self, choice):
        if choice == 0 or choice == 1:
            hp_heal = self.items[choice][0]
            self.hp += hp_heal
            return hp_heal, self.items[choice][1]
        else:
            sh_heal = self.items[choice][0]
            self.sh += sh_heal
            return sh_heal, self.items[choice][1]

    def get_items(self):
        count = 1
        for item in self.items:
            count += 1
            return count, item

    def res_up(self, res):
        self.res += res


class Planets_data:
    def __init__(self, planet_list, planet_no):
        self.planet_list = planet_list
        self.planet_name = planet_list[planet_no][0]
        self.planet_pop = planet_list[planet_no][1]
        self.planet_hp = planet_list[planet_no][2]
        self.planet_sh = planet_list[planet_no][3]
        self.planet_atk = planet_list[planet_no][4]
        self.planet_atk_low = planet_list[planet_no][4] - 5
        self.planet_atk_high = planet_list[planet_no][4] + 5
        self.planet_res = planet_list[planet_no][5]
        self.planet_res_max = planet_list[planet_no][5]
        self.actions = ["Atakuj", "Odlec", "Handluj"]

    def planet_stats(self):
        planet_stats = (self.planet_name, self.planet_pop, self.planet_hp, self.planet_sh, self.planet_atk,
                        self.planet_res, self.planet_res_max)
        return planet_stats

    def planet_attack(self):
        return random.randint(self.planet_atk_low, self.planet_atk_high)

    def planet_sacked(self):
        self.planet_res = 0
        return self.planet_res, self.planet_res_max

    def planet_res_up(self):
        if self.planet_res < self.planet_res_max:
            self.planet_res += 10
            if self.planet_res >= self.planet_res_max:
                self.planet_res = self.planet_res_max
        return self.planet_res, self.planet_res_max

    def planet_action_choice(self):
        c_i = 1
        print("\nACTIONS")
        for item in self.actions:
            print("     " + str(c_i) + ".", item)
            c_i += 1

    def planet_get_dmg(self, dmg):
        self.planet_hp -= dmg
        if self.planet_hp <= 0:
            self.planet_hp = 0
            print("Zniszczyłeś obronę planety oraz ukradłeś ", self.planet_res, " zasobów. Co teraz chcesz zrobić?")
