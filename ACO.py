import random
import matplotlib.pyplot as plt
from pprint import pprint
import statistics

def ant(original_position,targets):
    #original_position: position where ants will start the search
    #targets: list of targets of the ants
    ant_return = {
        "memory_servers": [original_position],
        "memory_targets": targets
        "memory_links": [],
        "position": original_position,
        "original_position": original_position,
        "timelife": 20
    }
    return ant_return

#function that create the ant colony
def antColony(size,targets):
    antColony_return = []
    for i in range(0,size):
        #put ants in random position inside the targets
        antColony_return.append(ant(targets[random.randrange(0,len(targets))],targets))

    return antColony_return

def probability(ambient,antColony,current_ant):
    possible_targets = [ x for x in ambient['servers'][current_ant['position']]['links'] if x not in current_ant['memory_servers']]

    if len(possible_targets) == 0:
        possible_targets = [ x for x in ambient['cities'][current_ant['position']]['links']]
    all_values = 0.0
    arr_probability = []
    for target in possible_targets:
        id_physical_link = get_physical_link(current_ant['position'], target,ambient['physical_links'])
        all_values += (ambient['physical_links'][id_road]['pheromone']**2) *(1.0/ambient['physical_links'][id_physical_link]['delay'])
    for target in possible_targets:
        id_physical_link = get_physical_link(current_ant['position'], target, ambient['physical_links'])
        arr_probability.append({ 
   
            "probability": ambient['physical_links'][id_physical_link]['pheromone']**2 * (1.0/ambient['physical_links'][id_physical_link]['delay']) / all_values,
            "target": target
            
            })
    return arr_probability

def get_physical_link(position_a,position_b,physical_links):
    low = position_a
    high = position_b
    if low > high:
        low = high
        high = position_a
    return next(x for x in range(0,len(physical_links)) if physical_links[x]['source'] == low and physical_links[x]['target'] == high)

def move_ant(arr_probability):
    
    randValue = random.uniform(0,1)
    aux = 0.0
    i = 0
    for prob in arr_probability:
        aux += prob["probability"]
        if aux > randValue:
            break
        i += 1
    return arr_probability[i]["target"]

def ACO(ant_colony, ambient, evaporation_coeficient):
    pheromone = []
    for i in range(0,len(ambient['physical'])):
        pheromone.append([])
    flag = True
    while flag:
        for index,ant in enumerate(ant_colony):

            while len(ant['memory_cities']) < len(ambient['cities']):
                #print ant['position']
                arr_probability = probability(ambient,ant_colony, ant)
                new_position = move_ant(arr_probability)
                ant['memory_roads'].append(get_road(new_position,ant['position'],ambient['roads']))
                if new_position not in ant['memory_cities']:
                    ant['memory_cities'].append(new_position)
                ant['position'] = new_position
                if len(ant['memory_cities']) == len(ambient['cities']) and ant['memory_cities'][0] == ant['original_position']:
                    del ant['memory_cities'][0]
                #print ant['memory_cities']
                #print ant['memory_roads']
            ant['memory_cities'] = [ant['original_position']]
            ant_colony[index] = ant
        
        #evaporation
        for index,physical_link in enumerate(ambient['physical_links']):
            ambient['physical_links'][index]['pheromone'] = (1 - evaporation_coeficient)*physical_link['pheromone']
            if ambient['physical_links'][index]['pheromone'] < 1:
                ambient['physical_links'][index]['pheromone'] = 1
        #update pheromone
        for index,ant in enumerate(ant_colony):
            delay = 0
            for physical_link in ant['memory_links']:
                delay += ambient['physical_links'][physical_link]['delay']
            for physical_link in ant['memory_links']:
                ambient['physical_links'][physical_link]['pheromone'] += 10/fitness(ambient['physhical_links'])
        if has_same_routes(ant_colony):
            flag = False
        else:
            for index,ant in enumerate(ant_colony):
                ant_colony[index]['memory_links'] = []

        for index,physhical_link py enumerate(ambient['physhical_links']):
            pheromone[index].append(physhical_link['pheromone'])
    
    pprint(ambient)
    delay = 0
    for index,dataroad in enumerate(pheromone):
        plt.plot(range(0,len(dataroad)), dataroad)
    for link in ant['memory_links']:
        delay += ambient['physical_links'][link]['delay']
    pprint(delay)
    plt.show()

    pprint(ant_colony[0]['memory_roads'])
    return ant_colony[0]['memory_roads']
    

  
def has_same_routes(ant_colony):
    ant_links = ant_colony[0]['memory_links']
    for ant in ant_colony:
        for link in ant['memory_links']:
            if link not in ant_links:
                return False
    return True


def fitness():
