#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_number_of_horses():
    return input("Choose the number of horses for this race: ")


def get_race_type():
    return input("Choose race type between trifecta, quartet, quintet: ")


def get_horses_specs():
    horses = []
    for i in range(int(get_number_of_horses())):
        horses.append({"number": i + 1, "dist": 2400, "speed": 0})
    return horses

def launch_race():
    horses = get_horses_specs()
    race_types = {"trifecta": 3, "quartet": 4, "quintet": 5}
    winners = []

    while all("dist" in horse for horse  in horses) > 0:
        for i in range(len(horses)):
            actual_speed = horses[i]["speed"]
            dice = random.choice(range(1, 7))
            dist = horses[i]["dist"]

            match actual_speed:
                case 0:
                    match dice:
                        case 1:
                            continue
                        case 2:
                            actual_speed += 1
                        case 3:
                            actual_speed += 1
                        case 4:
                            actual_speed += 1
                        case 5:
                            actual_speed += 2
                        case 6:
                            actual_speed += 2
                case 1:
                    match dice:
                        case 1:
                            continue
                        case 2:
                            continue
                        case 3:
                            actual_speed += 1
                        case 4:
                            actual_speed += 1
                        case 5:
                            actual_speed += 1
                        case 6:
                            actual_speed += 2
                case 2:
                    match dice:
                        case 1:
                            continue
                        case 2:
                            continue
                        case 3:
                            actual_speed += 1
                        case 4:
                            actual_speed += 1
                        case 5:
                            actual_speed += 1
                        case 6:
                            actual_speed += 2
                case 3:
                    match dice:
                        case 1:
                            actual_speed -= 1
                        case 2:
                            continue
                        case 3:
                            continue
                        case 4:
                            actual_speed += 1
                        case 5:
                            actual_speed += 1
                        case 6:
                            actual_speed += 1
                case 4:
                    match dice:
                        case 1:
                            actual_speed -= 1
                        case 2:
                            continue
                        case 3:
                            continue
                        case 4:
                            continue
                        case 5:
                            actual_speed += 1
                        case 6:
                            actual_speed += 1
                case 5:
                    match dice:
                        case 1:
                            actual_speed -= 2
                        case 2:
                            actual_speed -= 1
                        case 3:
                            continue
                        case 4:
                            continue
                        case 5:
                            continue
                        case 6:
                            actual_speed += 1
                case 6:
                    match dice:
                        case 1:
                            actual_speed -= 2
                        case 2:
                            actual_speed -= 1
                        case 3:
                            continue
                        case 4:
                            continue
                        case 5:
                            continue
                        case 6:
                            actual_speed = -1

            match actual_speed:
                case 0:
                    continue
                case 1:
                    dist -= 23
                case 2:
                    dist -= 46
                case 3:
                    dist -= 69
                case 4:
                    dist -= 92
                case 5:
                    dist -= 115
                case 6:
                    dist -= 138

            while len(winners) <= race_types[get_race_type()]:
                if actual_speed == 0:
                    winners.append(horses[i])

    print(winners)


if __name__ == "__main__":
    launch_race()