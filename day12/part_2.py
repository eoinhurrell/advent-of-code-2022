#!/usr/bin/env python3
from functools import partial

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

text = get_data(day=12, year=2022)

from string import ascii_lowercase

# This is messy
class Node:
    def __init__(self, v):
        assert v in ascii_lowercase
        self.v = v
        self.predecessors = set()

    def __repr__(self):
        return f"Node({self.v})"

    def add_predecessor(self, other):
        if ord(other.v) - ord(self.v) <= 1:
            other.predecessors.add(self)

start = None
end = None

def make_row(line):
    global start, end
    def process_char(c):
        global start, end
        if c == 'S':
            n = Node('a')
            start = n
            return n
        elif c == 'E':
            n = Node('z')
            end = n
            return n
        else:
            return Node(c)
    return list(map(process_char, line))

nodes = list(map(make_row, text.splitlines()))
node_queue = []
def build_graph(node_queue, nodes, i, line):
    for j in range(len(line)):
        nodes[i][j].coord = (i, j)
        if i > 0:
            nodes[i][j].add_predecessor(nodes[i-1][j])
        if i < len(nodes) - 1:
            nodes[i][j].add_predecessor(nodes[i+1][j])
        if j > 0:
            nodes[i][j].add_predecessor(nodes[i][j-1])
        if j < len(nodes[i]) - 1:
            nodes[i][j].add_predecessor(nodes[i][j+1])
        nodes[i][j].dist = 1000000000
        nodes[i][j].prev = None
        node_queue.append(nodes[i][j])

connect = partial(build_graph, node_queue, nodes)
# build the graph (this has too many side effects)
list(map(lambda item: connect(*item), enumerate(nodes)))
end.dist = 0

while len(node_queue) > 0:
    node_queue = sorted(node_queue, key=lambda x:x.dist, reverse=True)
    u = node_queue.pop()
    for v in u.predecessors:
        if v in node_queue:
            alt = u.dist + 1
            if alt < v.dist:
                v.dist = alt
                v.prev = u

print(min(n.dist for row in nodes for n in row if n.v == 'a'))
# 350
