#!/usr/bin/env python2
import networkx as nx
import matplotlib.pyplot as plt
import copy
seq_list = ["ATGT", "TGTC", "GTCT", "TCTA", "CTAG", "TAGT", "AGTG", "GTGA", "TGAA", "GAAC", "AACG", "ACGT", "CGTA", "GTAG", "TAGG", "AGGC", "GGCC", "GCCT", "CCTG", "CTGA"]

def de_bruijn(seq):
    G = nx.DiGraph()
    k_minus1_length = len(seq[0]) - 1
    k_minus1_mers = []
    k_minus1_mers_left = []
    k_minus1_mers_right = []

# create k minus 1 mers
    for j in range(0, len(seq)):
        tmp1 = seq[j]
        left = tmp1[0:k_minus1_length]
        right = tmp1[1:k_minus1_length + 1]
        k_minus1_mers.append(left)
        k_minus1_mers.append(right)
        k_minus1_mers_left.append(left)
        k_minus1_mers_right.append(right)

    for m in range(0, len(k_minus1_mers_left)):
        tmp4 = k_minus1_mers_left[m]
        tmp5 = k_minus1_mers_right[m]
        G.add_edge(tmp4, tmp5)
    # to draw the graph run:
    # plt.figure(figsize=(8, 6))
    # nx.draw(G)
    # plt.show()
# create node for unique k -1 mer
    for n in range(0, len(k_minus1_mers)):
        tmp2 = k_minus1_mers[n]
        G.add_node(tmp2)
    return G

# eulerian path; visits every edge once, nodes can be more than once
def eulerian_path(G):

    starting_node = [n for n, d in G.in_degree() if d == 0]  # starting node would be node with zero in degree
    starting_node = starting_node[0]
    seen_edges = set()
    paths = []
    path = []
    e = list(G.out_edges(starting_node))  # tuples, all edges of first node
    e1 = e[0]

    recursive_euler(paths, path, e1, seen_edges, G)

    for path in paths:
        if len(path) >= len(G.edges):  # gets rid of short, unfinished walks, must visit every edge
            sequences = []
            sequence = ""
            p_tmp = path[0]
            last_char_seq = p_tmp[1][0]
            for i in range(1, len(path)+1):
                path_tmp = path[i-1]
                left_node = path_tmp[0]
                l_char = left_node[0]
                sequence = sequence + l_char
                if i == len(path):
                    sequence = sequence + last_char_seq
            sequences.append(sequence)
            print("Sequence is:")
            print sequence


def recursive_euler(paths, path, edge, seen_edges, G):  # continues walk until only avail edge has been seen
    if edge in seen_edges:
        paths.append(path)
        return
    seen_edges.add(edge)
    path.append(edge)
    n = edge[1]
    edges = list(G.out_edges(n))
    for e in edges:
        recursive_euler(paths, copy.deepcopy(path), e, copy.deepcopy(seen_edges), G)
    return


if __name__ == '__main__':
    de_bruijn_graph = de_bruijn(seq_list)
    eulerian_path(de_bruijn_graph)