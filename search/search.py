# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    # import code; code.interact(local=dict(globals(), **locals()))
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    initial_state = (problem.getStartState(), [])
    data_structure = util.Stack()
    data_structure.push(initial_state)
    visited = []
    while data_structure.isEmpty()==False:
        state = data_structure.pop()
        if state in visited: continue
        visited.append(state[0])
        if problem.isGoalState(state[0]):
            return state[1]
        for successor in problem.getSuccessors(state[0]):
            s_state, s_dir, s_cost = successor
            if not s_state in visited:
                data_structure.push((s_state, state[1] + [s_dir]))

def breadthFirstSearch(problem):
    initial_state = (problem.getStartState(), [])
    data_structure = util.Queue()
    data_structure.push(initial_state)
    visited = [initial_state[0]]
    while data_structure.isEmpty()==False:
        state = data_structure.pop()
        if problem.isGoalState(state[0]):
            return state[1]
        for successor in problem.getSuccessors(state[0]):
            s_state, s_dir, s_cost = successor
            if not (s_state in visited):
                visited.append(s_state)
                data_structure.push((s_state, state[1] + [s_dir]))


def uniformCostSearch(problem):
    data_structure = util.PriorityQueue()
    initial_state = (problem.getStartState(), [], 0)
    for successor in problem.getSuccessors(initial_state[0]):
        new_state = (successor[0], initial_state[1] + [successor[1]], successor[2] + initial_state[2])
        data_structure.push(new_state, new_state[2])
    visited = []
    visited.append(initial_state[0])
    while not data_structure.isEmpty():
        state = data_structure.pop()
        if problem.isGoalState(state[0]):
            return state[1]
        if state[0] not in visited:
            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            for successor in successors:
                new_state = (successor[0], state[1] + [successor[1]], successor[2] + state[2])
                data_structure.push(new_state, new_state[2])



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):   
    data_structure = util.PriorityQueueWithFunction(lambda state: state[2] + heuristic(state[0], problem))
    initial_state = (problem.getStartState(), [], 0)
    for successor in problem.getSuccessors(initial_state[0]):
        new_state = (successor[0], initial_state[1] + [successor[1]], successor[2] + initial_state[2])
        data_structure.push(new_state)
    visited = []
    visited.append(initial_state[0])    
    while not data_structure.isEmpty():
        state = data_structure.pop()
        if problem.isGoalState(state[0]):
            return state[1]
        if state[0] not in visited:
            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            for successor in successors:
                new_state = (successor[0], state[1] + [successor[1]], successor[2] + state[2])
                data_structure.push(new_state)


def learningRealTimeAStar(problem, heuristic=nullHeuristic):    
    MAXTRIALS = 10
    H = {}    
    s = problem.getStartState()
    path_to_s = {}
    path_to_s[s] = []
    actions = []
    H[s] = heuristic(s, problem)
    while not problem.isGoalState(s):
        successors = problem.getSuccessors(s)
        for successor in successors:
            successor_state = successor[0]
            H[successor_state] = H.get(successor_state) or heuristic(successor_state, problem)
        s1_state, s1_action, s1_cost = min(successors, key=lambda x: x[2] + H.get(x[0]) )
        f_s1 = s1_cost + H.get(s1_state)
        H[s] = max(H[s], f_s1)
        actions.append(s1_action)
        s = s1_state
    return actions


# Abbreviations
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
