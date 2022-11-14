import SimpleProblemSolvingAgent
import search
import json
from Problem import *


def main():
    answer = input('Would you like to read the romainia map? (Yes/No):  ')
    if answer.lower() == 'yes':
        map = create_map("romania_map.json")
        print(f"Loading from romania_map ...")
        while (True):
            city1 = input('Please enter city 1: ')
            city2 = input('Please enter city 2: ')
            if city1 == city2:
                print("The cities you entered are the same. Please enter different cities.")
            elif not map.nodes().__contains__(city1):
                print(f"{city1} is not on the map. Please enter valid cities")
            elif not map.nodes().__contains__(city2):
                print(f"{city2} is not on the map. Please enter valid cities")
            else:
                '''If the cities inputted are valid find the cost between cities and the path between them'''
                find_path(city1, city2, map)
                answer = input(f'Would you like to find the optimal path between any 2 cities again? (Yes/No): ')
                if answer.lower() != 'yes':
                    print("Thank You for Using Our App!")
                    break
    else:
        print("Thank You for Using Our App!")

'''Finds the optimal path between 2 cities in map using the A* search algorithm'''
def find_path(city1, city2, map):
    agent = SimpleProblemSolvingAgent.SimpleProblemSolvingAgentProgram(city1)
    problem = GraphProblem(city1, city2, map)

    path = agent.search(problem)
    pathList = path.path()

    print("A* Search")
    print(f"\t Cost: {path.path_cost}")

    print("\t Cities: ")
    for n in pathList:
        print(n.state, end=", ")
    print()


'''Reads values in file and translates that to map links'''
def create_map(filepath):
    try:
        file = open(filepath)
    except:
        print(f"File {filepath} not found!")
        return None
    data = json.load(file)

    graphData = data["graph"]
    locationsData = data["locations"]

    graph = search.Graph(graphData, False)
    graph.locations = locationsData

    return graph


if __name__ == "__main__":
    main()
