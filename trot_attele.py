#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulation de course de trot attelé
"""

import random
import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()



def get_number_of_horses():
    """
    Retourne le nombre de chevaux à faire participer (entrés par le joueur)
    """
    while True:
        number_of_horses = input("Choose the number of horses between 12 and 20 for this race: ")
        if number_of_horses.isdigit() and 12 <= int(number_of_horses) <= 20:
            return number_of_horses
        else:
            continue


race_types = {"trifecta": 3, "quartet": 4, "quintet": 5}



def get_race_type():
    """
    Retourne le type de la course (entré par le joueur)
    """
    while True:
        race_type = input("Choose race type between trifecta, quartet, quintet: ").lower()
        if race_type in race_types.keys():
            return race_type
        else:
            continue



def get_horses_specs():
    """
    Retourne une liste de tous les chevaux participants (dictionnaires)
    """
    horses = []
    for i in range(int(get_number_of_horses())):
        horses.append({"number": i + 1, "dist": 0, "speed": 0})
    return horses



def launch_race():
    """
    Fonction principale faisant fonctionner la course
    """
    horses = get_horses_specs()
    race_type = get_race_type()

    winners = []
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in horses]

    """
    Boucle while permettant de boucler jusqu'à qu'il y est le nombre de gagnants indiqués par le type de course,
    et jusqu'à qu'il n'y ait plus de cheval avec une distance inférieure à 2400.
    """
    while len(winners) < race_types[race_type] and any(horse["dist"] < 2400 for horse in horses):
        for horse in horses[:]:
            dice = random.choice(range(1, 7))

            """
            Switch match qui modifie la vitesse des chevaux selon le lancer de dé.
            """
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
                        print(f"Horse number {horse['number']} is disqualified!")

            """
            Switch match qui modifie la distance de chaque cheval selon sa vitesse.
            """
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

            """
            Librairie Matplotlib pour rajouter le graphique horizontal
            """
            ax.clear()
            y_pos = np.arange(len(horses))
            distance = [horse["dist"] for horse in horses]
            bars = ax.barh(y_pos, distance, align='center', color = colors)
            for i, bar in enumerate(bars):
                width = bar.get_width()
                speed = horses[i]["speed"]
                dist = horses[i]["dist"]
                ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                f"{speed} | {dist} m", va='center', fontsize=9, color='black')


            ax.invert_yaxis()
            ax.set_xlabel('Distance')
            ax.set_title(f'Race: {race_type}')

            plt.pause(0.01)


            """
            Condition de victoire selon si le nombre de vainqueurs dans le tableau winners est inférieur ou supérieur au type de course,
            et si le cheval à une distance supérieure ou égale à 2400.
            """
            if len(winners) < race_types[race_type] and horse not in winners:
                if horse["dist"] >= 2400:
                    winners.append(horse)
                    print(f"{horse['number']} a terminé !")
                if len(winners) >= race_types[race_type]:
                    match race_type:
                        case "trifecta":
                            print(
                                f"The winners are {winners[0]['number']}, {winners[1]['number']} et {winners[2]['number']}!")
                        case "quartet":
                            print(
                                f"The winners are {winners[0]['number']}, {winners[1]['number']}, {winners[2]['number']} and {winners[3]['number']}!")
                        case "quintet":
                            print(
                                f"The winners are {winners[0]['number']}, {winners[1]['number']}, {winners[2]['number']}, {winners[3]['number']} and {winners[4]['number']}!")

            """
            Condition qui arrête la boucle si le nombre de gagnants dans le tableau winners
            est égal ou supérieur au type de course.
            """

            if len(winners) >= race_types[str(race_type)]:
                break


if __name__ == "__main__":
    launch_race()