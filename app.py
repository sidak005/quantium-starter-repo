import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value="all",
        inline=True,
        style={'textAlign': 'center', 'marginBottom': '20px'}
    ),

    dcc.Graph(id="sales-chart"),
    html.P("Q: Were sales higher before or after the price increase on Jan 15, 2021?",
           style={'textAlign': 'center', 'fontStyle': 'italic'})
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    fig = px.line(
        filtered_df.sort_values("date"),
        x="date",
        y="sales",
        color="region" if region == "all" else None,
        title="Pink Morsel Sales Over Time"
    )

    # vertical line for price increase date
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

    return fig


if __name__ == "__main__":
    app.run(debug=True)
