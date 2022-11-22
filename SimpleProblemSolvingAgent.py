import search

def print_results(str, results):
    print(str)
    print(f"\t Cost: {results.path_cost}")

    print("\t Cities: ")
    for n in results.path():
        print(n.state, end=", ")
    print()

class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        self.state = percept

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        bfs=search.best_first_graph_search(problem,lambda n: problem.h(n))
        astar=search.astar_search(problem)
        hill=search.hill_climbing(problem)
        #sa=search.simulated_annealing(problem, search.exp_schedule())

        print_results('Best-First Search',bfs)
        print_results('A* Search', astar)
        print_results('Hill climbing Search', hill)
        #print_results('Simulated annealing', sa)

