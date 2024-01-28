import util
from util import Stack
from util import Queue
from util import PriorityQueue

class DFS(object):
    def depthFirstSearch(self, problem):
        """
        Search the deepest nodes in the search tree first
        [2nd Edition: p 75, 3rd Edition: p 87]

        Your search algorithm needs to return a list of actions that reaches
        the goal.  Make sure to implement a graph search algorithm
        [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** TTU CS5368 YOUR CODE HERE ***"
        Data = Stack()
        List = []
        Null = []
        if Data!=Null:
            StartState = problem.getStartState()
            Data.push((StartState, Null))
        while Data:
            Node, Movements = Data.pop()
            if problem.isGoalState(Node):
                return Movements
            elif Node not in List:
                Current = problem.getSuccessors(Node)
                List.append(Node)
                for successor, action, stepCost in Current:
                    Next_step = Movements + [action]
                    Data.push((successor, Next_step))
        util.raiseNotDefined()
        

class BFS(object):
    def breadthFirstSearch(self, problem):
        "*** TTU CS5368 YOUR CODE HERE ***"
        Data = Queue()
        List = []
        Null = []
        if Data!=Null:
            StartState = problem.getStartState()
            Data.push((StartState, Null))
        while Data:
            Node, Movements = Data.pop()
            if problem.isGoalState(Node):
                return Movements
            elif Node not in List:
                Current = problem.getSuccessors(Node)
                List.append(Node)
                for successor, action, stepCost in Current:  
                    Next_step = Movements + [action]
                    Data.push((successor, Next_step))
        util.raiseNotDefined()

class UCS(object):
    def uniformCostSearch(self, problem):
        "*** TTU CS5368 YOUR CODE HERE ***"
        Data = PriorityQueue() 
        Null_0 = []
        Null_1 = [] 
        List = []
        visited = [] 
        if Data!=Null_0:
            StartState = problem.getStartState()
            Data.push((StartState, Null_0), Null_1)
        while Data:
            Node, Movements = Data.pop()
            if problem.isGoalState(Node):
                return Movements
            elif Node not in List:
                Current = problem.getSuccessors(Node)
                List.append(Node)
                for successor, action, stepCost in Current:
                    Next_step = Movements + [action]
                    if successor not in visited:
                        CostofActions = problem.getCostOfActions(Next_step)
                        Data.push((successor,Next_step),CostofActions)
        util.raiseNotDefined()
        
class aSearch (object):
    def nullHeuristic( state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0
    def aStarSearch(self,problem, heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        "*** TTU CS5368 YOUR CODE HERE ***"
        Data = PriorityQueue() 
        Null_0 = []
        Null_1 = [] 
        List = []
        visited = [] 
        if Data!=Null_0:
            StartState = problem.getStartState()
            Data.push((StartState, Null_0), Null_1)
        while Data:
            Node, Movements = Data.pop()
            
            if problem.isGoalState(Node):
                return Movements
            elif Node not in List:
                Current = problem.getSuccessors(Node)
                List.append(Node)
                for successor, action, cost in Current:
                    Next_step = Movements + [action]
                    if successor not in visited:
                        CostofActions = problem.getCostOfActions(Next_step)
                        Heuristic_value = heuristic(successor,problem) 
                        Cost = CostofActions + Heuristic_value
                        Data.push((successor,Next_step),Cost)
        util.raiseNotDefined()

