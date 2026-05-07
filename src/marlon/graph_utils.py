import networkx as nx
import matplotlib.pyplot as plt
import os

def plot_network_state(state):
    G = nx.Graph()

    for i, compromised in enumerate(state):
        G.add_node(i, compromised=bool(compromised))

    for i in range(len(state) - 1):
        G.add_edge(i, i + 1)

    colors = ["red" if G.nodes[n]["compromised"] else "green" for n in G.nodes]

    plt.figure()
    nx.draw(G, with_labels=True, node_color=colors)
    plt.title("Attacker vs Defender Network State")

    os.makedirs("results", exist_ok=True)
    plt.savefig("results/network_state.png")
    plt.close()

    print("Graph saved to: results/network_state.png")
