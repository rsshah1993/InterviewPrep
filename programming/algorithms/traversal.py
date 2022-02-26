"""
Tree and graph traversal

Graphs: Graphs are a class of abstract data types that model the relationships between data.
Formally, a graph G = (V, E) consists of a set of vertices V and a set of edges E. Graphs
can model real-world artifacts like maps by representing intersections or places as vertices
and the roads connecting places as edges, where a graph problem might be to return the
shortest path between two places.

Trees: Special case of graph where there is only one path between any two vertices.
    Satisfies:
        connectivity - every vertex can reach every other vertex
        acyclic - No cycles; no sequence of unique edges starting at a vertex and
            returning to the same vertex.

"""
from typing import Optional, List


class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def construct_tree(graph, tree=TreeNode(), cur_node=0):
    if cur_node not in graph.keys():
        tree.data = cur_node
        return tree

    tree.data = cur_node

    tree.left = construct_tree(
        graph=graph, tree=TreeNode(), cur_node=graph[cur_node][0])

    tree.right = construct_tree(
        graph=graph, tree=TreeNode(), cur_node=graph[cur_node][1])

    return tree


def depth_first_search(tree: Optional[TreeNode], acc=list()):
    if tree is None:
        return acc
    acc.append(tree.data)
    acc = depth_first_search(tree.left, acc=acc)
    acc = depth_first_search(tree.right, acc=acc)

    return acc


def breadth_first_search(tree: Optional[TreeNode]):
    visited = list()
    queue = list()
    queue.append(tree)
    while queue:
        m = queue.pop(0)
        if m.left is not None:
            queue.append(m.left)
        if m.right is not None:
            queue.append(m.right)
        visited.append(m.data)

    return visited


def in_order_traversal(tree: Optional[TreeNode], acc: List[int] = list()) -> List[int]:
    if tree is None:
        return acc

    acc = in_order_traversal(tree.left, acc=acc)
    acc.append(tree.data)
    acc = in_order_traversal(tree.right, acc=acc)

    return acc

def post_order_traversal(tree: Optional[TreeNode], acc: List[int] = list()) -> List[int]:
    if tree is None:
        return acc
    acc = post_order_traversal(tree.left, acc=acc)
    acc = post_order_traversal(tree.right, acc=acc)
    acc.append(tree.data)
    return acc

# from leetcode:
def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Check for valid binary search tree. In this case
    a valid tree is when all nodes on a left branch are less than the
    node value, and all nodes on a right branch are greater than the node
    value.

    We keep track of this by specifying a range that the a node must fall within.
    If we take a left branch, values must be less than the current node value
    so we specify that as the upper range. Similarly for a right branch where
    we set the minimum of the range to the current nodes value.
    """
    def validate(node: TreeNode, greater_than: float, less_than: float) -> bool:
        if node is None:
            return True

        elif greater_than < node.data < less_than:
            left = validate(node.left, less_than=node.data,
                            greater_than=greater_than)
            # don't have to validate the entire tree if
            # left branch is invalid
            if not left:
                return left

            right = validate(node.right, less_than=less_than,
                             greater_than=node.data)
            return right

        else:
            return False

    return validate(root, greater_than=float("-inf"), less_than=float("inf"))


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Inverting binary search tree """
    if root is None:
        return

    left = invertTree(root=root.right)
    right = invertTree(root=root.left)
    root.left = left
    root.right = right

    return root


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        6: [9, 10],
        5: [7, 8]
    }
    tree = construct_tree(graph=graph, tree=TreeNode(), cur_node=0)
    print("DFS: ", depth_first_search(tree=tree))
    print("BFS: ", breadth_first_search(tree=tree))
    print("In Order: ", in_order_traversal(tree=tree))
    print("Post Order: ", post_order_traversal(tree=tree))
