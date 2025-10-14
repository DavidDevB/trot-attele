#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()


""" Retourne le nombre de chevaux à faire participer (entrés par le joueur) """
def get_number_of_horses():
    return input("Choose the number of horses for this race: ")


race_types = {"trifecta": 3, "quartet": 4, "quintet": 5}


""" Retourne le type de la course (entré par le joueur) """
def get_race_type():
    while True:
        race_type = input("Choose race type between trifecta, quartet, quintet: ")
        if race_type not in race_types.keys():
            print("Must be trifecta, quartet or quintet.")
            race_type = input("Choose race type between trifecta, quartet, quintet: ")
        return race_type


""" Retourne une liste de tous les chevaux participants (dictionnaires)"""
def get_horses_specs():
    horses = []
    for i in range(int(get_number_of_horses())):
        horses.append({"number": i + 1, "dist": 0, "speed": 0})
    return horses


""" Fonction principale faisant fonctionner la course"""
def launch_race():
    horses = get_horses_specs()
    race_type = get_race_type()

    winners = []
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in horses]

    # Boucle while permettant de boucler jusqu'à qu'il y est le nombre de gagnants indiqués par le type de course,
    # et jusqu'à qu'il n'y ait plus de cheval avec une distance supérieure à zéro.
    while len(winners) < race_types[race_type] and any(horse["dist"] < 2400 for horse in horses):
        for horse in horses[:]:
            dice = random.choice(range(1, 7))

            # Switch match qui modifie la vitesse des chevaux selon le lancer de dé.
            match horse["speed"]:
                case 0:
                    if dice in [2, 3, 4]:
                        horse["speed"] += 1
                    elif dice in [5, 6]:
                        horse["speed"] += 2
                case 1:
                    if dice in [3, 4, 5]:
                        horse["speed"] += 1
                    elif dice == 6:
                        horse["speed"] += 2
                case 2:
                    if dice in [3, 4, 5]:
                        horse["speed"] += 1
                    elif dice == 6:
                        horse["speed"] += 2
                case 3:
                    if dice == 1:
                        horse["speed"] -= 1
                    elif dice in [4, 5, 6]:
                        horse["speed"] += 1
                case 4:
                    if dice == 1:
                        horse["speed"] -= 1
                    elif dice in [5, 6]:
                        horse["speed"] += 1
                case 5:
                    if dice == 1:
                        horse["speed"] -= 2
                    elif dice == 2:
                        horse["speed"] -= 1
                    elif dice == 6:
                        horse["speed"] += 1
                case 6:
                    if dice == 1:
                        horse["speed"] -= 2
                    elif dice == 2:
                        horse["speed"] -= 1
                    elif dice == 6:
                        horses.remove(horse)
                        print(f"Horse number {horse["number"]} is disqualified!")

            # Switch match qui modifie la distance de chaque cheval selon sa vitesse.
            match horse["speed"]:
                case 0:
                    continue
                case 1:
                    horse["dist"] += 23
                case 2:
                    horse["dist"] += 46
                case 3:
                    horse["dist"] += 69
                case 4:
                    horse["dist"] += 92
                case 5:
                    horse["dist"] += 115
                case 6:
                    horse["dist"] += 138

            # Librairie Matplotlib pour rajouter le graphique horizontal
            ax.clear()
            y_pos = np.arange(len(horses))
            distance = [horse["dist"] for horse in horses]
            ax.barh(y_pos, distance, align='center', color = colors)
            ax.set_yticks(y_pos, labels=[horse["number"] for horse in horses])
            ax.invert_yaxis()
            ax.set_xlabel('Distance')
            ax.set_title(f'Race: {race_type}')

            plt.pause(0.05)


            # Condition de victoire selon si le nombre de vainqueurs dans le tableau winners est inférieur ou supérieur au type de course,
            # et si le cheval à une distance inférieure ou égale à zéro.
            if len(winners) < race_types[race_type] and horse not in winners:
                if horse["dist"] >= 2400:
                    winners.append(horse)
                    print(f"{horse['number']} a terminé !")
                if len(winners) >= race_types[race_type]:
                    match race_type:
                        case "trifecta":
                            print(
                                f"Winners are {winners[0]["number"]}, {winners[1]["number"]} et {winners[2]["number"]}!")
                        case "quartet":
                            print(
                                f"Winners are {winners[0]["number"]}, {winners[1]["number"]}, {winners[2]["number"]} and {winners[3]["number"]}!")
                        case "quintet":
                            print(
                                f"Winners are {winners[0]["number"]}, {winners[1]["number"]}, {winners[2]["number"]}, {winners[3]["number"]} and {winners[4]["number"]}!")

            # Condition qui arrête la boucle si le nombre de gagnants dans le tableau winners
            # est égal ou supérieur au type de course.
            if len(winners) >= race_types[race_type]:
                break


if __name__ == "__main__":
    launch_race()