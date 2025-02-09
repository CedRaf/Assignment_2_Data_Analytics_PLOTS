import networkx as nx
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("networks_assignment.csv", index_col=0) 

G = nx.Graph()


green_nodes = {"D", "F", "I", "N", "S"}


for node in df.index:
    color = "green" if node in green_nodes else "blue"
    G.add_node(node, color=color)  


for i, row in df.iterrows():
    for j, val in row.items():
        if val > 0: 
            G.add_edge(i, j, weight=val)


pos = nx.spring_layout(G)


edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1, color='gray'),
    hoverinfo='none',
    mode='lines'
)


node_x, node_y, node_color, node_text = [], [], [], []
for node in G.nodes(data=True):
    x, y = pos[node[0]]
    node_x.append(x)
    node_y.append(y)
    node_color.append(node[1].get('color', 'blue')) 
    node_text.append(node[0])

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text,
    marker=dict(size=15, color=node_color, line=dict(width=2, color='black')),
    textposition="top center"
)


fig = go.Figure(data=[edge_trace, node_trace])
fig.update_layout(
    title="Network Graph",
    showlegend=False,
    hovermode='closest',
    margin=dict(b=0, l=0, r=0, t=40),
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False)
)

fig.show()