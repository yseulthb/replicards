"""


"""

import copy
import random
import numpy as np
import matplotlib.pyplot as plt


class Organism:
    
    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness
        
    def reproduce(self):
        num_of_offspring = np.random.poisson(self.fitness)
        offspring = []
        for i in range(num_of_offspring):
            offspring.append(copy.deepcopy(self))
        return offspring

class Report:
    
    def __init__(self, population):
        
        # Generation number
        self.gen = 0
        
        # Lineages
        self.names = list(set([org.name for org in population]))
        self.names.sort()
        
        # Fixation: whether or not one lineage reached fixation
        self.fixation = None
        
        # Initialize counts dictionary
        self.counts = dict({})
        for name in self.names:
            self.counts[name] = []
        
        # Initial counts
        self.update_counts(population)
    
    def get_org_names(self, population):
        ''' Returns a list with the names of each organism. '''
        return [org.name for org in population]
    
    def update_counts(self, population):
        org_names = self.get_org_names(population)
        for name in self.names:
            self.counts[name].append(org_names.count(name))
        self.gen += 1
        if len(set(org_names)) == 1:
            self.fixation = True
    
    def get_latest_counts(self):
        latest = dict({})
        for name in self.names:
            latest[name] = self.counts[name][-1]
        return latest
    
    def plot_evolution(self):
        for name in self.names:            
            plt.plot(self.counts[name], label=name)
        plt.xticks(list(range(self.gen + 1)))
        plt.legend()
        plt.show()


def create(org_name, fitness, n):
    ''' Creates `n` organisms with name `org_name` and specified `fitness`. '''
    return [Organism(org_name, fitness) for i in range(n)]
