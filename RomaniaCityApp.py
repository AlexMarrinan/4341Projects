import SimpleProblemSolvingAgent
import search


def main():
    # answer = input('Should I read the romania map (Yes/No): ')
    answer = 'Yes'
    if answer == 'Yes':
        map = create_map('romania_map')
        print(map.nodes())
        while (True):
            # city1 = input('Please enter city 1: ')
            # city2 = input('Please enter city 2: ')
            city1 = 'Arad'
            city2 = 'Bucharest'
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
    agent.seq = map
    print(agent.state)
    problem = search.Problem(city1, city2)
    # agent.__dict__=map;
    bfsCost = 0
    # problem.path_cost(bfsCost,city1,,city2)
    print("Best-First Search")
    print(f"\t Cost: {bfsCost}")
    print("\t Cities:")
    print("A* Search")
    print("\t Cost: ")
    print("\t Cities:")


def create_map(filepath):
    graph = search.Graph()
    file = open(filepath)
    graph.make_undirected()
    for i in file.readlines():
        vals = i.split()
        graph.connect(vals[0], vals[1], vals[2])
    return graph


if __name__ == "__main__":
    main()
