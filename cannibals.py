
class State():
    def __init__(self, cannibalLeft, missionaryLeft, boatMovement, cannibalRight, missionaryRight, boatCannibal, boatMissionary):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boatMovement = boatMovement
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.boatCannibal = boatCannibal
        self.boatMissionary = boatMissionary
        self.parent = None

    def is_goal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
               and self.boatMovement == other.boatMovement and self.cannibalRight == other.cannibalRight \
               and self.missionaryRight == other.missionaryRight

def actions(cur_state):
    valid_actions = []
    if cur_state.boatMovement == 'left':

        ## Two missionaries.
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                          cur_state.cannibalRight, cur_state.missionaryRight + 2, 0, 2)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## Two cannibals.
        new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                          cur_state.cannibalRight + 2, cur_state.missionaryRight, 2, 0)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One missionary and one cannibal.
        new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                          cur_state.cannibalRight + 1, cur_state.missionaryRight + 1, 1, 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One missionary.
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                          cur_state.cannibalRight, cur_state.missionaryRight + 1, 0, 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One cannibal.
        new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                          cur_state.cannibalRight + 1, cur_state.missionaryRight, 1, 0)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

    else:

        ## Two missionaries
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                          cur_state.cannibalRight, cur_state.missionaryRight - 2, 0, 2)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## Two cannibals.
        new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                          cur_state.cannibalRight - 2, cur_state.missionaryRight, 2, 0)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One missionary and one cannibal.
        new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                          cur_state.cannibalRight - 1, cur_state.missionaryRight - 1, 1, 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One missionary crosses.
        new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                          cur_state.cannibalRight, cur_state.missionaryRight - 1, 0, 1)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

        ## One cannibal.
        new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                          cur_state.cannibalRight - 1, cur_state.missionaryRight, 1, 0)
        if new_state.is_valid():
            new_state.parent = cur_state
            valid_actions.append(new_state)

    return valid_actions

def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0, 0, 0)
    vertices = list()
    vertices.append(initial_state)

    while vertices:
        state = vertices.pop(0)

        # Loops through the vertices list until the end goal is reached
        if state.is_goal():
            return state

        for item in actions(state):
            if item not in vertices:
                vertices.append(item)

    return None

def backtrace_graph(solution):
    print("Boat Starting")
    path_state = []

    path_state.append(solution)
    parent = solution.parent

    while parent:
        path_state.append(parent)
        parent = parent.parent

    for item in range(len(path_state)):
        state = path_state[len(path_state) - item - 1]



        print("Boat moving in {} the direction, taking {} Cannibals and {} missionary".
                format(state.boatMovement, state.boatCannibal, state.boatMissionary))
        print("{} Cannibals and {} Missionaries on the left side of bank".format(state.cannibalLeft, state.missionaryLeft))
        print("{} Cannibals and {} Missionaries on the right side of bank".format(state.cannibalRight, state.missionaryRight))


        print("--------------------------------------------------------")
        print("--------------------------------------------------------")

def boat_start():
    graph = breadth_first_search()
    backtrace_graph(graph)

if __name__ == "__main__":
    boat_start()
