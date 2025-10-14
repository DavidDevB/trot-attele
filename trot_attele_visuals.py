#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


""" Retourne le nombre de chevaux à faire participer (entrés par le joueur) """
def get_number_of_horses():
    return input("Choose the number of horses for this race: ")


""" Retourne le type de la course (entré par le joueur) """
def get_race_type():
    return input("Choose race type between trifecta, quartet, quintet: ")


""" Retourne une liste de tous les chevaux participants (dictionnaires)"""
def get_horses_specs():
    horses = []
    for i in range(int(get_number_of_horses())):
        horses.append({"number": i + 1, "dist": 2400, "speed": 0})
    return horses


""" Fonction principale faisant fonctionner la course"""
def launch_race():
    horses = get_horses_specs()
    race_type = get_race_type()
    race_types = {"trifecta": 3, "quartet": 4, "quintet": 5}
    winners = []

    # Boucle while permettant de boucler jusqu'à qu'il y est le nombre de gagnants indiqués par le type de course,
    # et jusqu'à qu'il n'y ait plus de cheval avec une distance supérieure à zéro.
    while len(winners) < race_types[race_type] and any(horse["dist"] > 0 for horse in horses):
        for i in range(len(horses)):
            dice = random.choice(range(1, 7))

            # Switch match qui modifie la vitesse des chevaux selon le lancer de dé.
            match horses[i]["speed"]:
                case 0:
                    if dice in [2, 3, 4]:
                        horses[i]["speed"] += 1
                    elif dice in [5, 6]:
                        horses[i]["speed"] += 2
                case 1:
                    if dice in [3, 4, 5]:
                        horses[i]["speed"] += 1
                    elif dice == 6:
                        horses[i]["speed"] += 2
                case 2:
                    if dice in [3, 4, 5]:
                        horses[i]["speed"] += 1
                    elif dice == 6:
                        horses[i]["speed"] += 2
                case 3:
                    if dice == 1:
                        horses[i]["speed"] -= 1
                    elif dice in [4, 5, 6]:
                        horses[i]["speed"] += 1
                case 4:
                    if dice == 1:
                        horses[i]["speed"] -= 1
                    elif dice in [5, 6]:
                        horses[i]["speed"] += 1
                case 5:
                    if dice == 1:
                        horses[i]["speed"] -= 2
                    elif dice == 2:
                        horses[i]["speed"] -= 1
                    elif dice == 6:
                        horses[i]["speed"] += 1
                case 6:
                    if dice == 1:
                        horses[i]["speed"] -= 2
                    elif dice == 2:
                        horses[i]["speed"] -= 1
                    elif dice == 6:
                        horses[i]["speed"] = -1

            # Switch match qui modifie la distance de chaque cheval selon sa vitesse.
            match horses[i]["speed"]:
                case 0:
                    continue
                case 1:
                    horses[i]["dist"] -= 23
                case 2:
                    horses[i]["dist"] -= 46
                case 3:
                    horses[i]["dist"] -= 69
                case 4:
                    horses[i]["dist"] -= 92
                case 5:
                    horses[i]["dist"] -= 115
                case 6:
                    horses[i]["dist"] -= 138

            # Condition de victoire selon si le nombre de vainqueurs dans le tableau winners est inférieur ou supérieur au type de course,
            # et si le cheval à une distance inférieure ou égale à zéro.
            if len(winners) < race_types[race_type] and horses[i] not in winners:
                if horses[i]["dist"] <= 0:
                    winners.append(horses[i])
                    print(f"{horses[i]['number']} a terminé !")

            # Condition qui arrête la boucle si le nombre de gagnants dans le tableau winners
            # est égal ou supérieur au type de course.
            if len(winners) >= race_types[race_type]:
                break


if __name__ == "__main__":
    launch_race()