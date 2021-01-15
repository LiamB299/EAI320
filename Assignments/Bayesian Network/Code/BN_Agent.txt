#!/usr/bin/env python3
import csv
import numpy as np

# Liam Burgess
# 18015001
# 5/29/2020
# Refactored 6/3/2020
# Refactored 6/4/2020


# =====================================
# Variables holding data for probability computations
#f_table = np.full((243, 5), 1)
#total_x = np.full((5, 3), 1)
#total_y = np.full(243, 1)
#total = np.full(5, 1)
# =====================================

# Load data from array
def load_data():
    global f_table
    f_table = np.array([[    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  229,   229,   229,   229,   229],
       [ 7538,  7538,  7538,  7538,  7538],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7342,  7342,  7342,  7342,  7342],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [28111, 28111, 28111, 28111, 28111],
       [    1,     1,     1,     1,     1],
       [ 7650,  7650,  7650,  7650,  7650],
       [28342, 28342, 28342, 28342, 28342],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [28343, 28343, 28343, 28343, 28343],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  268,   268,   268,   268,   268],
       [  255,   255,   255,   255,   255],
       [    1,     1,     1,     1,     1],
       [ 7613,  7613,  7613,  7613,  7613],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  247,   247,   247,   247,   247],
       [ 7596,  7596,  7596,  7596,  7596],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  184,   184,   184,   184,   184],
       [    1,     1,     1,     1,     1],
       [28467, 28467, 28467, 28467, 28467],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [35942, 35942, 35942, 35942, 35942],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [28551, 28551, 28551, 28551, 28551],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7309,  7309,  7309,  7309,  7309],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7514,  7514,  7514,  7514,  7514],
       [  183,   183,   183,   183,   183],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [28405, 28405, 28405, 28405, 28405],
       [ 7559,  7559,  7559,  7559,  7559],
       [    1,     1,     1,     1,     1],
       [28226, 28226, 28226, 28226, 28226],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [28418, 28418, 28418, 28418, 28418],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29892, 29892, 29892, 29892, 29892],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [30148, 30148, 30148, 30148, 30148],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [30193, 30193, 30193, 30193, 30193],
       [ 7698,  7698,  7698,  7698,  7698],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7385,  7385,  7385,  7385,  7385],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7542,  7542,  7542,  7542,  7542],
       [  228,   228,   228,   228,   228],
       [    1,     1,     1,     1,     1],
       [30128, 30128, 30128, 30128, 30128],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29968, 29968, 29968, 29968, 29968],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [30443, 30443, 30443, 30443, 30443],
       [    1,     1,     1,     1,     1],
       [ 7483,  7483,  7483,  7483,  7483],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  202,   202,   202,   202,   202],
       [ 7397,  7397,  7397,  7397,  7397],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7416,  7416,  7416,  7416,  7416],
       [30523, 30523, 30523, 30523, 30523],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [30643, 30643, 30643, 30643, 30643],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [37779, 37779, 37779, 37779, 37779],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  232,   232,   232,   232,   232],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7682,  7682,  7682,  7682,  7682],
       [  268,   268,   268,   268,   268],
       [  241,   241,   241,   241,   241],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7616,  7616,  7616,  7616,  7616],
       [    1,     1,     1,     1,     1],
       [  244,   244,   244,   244,   244],
       [    1,     1,     1,     1,     1],
       [  279,   279,   279,   279,   279],
       [ 7581,  7581,  7581,  7581,  7581],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  243,   243,   243,   243,   243],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [37156, 37156, 37156, 37156, 37156],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29653, 29653, 29653, 29653, 29653],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29650, 29650, 29650, 29650, 29650],
       [    1,     1,     1,     1,     1],
       [ 7654,  7654,  7654,  7654,  7654],
       [  220,   220,   220,   220,   220],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  221,   221,   221,   221,   221],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [  229,   229,   229,   229,   229],
       [    1,     1,     1,     1,     1],
       [ 7497,  7497,  7497,  7497,  7497],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29375, 29375, 29375, 29375, 29375],
       [ 7797,  7797,  7797,  7797,  7797],
       [    1,     1,     1,     1,     1],
       [28999, 28999, 28999, 28999, 28999],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29539, 29539, 29539, 29539, 29539],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7384,  7384,  7384,  7384,  7384],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7498,  7498,  7498,  7498,  7498],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [ 7665,  7665,  7665,  7665,  7665],
       [29455, 29455, 29455, 29455, 29455],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29473, 29473, 29473, 29473, 29473],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [29332, 29332, 29332, 29332, 29332],
       [ 7365,  7365,  7365,  7365,  7365],
       [    1,     1,     1,     1,     1],
       [  161,   161,   161,   161,   161],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1],
       [    1,     1,     1,     1,     1]])
    totals()
    return

# =====================================


# find row index of frequency table
def table_write_row_index(prev, next):
    if next == "R":
        start = 0
    elif next == "P":
        start = 81
    else:
        start = 161

    if prev[0] == "R":
        start += 0
    elif prev[0] == "P":
        start += 27
    else:
        start += 53

    if prev[1] == "R":
        start += 0
    elif prev[1] == "P":
        start += 9
    else:
        start += 17

    if prev[2] == "R":
        start += 0
    elif prev[2] == "P":
        start += 3
    else:
        start += 6

    if prev[3] == "R":
        start += 0
    elif prev[3] == "P":
        start += 1
    else:
        start += 2
    return start


def gen_hard_code():
    np.set_printoptions(threshold=np.nan)
    filename = "DUMP1.txt"
    file = open(filename, "w")
    file.write(repr(f_table))
    return


# return move which will beat yt
def win_move(y):
    if y == "R":
        return "P"
    elif y == "P":
        return "S"
    else:
        return "R"


# Read CSV into frequency table
def CSV_read():
    index = 0
    filename = "data1.csv"
    with open(filename) as CSV:
        reader = csv.reader(CSV, delimiter=',')
        for row in reader:
            index = table_write_row_index(row[0], win_move(row[1]))
            for i in range(5):
                f_table[index][i] +=1
    totals()
    return


# update the frequency table as new data is generated
def update(hist, play):
    index = table_write_row_index(hist, play)
    for i in range(5):
        f_table[index][i] += 1
    return


# Compute totals of frequency table
def totals():
    global total
    global total_x
    global total_y
    for i in range(81):
        for j in range(5):
            total_y[i] += f_table[i][j]
            total_x[j][0] += f_table[i][j]

            total_y[81+i] += f_table[81+i][j]
            total_x[j][1] += f_table[81+i][j]

            total_y[161+i] += f_table[161+i][j]
            total_x[j][2] += f_table[161+i][j]
    for i in range(5):
        for j in range(3):
            total[i] += total_x[i][j]
    return


# probability of class Ck
def p_c(obj):
    if obj == "R":
        pc = total_x[0][0]
    elif obj == "P":
        pc = total_x[0][1]
    else:
        pc = total_x[0][2]
    return pc/(total_x[0][0]+total_x[0][1]+total_x[0][2])


# product of different feature variable probabilities
def cond(y, evi):
    v_1 = f_table[table_write_row_index(evi,y)][1] / total[1]
    v_2 = f_table[table_write_row_index(evi,y)][2] / total[2]
    v_3 = f_table[table_write_row_index(evi,y)][3] / total[3]
    v_4 = f_table[table_write_row_index(evi,y)][4] / total[4]
    return v_1*v_2*v_3*v_4


# compute class c1 and return argmax
def compute_prob(prev):
    c1 = np.zeros(3)
    m = ["R", "P", "S"]
    for i in range(3):
        con = cond(m[i], prev)
        pc = p_c(m[i])
        if np.isnan(pc):
            pc = 0
        c1[i] = pc * con
    index_max = max(range(len(c1)), key=c1.__getitem__)
    object = ret_obj(index_max)
    return object


# return argmax object of Ck
def ret_obj(ind):
    if ind==0:
        return "R"
    elif ind==1:
        return "P"
    else:
        return "S"


# Wrapper function- The previous set of four moves is passed in and the classifier determines the next move
# Data may be read from CSV, Array or generated during online learning
# Both options disabled for Online learning, the agent manages data itself
def classifier(prev):
    #CSV_read()
    #Load from array
    #load_data()
    return compute_prob(prev)

# classifier("RRRR") returns "P"

# ======================================================
# Agent Code
# Implements the simple strategy of playing randomly for two moves and then generates moves from the data acquired
# Data is shifted out in a first two in- first two out basis
# The neural network beat this agent

out = ""
if input == "":
    f_table = np.full((243, 5), 1)
    total_x = np.full((5, 3), 1)
    total_y = np.full(243, 1)
    total = np.full(5, 1)
    plays = []
    history = []
    prev_play = ""
    for _ in range(2):
        plays.append(np.random.choice(["R", "P", "S"]))
    out = plays.pop()
    history.append(out)
else:
    inp = input
    history.append(inp)
    if len(plays) > 0:
        out = plays.pop()
        history.append(out)
    else:
        if prev_play == "":
            prev = history[0]+history[1]+history[2]+history[3]
            prev_play = classifier(prev)
            history.append(prev_play)
            out = prev_play
        else:
            update(prev, win_move(inp))
            history.pop()
            history.pop()
            prev = history[0] + history[1] + history[2] + history[3]
            prev_play = classifier(prev)
            history.append(prev_play)
            out = prev_play

output = out


# ======================================================
