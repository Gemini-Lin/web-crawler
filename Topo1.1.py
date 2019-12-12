
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['h1','h2','h3','h4','h5','h6','h7','h8'])
G.add_nodes_from(['s1','s2','s3','s4','s5','s6'])

G.add_edges_from([('h1','s1'),('h2','s1'),('h3','s2'),('h4','s2'),('h5','s5'),('h6','s5'),('h7','s6'),('h8','s6')])
G.add_edges_from([('s1','s3'),('s3','s5'),('s2','s4'),('s4','s6'),('s1','s4'),('s3','s6'),('s2','s3'),('s4','s5')])

nx.draw(G,with_labels=True)
plt.savefig("Topo1.png")
plt.show()
