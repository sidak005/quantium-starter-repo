import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv("data/processed_sales.csv")

df["date"] = pd.to_datetime(df["date"])

# line chart
fig = px.line(
    df.sort_values("date"),
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time"
)

fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", width=2, dash="dash")
)

fig.add_annotation(
    x="2021-01-15",
    y=1,
    yref="paper",
    text="Price Increase",
    showarrow=False,
    font=dict(color="red"),
    xanchor="left"
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales visualiser", style={'textAlign': 'center'}),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    ),

    html.P("Q: Were sales higher before or after the price increase on Jan 15, 2021?",
           style={'textAlign': 'center', 'fontStyle': 'italic'})
])

if __name__ == "__main__":
    app.run(debug=True)
