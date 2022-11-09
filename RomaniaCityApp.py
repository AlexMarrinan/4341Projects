import SimpleProblemSolvingAgent


def main():
    answer = input('Should I read read the romania map (Y/N): ')
    if answer == 'Y':
        map = create_map().nodes()
        print(map)
        while (True):
            city1 = input('Please enter city 1: ')
            city2 = input('Please enter city 2: ')
            #city1='Arad'
            #city2 = 'Iasi'
            #print(map.index(city1))
            #print(map.index(city2))
            if city1 == city2:
                print("The cities you entered are the same. Please enter different cities.")
            elif not map.__contains__(city1):
                print(f"{city1} is not on the map. Please enter valid cities")
            elif not map.__contains__(city2):
                print(f"{city2} is not on the map. Please enter valid cities")
            else:
                find_path()
                break;
    else:
        pass

def find_path():
    print("Valid Cities")
def create_map():
    romania_map = SimpleProblemSolvingAgent.UndirectedGraph(dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99),
        Hirsova=dict(Urziceni=98),
        Iasi=dict(Vaslui=92, Neamt=87),
        Lugoj=dict(Timisoara=111, Mehadia=70),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97),
        Rimnicu=dict(Sibiu=80),
        Urziceni=dict(Vaslui=142)))
    romania_map.locations = dict(
        Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
        Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
        Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
        Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
        Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
        Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
        Vaslui=(509, 444), Zerind=(108, 531))
    return romania_map


if __name__ == "__main__":
    main()
