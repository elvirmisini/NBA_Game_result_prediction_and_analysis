import pandas as pd
import csv
import numpy

from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv("nbagames.csv")
data1 = pd.read_csv("teamRecord1.csv")

data.columns = ['', 'Team', 'Game', 'Date', 'Home', 'Opponent', 'WINorLOSS', 'TeamPoints', 'OpponentPoints',
                'FieldGoals', 'FieldGoalsAttempted', 'FieldGoals.', 'X3PointShots', 'X3PointShotsAttempted',
                'X3PointShots.', 'FreeThrows', 'FreeThrowsAttempted', 'FreeThrows.', 'OffRebounds', 'TotalRebounds',
                'Assists', 'Steals', 'Blocks', 'Turnovers', 'TotalFouls', 'Opp.FieldGoals', 'Opp.FieldGoalsAttempted',
                'Opp.FieldGoals.', 'Opp.3PointShots', 'Opp.3PointShotsAttempted', 'Opp.3PointShots.',
                'Opp.FreeThrowsOpp.', 'FreeThrowsAttempted', 'Opp.FreeThrows.', 'Opp.OffRebounds', 'Opp.TotalRebounds',
                'Opp.Assists', 'Opp.Steals', 'Opp.Blocks', 'Opp.Turnovers', 'Opp.TotalFouls']
win = 0
loss = 0
points = 0
totalPoints = 0
fieldGoals = 0
totalField = 0
assists = 0
totalAssist = 0

a_list = []

for i in range(30):
    first_value = data['WINorLOSS'].values[i * 82:82 * (i + 1)]
    for fi in first_value:
        points = points + data['TeamPoints'].values[i * 82:(i + 1) * 82]
        fieldGoals = fieldGoals + data['FieldGoals'].values[i * 82:(i + 1) * 82]
        assists = assists + data['Assists'].values[i * 82:(i + 1) * 82]

        totalPoints = np.sum(points)
        totalField = np.sum(fieldGoals)
        totalAssist = np.sum(assists)

        if fi == 'W':
            win = win + 1
        else:
            loss = loss + 1
    print(data['Team'].values[(i + 1) * 81], round(win / 3, 2), round(loss / 3, 2), round(totalPoints / (8200 * 5), 2),
          round(totalField / 8200 / 3, 2), round(totalAssist / 8200, 2))
    table = data['Team'].values[(i + 1) * 81], round(win / 3, 2), round(loss / 3, 2), round(totalPoints / (8200 * 5),
                                                                                            2), round(
        totalField / 8200 / 3, 2), round(totalAssist / 8200, 2)
    a_list.append(table)
    win = 0
    loss = 0
    points = 0
    fieldGoals = 0
    assists = 0
    totalPoints = 0
    totalField = 0
    totalAssist = 0
print("")


def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if sub_li[j][1] > sub_li[j + 1][1]:
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


b_list = Sort(a_list)


def Reverse(lst):
    return [ele for ele in reversed(lst)]


c_list = Reverse(b_list)
d_list = ['Team', 'Win', 'Loss', 'Offense', 'Standings', 'Stats']
file = open('teamRecord1.csv', 'w+', newline='\n')

with file:
    write = csv.writer(file)
    write.writerow(d_list)
    for i in range(29):
        write.writerow(c_list[i])

for i in range(30):
    print(c_list[i])
