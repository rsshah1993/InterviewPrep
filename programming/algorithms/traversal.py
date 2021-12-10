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
from typing import Optional


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


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        6: [7, 9],
        5: [8, 10]
    }
    tree = construct_tree(graph=graph, tree=TreeNode(), cur_node=0)
    print(depth_first_search(tree=tree))
    print(breadth_first_search(tree=tree))
