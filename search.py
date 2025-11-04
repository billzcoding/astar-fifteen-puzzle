# Muhammad Mahd Zeeshan
# 2023462 CS

import heapq
def Astar(root):
    fringe = []
    evaluated_states = set()
    heapq.heappush(fringe, (root.f, root))  # Use f value for priority queue

    while fringe:
        current_node = heapq.heappop(fringe)[1]

        if current_node.is_goal():
            return current_node.get_path()

        # Check if the state has already been evaluated (visited)
        if current_node.state in evaluated_states:
            continue
            
        evaluated_states.add(current_node.state)

        for child in current_node.generate_children():
            # Check if the child state has already been evaluated (visited)
            if child.state not in evaluated_states:
                # Push the child node onto the fringe
                # Note: This is a simple implementation of A* (uniform-cost search with heuristic) 
                # that re-adds nodes to the fringe without path relaxation/update.
                # Since the heuristic is consistent (Manhattan distance), this is usually sufficient for
                # finding the optimal path for the 15 puzzle.
                heapq.heappush(fringe, (child.f, child))

    return None  # Return None if no solution is found