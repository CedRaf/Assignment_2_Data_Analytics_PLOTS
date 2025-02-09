import plotly.express as px
import pandas as pd 



df = pd.read_csv("bar_assignment.csv") 


fixed_df = df.groupby("LABEL")["COUNT"].value_counts().unstack(fill_value=0)
fixed_df.columns = ["No", "Yes"]
fixed_df.reset_index(inplace=True)


fig = px.bar(
    fixed_df,
    x=["No", "Yes"], 
    y="LABEL",
    orientation="h", 
    labels={"LABEL": "Y-LABELS", "value": "X-LABELS"}
 
)


fig.update_layout(
    font=dict(size=16),  
    title_font=dict(size=20),  
)


fig.show()

# fixed_df.to_excel("transformed_df.xlsx", index=False)