import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

G.add_nodes_from(['h1','h2','h3','h4','h5','h6','h7','h8'],color="blue")
G.add_nodes_from(['s1','s2','s3','s4','s5','s6'],color="blue")

G.add_edges_from([('h1','s1'),('h2','s1'),('h3','s2'),('h4','s2'),('h5','s5'),('h6','s5'),('h7','s6'),('h8','s6')],color="blue")
G.add_edges_from([('s1','s3'),('s3','s5'),('s2','s4'),('s4','s6'),('s1','s4'),('s3','s6'),('s2','s3'),('s4','s5')],color="blue")

nx.draw(G,with_labels=True)
plt.savefig("Topo1-1.png")
plt.show(G)

ShortestPath = ['h4','s2','s4','s6','h8']
G.add_nodes_from(ShortestPath,color='red')
for i in ShortestPath[:-1]:
    G.add_edge(i,ShortestPath[ShortestPath.index(i)+1],color='red')

Edge1 = [(u, v) for (u, v, d) in G.edges(data=True) if d['color'] =='red']
Edge2 = [(u, v) for (u, v, d) in G.edges(data=True) if d['color'] =='blue']
Node1 = [(u) for (u, d) in G.nodes(data=True) if d['color'] =='red']
Node2 = [(u) for (u, d) in G.nodes(data=True) if d['color'] =='blue']

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos,nodelist=Node1,node_color='r')
nx.draw_networkx_nodes(G, pos,nodelist=Node2,node_color='b')

nx.draw_networkx_edges(G, pos, edgelist=Edge1,edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=Edge2,edge_color='b')

nx.draw_networkx_labels(G, pos)

plt.axis('off')
plt.show()









