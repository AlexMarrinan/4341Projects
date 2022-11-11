import SimpleProblemSolvingAgent
import search
from Problem import *


def main():
    # answer = input('Should I read the romania map (Yes/No): ')
    answer = 'Yes'
    if answer == 'Yes':
        map = create_map('romania_map')
        map.locations = dict(
        Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
        Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
        Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
        Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
        Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
        Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
        Vaslui=(509, 444), Zerind=(108, 531))
        #print(map.locations["Arad"])
        while (True):
            # city1 = input('Please enter city 1: ')
            # city2 = input('Please enter city 2: ')
            city1 = 'Sibiu'
            city2 = 'Sibiu'
            if city1 == city2:
                print("The cities you entered are the same. Please enter different cities.")
            elif not map.nodes().__contains__(city1):
                print(f"{city1} is not on the map. Please enter valid cities")
            elif not map.nodes().__contains__(city2):
                print(f"{city2} is not on the map. Please enter valid cities")
            else:
                find_path(city1, city2, map)
                answer = input(f'Would you like to find the optimal path between any 2 cities again? (Yes/No): ')
                if answer != 'Yes':
                    print("Thank You for Using Our App")
                    break
    else:
        print("Thank You for Using Our App")


def find_path(city1, city2, map):
    agent = SimpleProblemSolvingAgent.SimpleProblemSolvingAgentProgram(city1)
    problem = GraphProblem(city1, city2, map)

    path = agent.search(problem)

    print(path)

    pathDistance = 0
    #estimateToGoal = problem.value(city2)
    #print(search.best_first_graph_search(problem, estimateToGoal+pathDistance, agent))
    # problem.path_cost(bfsCost,city1,city2)
    print("Best-First Search")
    #print(f"\t Cost: {bfsCost}")
    print("\t Cities:")
    print("A* Search")
    print("\t Cost: ")
    print("\t Cities:")


def create_map(filepath):
    graph = search.Graph()
    file = open(filepath)
    for i in file.readlines():
        vals = i.split()
        graph.connect1(vals[0], vals[1], int(vals[2]))
        graph.connect1(vals[1], vals[0], int(vals[2]))

    print(graph.graph_dict)
    return graph


if __name__ == "__main__":
    main()
