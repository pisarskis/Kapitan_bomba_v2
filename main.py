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


moving = []
moving_x = 0
correct_move = "asdw"
planet_positions = []
planet_positions_det = {}  # slownik zawierajacy pelne parametry planety w formacie 0 : (x, y, z)
planet_position_temp = {}  # slownik umozliwiajacy polaczenie pozycji palnety miedzy zmiennymi z gry a obiektowka
# format (0: x) gdzie x to pozycja planety wygenerowana na mape np 37
planet_positions_det_count = 0
planet_positions_temp_count = 0
planet_names = ("ziemia1", "ziemia2", "ziemia3", "ziemia4", "ziemia5", "ziemia6", "ziemia7")

orzel1 = (100, 200, 200, "Orzel1", "Opis1", 100)
orzel2 = (150, 300, 30, "Orzel2", "Opis2", 100)
orzel3 = (200, 400, 40, "Orzel3", "Opis3", 100)
lomot1 = (300, 500, 50, "Lomot1", "Opis4", 100)
lomot2 = (400, 600, 70, "Lomot2", "Opis5", 100)
ships = [orzel1, orzel2, orzel3, lomot1, lomot2]

hp_rec = (50, "Zestaw naprawczy")
hp_rec_big = (100, "Duzy zestaw naprawczy")
sh_rec = (100, "Shield booster")
sh_rec_big = (200, "Duży shield booster")
items = [hp_rec, hp_rec_big, sh_rec, sh_rec_big]

player = Ships(ships,  0, items)


def genarate_planet():
    planet_list =[]
    for planet in planet_names:
        planet_pop = random.randint(0, 90000)
        planet_hp = random.randint(int(planet_pop * 0.005), int(planet_pop * 0.015))
        planet_sh = random.randint(int(planet_hp * 1.2), int(planet_hp * 1.5))
        planet_atk = random.randint(int(planet_hp * 0.07), int(planet_hp * 0.11))
        planet_res = random.randint(int(planet_pop * 0.005), int(planet_pop * 0.02))

        stats = ((planet, planet_pop, planet_hp, planet_sh, planet_atk, planet_res),)
        planet_list += stats

    return planet_list


def move_to_planet(planet_positions_det, moving_x):  # uruchamia klasy po wleceniu na planete
        temp = 0
        for i in planet_position_temp:
            if planet_position_temp[i] == moving_x:
                temp += i

        planets_data_class = Planets_data(generate_planet_fc, temp)
        print("Przyleciałeś do planety ", planet_positions_det.get(moving_x)[0])
        planets_data_class.planet_action_choice()
        while True:
            player_choice = input('Co chcesz zrobić?')
            if player_choice == "1":
                player_dmg = player.calc_dmg()
                planets_data_class.planet_get_dmg(player_dmg)
                print("Zadales", player_dmg, "pkt obrażen. Planecie pozostalo", planets_data_class.planet_stats()[2],
                      "pkt obrony.")
                if planets_data_class.planet_stats()[2] == 0:
                    planets_data_class.planet_sacked()
                    player.res_up(planets_data_class.planet_stats()[6])
                    print(map_flat)
                    return False
                planet_dmg = planets_data_class.planet_attack()
                player.get_damage(planet_dmg)
                print("Planeta zaatakowala za", planet_dmg, "pkt. Pozostalo Ci", player.ship_stats()[0], "/",
                      player.ship_stats()[1], "hp oraz", player.ship_stats()[2], "/", player.ship_stats()[3], "oslon")
                if player.ship_stats()[0] == 0:
                    print("Zginales :(")
                    return False

            elif player_choice == "2":
                print(map_flat)
                return False

            elif player_choice == "3":
                print("Masz", player.ship_stats()[7], "kredytow. Co chcesz kupić?")
                print("     1 - Statek")
                print("     2 - Przedmioty")
                shop_choice = input(":")
                print(shop_choice)
                while True:
                    if shop_choice == "1":
                        print("Mozesz kupic nastepujace statki:")
                        ship_no = 1
                        for ship in ships:
                            print(ship_no, ship[3], ship[4], " - ", ship[5])
                            ship_no += 1
                        print(ship_no, "Powrót do mapy")
                        player_choice_shop = input("Co wybierasz? ")
                        for player_choice in range(ship_no):
                            if player_choice == int(player_choice_shop) - 1:
                                temp = int(player_choice_shop) - 1
                                player.ship_choice(temp)
                        print(player.ship_stats()[0])



            else:
                print("Nie rozumiem :(")




def generate_map():  # Funkcja odpowiedzialna za wygenerowanie listy uruchamianej później w funkcji map()
    for i in range(0, 120):
        if i == 0:
            moving.append("0")
        else:
            moving.append(".")
    return moving


def map():  # Funkcja odpowiedzialna za wygenerowanie mapy
    map_flat = ""
    for i in moving:
        if len(map_flat) == 19:
            map_flat += i + "\n"
        elif len(map_flat) == 40:
            map_flat += i + "\n"
        elif len(map_flat) == 61:
            map_flat += i + "\n"
        elif len(map_flat) == 82:
            map_flat += i + "\n"
        elif len(map_flat) == 103:
            map_flat += i + "\n"
        else:
            map_flat += i

    return map_flat


def move_error():  # Funkcja odpowiedzialna za wygenerowanie komunikatu przy próbie opuszczenia mapy
    print("Nie możesz wylecieć poza galaktykę")
    map()
    map_flat = map()
    print(map_flat)


def key_error(move):  # Funkcja odpowiedzialna za wygenerowanie komunikatu przy wprowadzeniu klawiszy spoza klawiszologi
    while move not in correct_move:
        move = input("Zły klawisz,  którą stronę chcesz iść? a - w lewo, d - w prawo, s - dół, w - góra ").lower()


def move_engine(moving_x=0):  # Funkcja odpowiedzialna za poruszanie się statku po mapie
    move = input("W którą stronę chcesz iść? a - w lewo, d - w prawo, s - dół, w - góra ").lower()

    while move not in correct_move:
        move = input("Zły klawisz,  którą stronę chcesz iść? a - w lewo, d - w prawo, s - dół, w - góra ").lower()

    while move == "a" or move == "d" or move == "w" or move == "s":
        if move == "a":
            if moving_x == 0 or moving_x == 20 or moving_x == 40 or moving_x == 60 or moving_x == 80 or moving_x == 100:
                move_error()
            else:
                if moving[moving_x - 1] == "P":

                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x - 1] = "W"
                    moving_x -= 1
                    map()
                    map_flat = map()
                    print(map_flat)
                    move_to_planet(planet_positions_det, moving_x)
                else:
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x - 1] = "0"
                    moving_x -= 1
                    map()
                    map_flat = map()
                    print(map_flat)
        elif move == "d":
            if moving_x == 19 or moving_x == 39 or moving_x == 59 or moving_x == 79 or moving_x == 99 or moving_x == 119:
                move_error()
            else:
                if moving[moving_x + 1] == "P":
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x + 1] = "W"
                    moving_x += 1
                    map()
                    map_flat = map()
                    print(map_flat)
                    move_to_planet(planet_positions_det, moving_x)
                else:
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x + 1] = "0"
                    moving_x += 1
                    map()
                    map_flat = map()
                    print(map_flat)

        elif move == "w":
            if moving_x in range(0, 19):
                move_error()
            else:
                if moving[moving_x - 20] == "P":
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x - 20] = "W"
                    moving_x -= 20
                    map()
                    map_flat = map()
                    print(map_flat)
                    move_to_planet(planet_positions_det, moving_x)
                else:
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x - 20] = "0"
                    moving_x -= 20
                    map()
                    map_flat = map()
                    print(map_flat)

        elif move == "s":
            if moving_x in range(100, 120):
                move_error()
            else:
                if moving[moving_x + 20] == "P":
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x + 20] = "W"
                    moving_x += 20
                    map()
                    map_flat = map()
                    print(map_flat)
                    move_to_planet(planet_positions_det, moving_x)
                else:
                    if moving[moving_x] == "W":
                        moving[moving_x] = "P"
                    else:
                        moving[moving_x] = "."
                    moving[moving_x + 20] = "0"
                    moving_x += 20
                    map()
                    map_flat = map()
                    print(map_flat)

        if player.ship_stats()[0] == 0:
            print('Koniec gry')
            break
        move = input("W którą stronę chcesz iść? a - w lewo, d - w prawo, s - dół, w - góra ").lower()

        while move not in correct_move:
            move = input("Zły klawisz,  którą stronę chcesz iść? a - w lewo, d - w prawo, s - dół, w - góra ").lower()


moving = generate_map()
generate_planet_fc = genarate_planet()

for i in range(7):  # Kod odpowiedzialny za wygenerowanie na mapie planet na losowych koordynatach.
    new_planet = random.randint(1, 119)
    while new_planet in planet_positions:
        new_planet = random.randint(1, 119)
    planet_positions.append(new_planet)
    planet_positions_det[new_planet] = generate_planet_fc[planet_positions_det_count]
    planet_position_temp[planet_positions_det_count] = new_planet
    planet_positions_det_count += 1
    moving[planet_positions[i]] = "P"

map_flat = map()
print(map_flat)
move_engine()