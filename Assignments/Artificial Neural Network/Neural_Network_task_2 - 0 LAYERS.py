#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib.pyplot as plt
#====================

# Refactor dates:
# 2/04/2020
# 8/04/2020
# 25/04/2020
# 28/04/2020
# 01/05/2020
# 03/05/2020

#np.random.seed(5)

#N = 1 #np.random.randint(5, 100)
weight_random_range = 1000000
test = []
wins = []
losses = []
np.random.seed(1)

#====================
# Generate data sets
# Return the 1 hot training data of a move as input feature
def last_move_1hot(move):
    if move == 'R':
        r = 1
        p = 0
        s = 0
        return r, p, s
    elif move == 'P':
        r = 0
        p = 1
        s = 0
        return r, p, s
    else:
        r = 0
        p = 0
        s = 1
        return r, p, s

# set target as winning move
def win_move(y_move):
    r, p, s = last_move_1hot(y_move)
    if r == 1:
        r = 0
        p = 1
        s = 0
        return r, p, s
    elif p == 1:
        r = 0
        p = 0
        s = 1
        return r, p, s
    else:
        r = 1
        p = 0
        s = 0
    return r, p, s


# Read CSV to generate input and testing data
def CSV_read(N, start = 0):
    d = []
    c = []
    filename = "data1.csv"
    with open(filename) as CSV:
        reader = csv.reader(CSV, delimiter=',')
        how_many = skip = 0
        for row in reader:
            if skip < start:
                skip += 1
                continue
            for i in range(4):
                r, p, s = last_move_1hot(row[0][i])
                d.append(r)
                d.append(p)
                d.append(s)

            # generate move as target which may be used to train towards
            r, p, s = win_move(row[1])
            c.append(r)
            c.append(p)
            c.append(s)
            how_many += 1
            if how_many == N:
                break

        # bias
        d.append(1)

        #print("Data read complete")

    return d, c

# ============================================
# export data to CSV file
def export(DHW, HHW, HCW):
    #np.savetxt("Input_Hidden.csv", DHW, delimiter=",")
    #np.savetxt("Hidden_Hidden.csv", HHW, delimiter=",")
    #np.savetxt("Hidden_Output.csv", HCW, delimiter=",")
    return print("Files saved")

# generate files with the format of an array for easy copying
def gen_hard_code(DHW, HHW, HCW):
    np.set_printoptions(threshold=np.nan)
    filename = "DUMP1.txt"
    file = open(filename, "w")
    file.write(repr(DHW))
    filename = "DUMP2.txt"
    file = open(filename, "w")
    file.write(repr(HHW))
    filename = "DUMP3.txt"
    file = open(filename, "w")
    file.write(repr(HCW))
    return print("data hardcoded")

# load pre-generated weights
def Load_from_file():
    W = [line.split(',') for line in open("Input_Hidden.csv")]
    DHW = np.array(W)
    DHW.transpose()
    W = [line.split(',') for line in open("Hidden_Hidden.csv")]
    HHW = np.array(W)
    HHW.transpose()
    W = [line.split(',') for line in open("Hidden_Output.csv")]
    HCW = np.array(W)
    HCW.transpose()
    return DHW.astype('float64'), HHW.astype('float64'), HCW.astype('float64')


# ============================================
# Graphing
# pyplot graphing function
def graph(x, y, xlab, ylab, title, file):
    x = np.arange(0, x, 1)
    plt.title(title, size=18)
    plt.xlabel(xlab, size=18)
    plt.ylabel(ylab, size=18)
    plt.grid(1)
    plt.plot(x, y)
    plt.show()
    if file == 1:
        plt.savefig('Loss.png', bbox_inches='tight')
    else:
        None
    return


#============================================
# back propagation functions
# Generate weights
def weights(depth, width):
    W = np.empty([depth, width])
    W.astype(float)

    for i in range(depth):
        for j in range(width):
            rand = np.random.randint(-1*weight_random_range, weight_random_range) / weight_random_range
            W[i][j] = rand
    return W


# Generate the arrays as numpy arrays for the BackProp function
def gen_arrays(D, C, Win, Wout):
    retD = np.array(D)
    retC = np.array(C)
    retWin = np.array(Win)
    retWout = np.array(Wout)
    return retD, retC, retWin, retWout


# array of errors for back propagation
def array_errors(comp, target):
    copy = target - comp
    return copy


# compute the error of the data
def compute_error(computed, target):
    sum = 0
    for i in range(np.size(computed)):
        sum += np.square(target[i] - computed[i])
    sum /= 2
    return sum


# computer convergence criterion
def convergence_criterion(Ei, Ef):
    if Ef - Ei > 0:
        return True
    else:
        return False


# sigmoid activation function
def activation_function(z):
    sum = 1 / (1 + np.e**-z)
    return sum


# derivative of activation function
def derivative_activation_function(z):
    sum = activation_function(z)
    sum = sum * (1 - sum)
    return sum


# using numpy matrix multiplication
def forward_layer_propagation(A, W):
    inj = np.matmul(W, A)
    Ao = activation_function(inj)
    return Ao, inj


# compute upstream gradient at output
def output_back_gradient(inj, Err):
    der = derivative_activation_function(inj)
    del_j = der * Err
    return del_j


# compute upstream gradient for nodes not the output
def back_gradient(inj, W, j_del):
    hold = []
    for i in range(W.shape[1]):
        sum = 0
        for j in range(W.shape[0]):
            sum += W[j][i]
        hold.append(sum)
    hold = np.array(hold)
    inj = derivative_activation_function(inj)
    sum = np.outer(inj, hold).transpose()
    i_del = np.matmul(sum, j_del)
    return i_del


# generate a bias array of the correct size for appending to np array
def bias_array(size):
    ret = []
    for _ in range(size):
        ret.append(1)
    return np.array(ret)


# update weights
def weight_update(W, delta, learning_rate, A):
    sum = np.outer(delta, A)
    sum *= learning_rate
    new_weights = W + sum
    return new_weights


# changes final computation of moves from decimal to moves to be played
def moves(number_of_moves, comp_data):
    tolerence = 0.6
    if number_of_moves*3 > np.size(comp_data):
        print("Not enough moves from data")
        return 1

    #if 0.4 < comp_data[0] < 0.6:
    #    return print("Data not fitted enough")

    moves = []
    i = 0
    while len(moves) != number_of_moves:
        for x in range(3):
            if comp_data[i+x] > tolerence:
                if x==0:
                    moves.append("R")
                elif x==1:
                    moves.append("P")
                elif x==2:
                    moves.append("S")
                i += 3
                break
            elif x == 2:
                moves.append("R")
                i += 3
                break

    return moves


# test against data not used to train with from CSV best score is 100/100
def real_test(target, comp):
    w = c = 0
    for i in range(np.size(target)):
        if comp[i] > 0.8:
            if target[i] == np.ceil(comp[i]):
                c += 1
            else:
                w += 1
    return w, c


# Back-propagation algorithm
def BackPropagation(dn, cn_target, dhw, learning_rate, epoch, error):
    loss = []
    e = 0
    cn_comp = []
    for iteration in range(epoch):

        #print("Iteration: "+str(iteration+1))

        # forward propagation
        # input to hidden 1
        dn.transpose()
        cn_comp, in1 = forward_layer_propagation(dn, dhw)

        # only prediction not backprop desired
        if cn_target == []:
            return cn_comp

        # compute errors
        e = compute_error(cn_comp, cn_target)
        loss.append(e)

        # check error convergence
        if len(loss) > 1:
            if convergence_criterion(loss[len(loss) - 2], loss[len(loss) - 1]):
                break

        # ===============================================

        # back propagation
        # Cost calculation
        E = array_errors(cn_comp, cn_target)

        # output to input gradient calculation
        j_del = output_back_gradient(in1, E)

        # update output to input layer weights
        dhw = weight_update(dhw, j_del, learning_rate, dn)

    return dhw, loss, cn_comp


# =====================================
# Tests
def tests(N_samples, sets, iterate, error_stop, learn_rate, hidden_nodes):
    wins = []
    #hidden_nodes = int(N_samples/8)
    #("Iteration: 0")
    loss_total = []
    D, C = CSV_read(N_samples, 0)
    Win = weights(len(C), len(D))
    dn, cn, Win, [] = gen_arrays(D, C, Win, [])
    DHW, loss, CN = BackPropagation(dn, cn, Win, learn_rate, iterate, error_stop)
    loss_total.extend(loss)
    wrong, correct = real_test(cn, CN)
    wins.append(correct)
    losses.append(wrong)
    #print(moves(N, CN))
# ======================================

    for i in range(1, sets):
        print("Iteration: "+str(i))
        D, C = CSV_read(N_samples, i*N_samples)
        dn, cn, [], [] = gen_arrays(D, C, [], [])
        DHW, loss, CN = BackPropagation(dn, cn, DHW, learn_rate, iterate, error_stop)
        loss_total.extend(loss)
        wrong, correct = real_test(cn, CN)
        wins.append(correct)
        losses.append(wrong)
        #print(moves(N, CN))

    #print(CN)

    graph(len(loss_total), loss_total, "Number of Iterations", "Loss", "Epochs vs Loss", 1)
    graph(len(wins), wins, "Number of Iterations", "Wins", "Sample set correctness rate vs Number of Iterations", 2)
    #export(DHW, HHW, HCW)
    #gen_hard_code(DHW, HHW, HCW)
    return

# =====================================
# n, number of data sets, epochs, error, rate of learning, hidden nodes

#Epochs
#tests(100, 150, 1, 0.000001, 0.83, int(100/8))
#tests(100, 150, 5, 0.000001, 0.83, int(100/8))
#tests(100, 150, 10, 0.000001, 0.83, int(100/8))
#tests(100, 150, 15, 0.000001, 0.83, int(100/8))
#tests(100, 150, 20, 0.000001, 0.83, int(100/8))
#tests(100, 150, 30, 0.000001, 0.83, int(100/8))

# hidden layers
tests(100, 300, 10, 0.000001, 1, int(100/8))

# hidden nodes
#tests(100, 150, 10, 0.000001, 0.8, 1)
#tests(100, 150, 10, 0.000001, 0.8, int(100/8))
#tests(100, 150, 10, 0.000001, 0.8, int(100/4))
#tests(100, 150, 10, 0.000001, 0.8, int(100/2))
#tests(100, 150, 10, 0.000001, 0.8, int(100))
#tests(100, 150, 10, 0.000001, 0.8, int(200))

# learning rate
#tests(100, 150, 10, 0.000001, 0.01, int(100/8))
#tests(100, 150, 10, 0.000001, 0.1, int(100/8))
#tests(100, 150, 10, 0.000001, 0.8, int(100/8))
#tests(100, 150, 10, 0.000001, 5, int(100/8))
#tests(100, 150, 10, 0.000001, 10, int(100/8))
#tests(100, 150, 10, 0.000001, 25, int(100/8))
#tests(100, 150, 10, 0.000001, 100, int(100/8))

# sample sets
#tests(100, 1, 10, 0.000001, 0.83, int(100/8))
#tests(100, 10, 10, 0.000001, 0.83, int(100/8))
#tests(100, 50, 10, 0.000001, 0.83, int(100/8))
#tests(100, 100, 10, 0.000001, 0.83, int(100/8))
#tests(100, 150, 10, 0.000001, 0.83, int(100/8))
#tests(100, 300, 10, 0.000001, 0.83, int(100/8))
#tests(100, 500, 10, 0.000001, 0.83, int(100/8))









