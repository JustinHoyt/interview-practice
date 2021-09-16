from typing import *

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone_root = Node(1)
        visited_nodes: Set = set()
        nodes_map: Dict[int, Node] = {1: clone_root}
        def clone_graph(curr: Node, curr_copy: Node):
            nonlocal visited_nodes
            if curr.val in visited_nodes:
                return
            visited_nodes.add(curr.val)
            
            for i, neighbor in enumerate(curr.neighbors):
                curr_copy.neighbors.append(nodes_map.setdefault(neighbor.val, Node(neighbor.val)))

            for i, _ in enumerate(curr.neighbors):
                clone_graph(curr.neighbors[i], curr_copy.neighbors[i])


        if node is None: return None
        clone_graph(node, clone_root)
        return clone_root
        



def test_happy_path():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [one, three]
    root = one

    root_copy = Solution().cloneGraph(root)

    assert root_copy.val == root.val
    assert len(root_copy.neighbors) == len(root.neighbors)
    assert root_copy.neighbors[0].val == root.neighbors[0].val
    assert root_copy.neighbors[1].val == root.neighbors[1].val
    assert len(root_copy.neighbors[0].neighbors) == len(root.neighbors[0].neighbors)
    assert root_copy.neighbors[0].neighbors[0].val == root.neighbors[0].neighbors[0].val
    assert root_copy.neighbors[0].neighbors[1].val == root.neighbors[0].neighbors[1].val
    assert len(root_copy.neighbors[1].neighbors) == len(root.neighbors[1].neighbors)
    assert root_copy.neighbors[1].neighbors[0].val == root.neighbors[1].neighbors[0].val
    assert root_copy.neighbors[1].neighbors[1].val == root.neighbors[1].neighbors[1].val

def test_single_node():
    one = Node(1)
    root = one

    root_copy = Solution().cloneGraph(root)

    assert root_copy.val == root.val

def test_null_node():
    one = None
    root = one

    root_copy = Solution().cloneGraph(root)

    assert root_copy is None

if __name__ == "__main__":
    test_null_node()