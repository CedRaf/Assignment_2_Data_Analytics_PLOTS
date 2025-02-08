import pandas as pd
import plotly.graph_objects as go
import plotly.express as px 

ds = pd.read_csv("sankey_assignment.csv")

sources = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
labels = ds["LABEL"].unique().tolist()
targets = ['Reg', 'Aca', 'Oth']

unique = sources + labels + targets

def get_index(label): 
    return unique.index(label)

sourcesNDX = []
targetsNDX = []
values = []

for _, row in ds.iterrows():
    for col in sources:
        if row[col] > 0:
            sourcesNDX.append(get_index(col))
            targetsNDX.append(get_index(row["LABEL"]))
            values.append(row[col])


for _, row in ds.iterrows():
    for col in targets:
        if row[col] > 0:
            sourcesNDX.append(get_index(row["LABEL"]))
            targetsNDX.append(get_index(col))
            values.append(row[col])


node_colors = [
    px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]
    for i in range(len(unique))
]

link_colors = [node_colors[s] for s in sourcesNDX]

figure = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=unique,
        color=node_colors
    ),
    link=dict(
        source=sourcesNDX,
        target=targetsNDX,
        value=values,
        color=link_colors
    )
))

figure.show()



