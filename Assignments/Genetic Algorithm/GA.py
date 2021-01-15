import csv
import numpy as np
import matplotlib.pyplot as plt
import random
#============================

filename = "data1.csv"

#random.seed = 10
history = []
last_play = []

plays = ['R', 'P', 'S']
population = 16
gene_size = 81
generations = 5

global mutation_chance
mutation_chance = 32/81
#(population - 2) / (population)#+generations/2)
#============================

with open(filename) as CSV:
    reader = csv.reader(CSV, delimiter=',')
    for row in reader:
        history.append(row[0])
        last_play.append(row[1])

BFS = list()
for i in plays:
    for j in plays:
        for k in plays:
            for l in plays:
                hold = str(i+j+k+l)
                BFS.append(hold)

#============================

def play_value(Opp_move, agent_move):
    if Opp_move == "R":
        if agent_move == "R":
            return 0
        elif agent_move == "P":
            return 1
        else:
            return 0
    elif Opp_move == "P":
        if agent_move == "P":
            return 0
        elif agent_move == "S":
            return 1
        else:
            return 0
    elif Opp_move == "S":
        if agent_move == "S":
            return 0
        elif agent_move == "R":
            return 1
        else:
            return 0

#============================
#All code above works

class actor():
    def __init__(self, genes = []):
        self.genes = genes
        if len(self.genes) == 0:
            self.gen_genes()
        self.fitness = 0

    def gen_genes(self):
        for x in range(0,81):
            self.genes.append(np.random.choice(['R', 'P', 'S']))
        print(self.genes)

    def return_gene(self, index):
        return self.genes[index]

    # returns a deep copy of gene-object sequence
    def return_entire_gene(self):
        copy = list()
        for x in self.genes:
            copy.append(x)
        return copy

    def return_fitness(self):
        return self.fitness

    # add to the fitness of the agent
    def add_fitness(self, add=0):
        self.fitness += add
        return

    def clear_fitness(self):
        self.fitness = 0
        return

    def set_genes(self, genes):
        self.genes = genes
        return

#===========================
#initiliaze GA class and generate each actor with a random 81 string chromosone list
class genetic_algorithm():
    def __init__(self, population):
        self.actors = list()
        self.fitness_values = list()
        self.population = population
        for x in range(self.population):
            self.actors.append(actor([]))
#Above all works
    #Generate acts as a wrapper function calling the different parts of the GA
    def generate(self, gener):
        global mutation_chance
        gener
        avg = []
        best = []
        for _ in range(gener):

            #Call each stage of the GA
            self.fitness()
            self.Selection()
            self.tournament()
            self.crossover()
            self.mutation()

            avg.append(self.avg_fitness())
            best.append(self.best_fitness())

            for z in range(len(self.actors)):
                self.actors[z].clear_fitness()

            print("Generation: "+str(_))

            #mutation_chance -= 1/27

        # Display run results
        self.results(avg, best, gener)
        self.textfile(self.best_seq())
        return

    #revision 2/3/2020
    def fitness(self):
        gene_count = 0

        #Starting at RRRR (== Gene 0) go through each gene
        for seq in BFS:
            count = 0
            #Keeps track in textfile of index location
            count_last_play = 0
            #Seq in current line of textfile
            for hist in history:
                count += 1
                # When the current gene's sequence matches the line in the textfile
                if seq == hist:
                    # Iterate through each member
                    for act in self.actors:
                        #The move the textfile played versus the member is compared and valued via play value
                        act.add_fitness(play_value(last_play[count_last_play], act.return_gene(gene_count)))
                count_last_play += 1
                if count == 100000:
                    break
            gene_count += 1
        return

    def Selection(self):
        #take top half of population as reproducing candidates
        self.actors.sort(key = lambda actor: actor.fitness, reverse = True)
        elite = []
        self.population = int(self.population / 2)
        for i in range(self.population):
            elite.append(self.actors[i])
        self.actors = elite

    # Code above should all work

    # Tournament play with weighted win probabilty
    def tournament(self):
        losers = []
        losers_hold = []
        # The players are removed from winners as they are eliminated
        winners = self.actors
        random.shuffle(self.actors)
        while len(winners) != 1:
            for i in range(0, len(winners), 2):
                p1 = winners[i]
                p2 = winners[i+1]

                # weighted probability
                p_p1 = p1.return_fitness() / (p1.return_fitness() + p2.return_fitness())
                p_p2 = p2.return_fitness() / (p1.return_fitness() + p2.return_fitness())

                prob = [p_p1, p_p2]
                # to not break the for loop, the indices are stored and the
                # items are removed after all the iterations of a round complete
                if random.choices([0,1], prob) == 0:
                    losers.append(p2)
                else:
                    losers.append(p1)

            for k in losers:
                winners.pop(winners.index(k))
            losers_hold.extend(losers)
            losers.clear()
        # elements are placed into losers in the order they lose in the tournament
        losers_hold.extend(winners)
        # the winner is then added last and the entire list is flipped to give tournament order
        losers_hold.reverse()
        self.actors.clear()

        for i in range(int(self.population/2)):
            self.actors.append(losers_hold[i])
        self.population = int(self.population/2)
        return

    #===================================================================================

    #Simple crossover styles are applied here (50/50, checkered - both children kept- no metrics to choose genes)
    def crossover(self):
        children = list()
        l = 0
        #Cross over between actor and neighboring actor
        while l in range(self.population):
            #first half from first parent
            genome = self.actors[l].return_entire_gene()[0:41]
            #second half from second parent
            genome.extend(self.actors[l+1].return_entire_gene()[41:82])

            #Create first child
            child = actor(genome)
            #call alternate mutation
            #child.set_genes(self.mutation(child.return_entire_gene()))
            children.append(child)

            # first half of second parent
            genome = self.actors[l+1].return_entire_gene()[0:41]
            # second half of first parent
            genome.extend(self.actors[l].return_entire_gene()[41:82])
            l+=2

            #Create Second child
            child = actor(genome)
            #call alternate mutation
            #child.set_genes(self.mutation(child.return_entire_gene()))
            children.append(child)

            #print(children[0].return_entire_gene())
            #print(children[1].return_entire_gene())

        self.actors.extend(children)
        self.population = len(self.actors)

        #==================================================================


        return

    #revise because I lack vision 22/02/2020
    def mutation(self, seq = []):

        # generate a 1 or 0 dependant on the mutation probability defined above
        prob = [mutation_chance, 1-mutation_chance]
        options = [1, 0]
        if seq == []:
            #A method to generate a random value
            if random.choices(options, prob):
                print("Mutation")
                x = random.randrange(0, self.population/2)
                for i in range(x):
                    #Choose a member to edit
                    actor_edit = random.randrange(0, self.population)
                    #Choose a random amount of genes to edit
                    how_many = random.randrange(0, 42)
                    seq = self.actors[actor_edit].return_entire_gene()
                    for i in range(how_many):
                        #Randomize a random gene
                        j = random.randrange(0, 81)
                        seq[j] = np.random.choice(['R', 'P', 'S'])
                        #Overwrite the object at the random chosen spot
                        hold = actor(seq)
                        hold.add_fitness(self.actors[actor_edit].return_fitness())
                        self.actors[actor_edit] = hold
                        #print("New object:" +str(hold.return_fitness()))
                        return
        else:
            rpsr = ['R', 'P', 'S', 'R']
            for x in range(81):
                opt = random.choices(options, prob)
                if opt==[1]:
                    #print("Mutation 2")
                    seq[x] = rpsr[rpsr.index(seq[x])+1]
            return seq


    #====================================================================================

    #Evaluate the fitness of a generation
    #Average fitness of generation N
    def avg_fitness(self):
        avg = 0
        for act in self.actors:
            avg += act.return_fitness()
        avg = avg/self.population
        return avg

    #Best fitness recipient of generation N
    def best_fitness(self):
        best = 0
        for act in self.actors:
            if best<act.return_fitness():
                best = act.return_fitness()
        return best

    def best_seq(self):
        best = 0
        ret = []
        for act in self.actors:
            if best<act.return_fitness():
                best =  act.return_fitness()
                ret = act.return_entire_gene()
        return ret

    #Display results
    def results(self, top = [], avg = [], generations = 0):
        plt.title("Top fitness and Average fitness for "+ str(generations) + " generations", size = 18)
        plt.xlabel("Number of generations", size = 18)
        plt.ylabel("Top fitness and Average fitness", size = 18)
        plt.grid(1)
        generations = np.arange(0, len(avg), 1)
        plt.plot(generations, avg)
        plt.plot(generations, top)
        plt.show()
        return

    def textfile(self, data = []):
        with open("sequence.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

print("Prepare to crash")
GA = genetic_algorithm(population)
GA.generate(generations)
print("No crash")
print(str(GA.best_fitness()))



