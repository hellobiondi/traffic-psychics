# Data Manipulation Imports
import pandas as pd

# Data Visualisation Imports
import plotly.express as px

## Expected EV adoption numbers

def create_scatterplot(selected):
    '''
        Returns either a prompt for category selection or scatterplot object with trendlines.
        Params:
            selected: list of selected input from streamlit.
            
    '''
    try:
        expected_EV_df = pd.read_csv("./assets/expected_EV_adoption.csv")
    except:
        expected_EV_df = pd.read_csv("../assets/expected_EV_adoption.csv")

    if len(selected) == 0:
        return "Please select a category."

    if len(selected) == 1:
        graph_df = expected_EV_df[expected_EV_df['category'] == selected[0]]
    elif len(selected) == 2:
        graph_df = expected_EV_df[(expected_EV_df['category'] == selected[0]) | (expected_EV_df['category'] == selected[1])]
    else:
        graph_df = expected_EV_df

    expected_EV_chart = px.scatter(graph_df, 
                    x = 'year', y = 'qty',
                    color = 'category',
                    labels = {
                        "year": "Year", 
                        "qty": "Quantity", 
                        "category": "Label",
                    },
                    trendline = 'ols'
    )

    return expected_EV_chart


