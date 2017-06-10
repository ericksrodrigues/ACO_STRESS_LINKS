import random
def generateCities(totalCities):
    maxDistanceCity = 20
    cities = []
    roads = []
    id_connections = 0
    for i in range(0,totalCities):
        cities.append({
            "id": i,
            "target_cities": []
        })
    for i in range(0, totalCities):
        for j in range(0,totalCities):
            if i != j:
                cities[i]['target_cities'].append(j)
                if i < j:
                    roads.append({"id":id_connections, "source": i,"target": j, "distance": random.randint(1,maxDistanceCity), "pheromone": 1.0})
                    id_connections += 1
    return {
        "cities": cities,
        "roads": roads
    }

def getAmbient(file_directory):
    return : {
        "servers": parser(file_directory),
        "physical_links": parserLinks(file_directory)
    }

def parserLinks(file_directory):
    """Receive a path name and returns the list of links"""
    rnp_json_file_path = file_directory
    rnp_json_file = open(rnp_json_file_path, "r")
    rnp_json = json.load(rnp_json_file)
    rnp_links = rnp_json["links"]
    ret = []
    aux_id = 0
    for link in rnp_links:
        ret.append({
                "id": aux_id,
                "server_low": link["source"],
                "server_high": link["target"],
                "virtual_networks": [],
                "band": link["LinkSpeedRaw"],
                "originBand": link["LinkSpeedRaw"],
                "delay": random.randint(1,20),
                "pheromone": 1
            })
        aux_id += 1
    return ret                

def parser(file_directory):
    """Receive a path name and returns the list of nodes"""
    rnp_json_file_path = file_directory
    rnp_json_file = open(rnp_json_file_path, "r")
    rnp_json = json.load(rnp_json_file)
    rnp_nodes = rnp_json["nodes"]
    retorno = []
    for node in rnp_nodes:
    #Capture nodes
        retorno.append({
            "no": node["label"],
            "id": node["id"],
            "links": [] #which others servers that this server has connection
            
        })
    #capture links
    for link in rnp_json["links"]:
        retorno[link['source']]['links'].append(link['target'])
        retorno[link['target']]['links'].append(link['source'])
    return retorno

def getRandomRequest(topology_size,request_size){
    request = []
    while request_size > 0:
        aux = random.randint(1,topology_size)
        if aux not in request:
            {request.append(aux2)
            request_size -= 1}
}