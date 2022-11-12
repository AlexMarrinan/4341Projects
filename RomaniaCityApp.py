import SimpleProblemSolvingAgent
import search
from Problem import *


def main():
    answer = input('What map file should we read?: ')
    if answer != '':
        map = create_map(answer)
        while map == None:
            answer = input('What map file should we read?: ')
            map = create_map(answer)
        print(f"Loading from {answer} ...")
        map.locations = dict(
        Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
        Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
        Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
        Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
        Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
        Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
        Vaslui=(509, 444), Zerind=(108, 531))
        print(map.nodes())
        while (True):
            city1 = input('Please enter city 1: ')
            city2 = input('Please enter city 2: ')
            #city1 = 'Sibiu'
            #city2 = 'Zerind'
            if city1 == city2:
                print("The cities you entered are the same. Please enter different cities.")
            elif not map.nodes().__contains__(city1):
                print(f"{city1} is not on the map. Please enter valid cities")
            elif not map.nodes().__contains__(city2):
                print(f"{city2} is not on the map. Please enter valid cities")
            else:
                find_path(city1, city2, map)
                answer = input(f'Would you like to find the optimal path between any 2 cities again? (Yes/No): ')
                if answer.lower() != 'yes':
                    print("Thank You for Using Our App")
                    break
    else:
        print("Thank You for Using Our App")


def find_path(city1, city2, map):
    agent = SimpleProblemSolvingAgent.SimpleProblemSolvingAgentProgram(city1)
    problem = GraphProblem(city1, city2, map)

    path = agent.search(problem)
    pathList = path.path()
    #cost=problem.path_cost()
    path.path_cost

    print("A* Search")
    print(f"\t Cost: {path.path_cost}")

    print("\t Cities: ")
    for n in pathList:
        print(n.state, end=", ")
    print()


def create_map(filepath):
    graph = search.Graph()
    try:
        file = open(filepath)
    except: 
        print(f"File {filepath} not found!")
        return None
    for i in file.readlines():
        vals = i.split()
        graph.connect1(vals[0], vals[1], int(vals[2]))
        graph.connect1(vals[1], vals[0], int(vals[2]))

    #print(graph.graph_dict)
    return graph


if __name__ == "__main__":
    main()
