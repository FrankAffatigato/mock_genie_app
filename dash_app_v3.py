import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd

# ------------------------------------------------------------
# Mock Data
# ------------------------------------------------------------
schemas = {
    "sales_data": ["transactions", "store_performance"],
    "inventory_data": ["stock_levels", "supplier_deliveries"],
    "customer_data": ["customer_orders", "loyalty_points"]
}

data = pd.DataFrame({
    "store": ["A", "B", "C", "D", "E"],
    "sales": [145000, 112000, 98000, 153000, 127000],
    "profit": [34000, 28000, 22000, 36000, 30000],
    "transactions": [1200, 950, 800, 1300, 1050]
})

trend_data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    "profit": [18000, 19500, 22000, 26000, 30000, 34000, 36500, 39000],
})

# ------------------------------------------------------------
# Initialize App
# ------------------------------------------------------------
app = dash.Dash(__name__)
app.title = "Databricks Unity Dashboard"

# ------------------------------------------------------------
# Style Constants
# ------------------------------------------------------------
DARK_BG = "#1c1f26"
CARD_BG = "#232831"
TEXT_COLOR = "#f1f3f5"
ACCENT = "#1f6feb"
GREEN = "#3fb950"
RED = "#f85149"

# ------------------------------------------------------------
# Figures
# ------------------------------------------------------------
sales_fig = px.bar(
    data,
    x="store",
    y="sales",
    text="sales",
    color="store",
    color_discrete_sequence=["#001f3f", "#0056b3", "#66b3ff", "#ff8c00", "#ffbb66"],
    title="Sales by Store"
).update_layout(
    paper_bgcolor=CARD_BG,
    plot_bgcolor=CARD_BG,
    font_color=TEXT_COLOR,
    title_x=0.5,
    showlegend=False,
    height=400
)

profit_fig = px.line(
    trend_data,
    x="month",
    y="profit",
    markers=True,
    title="Monthly Profit Trend"
).update_traces(line_color=GREEN, marker_color=GREEN)
profit_fig.update_layout(
    paper_bgcolor=CARD_BG,
    plot_bgcolor=CARD_BG,
    font_color=TEXT_COLOR,
    title_x=0.5,
    showlegend=False,
    height=400
)

# ------------------------------------------------------------
# Layout
# ------------------------------------------------------------
app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": DARK_BG,
        "padding": "20px",
        "minHeight": "100vh",
        "overflowY": "auto",
    },
    children=[
        # Clean header (no logo at all)
        html.Div(
            [
                html.H1(
                    "FoodMart Databricks Analytics",
                    style={
                        "textAlign": "center",
                        "color": ACCENT,
                        "marginBottom": "5px",
                        "fontWeight": "bold",
                        "fontSize": "36px",
                    },
                ),
                html.Hr(
                    style={"border": f"1px solid {ACCENT}", "width": "80%", "margin": "auto"}
                ),
            ]
        ),

        # KPI Section
        html.Div(
            style={
                "display": "flex",
                "justifyContent": "space-evenly",
                "margin": "40px 0",
                "flexWrap": "wrap",
                "gap": "20px",
                "padding": "0 120px",
            },
            children=[
                html.Div(
                    style={
                        "backgroundColor": CARD_BG,
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center",
                        "width": "220px",
                        "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                    },
                    children=[
                        html.H4("Total Sales", style={"color": TEXT_COLOR}),
                        html.H2(f"${data['sales'].sum():,}", style={"color": ACCENT}),
                    ],
                ),
                html.Div(
                    style={
                        "backgroundColor": CARD_BG,
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center",
                        "width": "220px",
                        "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                    },
                    children=[
                        html.H4("Total Profit", style={"color": TEXT_COLOR}),
                        html.H2(f"${data['profit'].sum():,}", style={"color": GREEN}),
                    ],
                ),
                html.Div(
                    style={
                        "backgroundColor": CARD_BG,
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center",
                        "width": "220px",
                        "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                    },
                    children=[
                        html.H4("Transactions", style={"color": TEXT_COLOR}),
                        html.H2(f"{data['transactions'].sum():,}", style={"color": RED}),
                    ],
                ),
            ],
        ),

        # Chat Section
        html.Div(
            style={
                "backgroundColor": CARD_BG,
                "padding": "25px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                "maxWidth": "70%",
                "margin": "auto",
                "marginBottom": "40px",
            },
            children=[
                html.H4("Ask Genie AI Assistant", style={"color": ACCENT}),
                html.Div(
                    style={"display": "flex", "marginTop": "10px", "gap": "10px"},
                    children=[
                        dcc.Input(
                            id="chat-input",
                            type="text",
                            placeholder="Ask about this data...",
                            style={
                                "flex": "1",
                                "padding": "12px",
                                "borderRadius": "8px",
                                "border": "1px solid #30363d",
                                "backgroundColor": DARK_BG,
                                "color": TEXT_COLOR,
                            },
                        ),
                        html.Button(
                            "Send",
                            id="chat-send",
                            style={
                                "backgroundColor": ACCENT,
                                "color": "white",
                                "border": "none",
                                "borderRadius": "8px",
                                "padding": "10px 20px",
                                "cursor": "pointer",
                                "fontWeight": "bold",
                            },
                        ),
                    ],
                ),
                html.P(
                    "Note: This chat interface is for demonstration only.",
                    style={"color": "#8b949e", "marginTop": "8px", "fontSize": "14px"},
                ),
            ],
        ),

        # Stacked Charts Section
        html.Div(
            style={
                "backgroundColor": CARD_BG,
                "padding": "25px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                "maxWidth": "70%",
                "margin": "auto",
                "marginBottom": "40px",
            },
            children=[
                html.H4("Sales & Profit Overview", style={"color": ACCENT}),
                dcc.Graph(id="sales_bar", figure=sales_fig, config={"responsive": False}),
                html.Hr(style={"border": f"1px solid {ACCENT}", "margin": "30px 0"}),
                dcc.Graph(id="profit_line", figure=profit_fig, config={"responsive": False}),
            ],
        ),

        # Schema/Table Selector
        html.Div(
            style={
                "backgroundColor": CARD_BG,
                "padding": "25px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                "marginBottom": "40px",
                "maxWidth": "70%",
                "margin": "auto",
            },
            children=[
                html.H4("Unity Catalog Table Selector", style={"color": ACCENT}),
                html.Div(
                    style={"display": "flex", "gap": "20px", "marginTop": "10px"},
                    children=[
                        html.Div(
                            style={"width": "45%"},
                            children=[
                                html.Label(
                                    "Select Schema",
                                    style={"fontWeight": "bold", "color": TEXT_COLOR},
                                ),
                                dcc.Dropdown(
                                    id="schema-dropdown",
                                    options=[{"label": s, "value": s} for s in schemas.keys()],
                                    value=list(schemas.keys())[0],
                                    clearable=False,
                                    style={"color": DARK_BG},
                                ),
                            ],
                        ),
                        html.Div(
                            style={"width": "45%"},
                            children=[
                                html.Label(
                                    "Select Table",
                                    style={"fontWeight": "bold", "color": TEXT_COLOR},
                                ),
                                dcc.Dropdown(
                                    id="table-dropdown", clearable=False, style={"color": DARK_BG}
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),

        # Data Table
        html.Div(
            style={
                "backgroundColor": CARD_BG,
                "padding": "25px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0,0,0,0.4)",
                "maxWidth": "70%",
                "margin": "auto",
                "marginBottom": "60px",
            },
            children=[
                html.Div(
                    style={
                        "display": "flex",
                        "justifyContent": "space-between",
                        "alignItems": "center",
                    },
                    children=[
                        html.H4("Data Table (Mock Data)", style={"color": ACCENT}),
                        html.Button(
                            "Export",
                            id="export-btn",
                            style={
                                "backgroundColor": ACCENT,
                                "color": "white",
                                "border": "none",
                                "borderRadius": "6px",
                                "padding": "8px 16px",
                                "cursor": "pointer",
                                "fontWeight": "bold",
                            },
                        ),
                    ],
                ),
                dash_table.DataTable(
                    columns=[{"name": i.title(), "id": i} for i in data.columns],
                    data=data.to_dict("records"),
                    style_header={
                        "backgroundColor": ACCENT,
                        "color": "white",
                        "fontWeight": "bold",
                        "textAlign": "center",
                    },
                    style_cell={
                        "backgroundColor": CARD_BG,
                        "color": TEXT_COLOR,
                        "border": "1px solid #30363d",
                        "textAlign": "center",
                        "padding": "10px",
                        "fontSize": "15px",
                    },
                    style_table={"overflowX": "auto", "minWidth": "100%"},
                    page_size=10,
                ),
            ],
        ),
    ],
)

# ------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------
@app.callback(
    Output("table-dropdown", "options"),
    Output("table-dropdown", "value"),
    Input("schema-dropdown", "value"),
)
def update_table_options(selected_schema):
    tables = schemas[selected_schema]
    return [{"label": t, "value": t} for t in tables], tables[0]

# ------------------------------------------------------------
# Run App
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
