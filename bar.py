import plotly.express as px
import pandas as pd 



df = pd.read_csv("bar_assignment.csv") 


fixed_df = df.groupby("LABEL")["COUNT"].value_counts().unstack(fill_value=0)
fixed_df.columns = ["No", "Yes"]
fixed_df.reset_index(inplace=True)


melted_df = fixed_df.melt(id_vars="LABEL", var_name="Response", value_name="Count")

fig = px.bar(
    melted_df,
    x="Count",  
    y="LABEL",
    color="Response",  
    orientation="h",
    labels={"LABEL": "Y-LABELS", "Count": "X-LABELS"},
    color_discrete_map={"No": "red", "Yes": "blue"},
    text="Count"  
)


fig.update_layout(
    font=dict(size=16, family="Arial, sans-serif"),  
    title_font=dict(size=20, family="Arial, sans-serif"), 
)

fig.show()