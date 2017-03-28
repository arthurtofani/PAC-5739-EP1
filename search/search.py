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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    initial_state = (problem.getStartState(), None, 0)
    stack = util.Stack()
    stack.push(initial_state)
    visited, parent_states = dict(), dict()
    parent_states[initial_state[0]] = None
    goal_state = depthFirstFindGoal(problem, stack, visited, parent_states)
    return path(goal_state, visited, parent_states)


def path(state, visited, parent_states):
    direction = visited[state]
    if parent_states[state]==None:
        return []
    else:
        #import code; code.interact(local=dict(globals(), **locals()))
        return path(parent_states[state], visited, parent_states) + [direction]


def depthFirstFindGoal(problem, stack, visited, parent_states):
    while stack.isEmpty()==False:
        state, direction, cost = stack.pop()
        if state in visited:
            continue
        visited[state] = direction
        if problem.isGoalState(state):
            return state
        for successor in problem.getSuccessors(state):
            successor_state = successor[0]
            if not (successor_state in visited):
                parent_states[successor[0]] = state
                stack.push(successor)
    return None


def breadthFirstSearch(problem):
    initial_state = (problem.getStartState(), None, 0)
    queue = util.Queue()
    queue.push(initial_state)
    visited, parent_states = dict(), dict()
    parent_states[initial_state[0]] = None
    goal_state = breadthFirstFindGoal(problem, queue, visited, parent_states)
    return path(goal_state, visited, parent_states)

def breadthFirstFindGoal(problem, queue, visited, parent_states):
    while queue.isEmpty()==False:
        state, direction, cost = queue.pop()
        if state in visited:
            continue
        visited[state] = direction
        if problem.isGoalState(state):
            return state
        for successor in problem.getSuccessors(state):
            successor_state = successor[0]
            if not (successor_state in visited):
                parent_states[successor_state] = state
                queue.push(successor)
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...


# Abbreviations
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar