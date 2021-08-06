import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Wide form data
try:
    exhaust_emission_df = pd.read_csv("./assets/exhaust_emissions.csv")
except:
    exhaust_emission_df = pd.read_csv("../assets/exhaust_emissions.csv")

def create_barchart(user_selected_emissions):
    '''
        Returns a bar chart showing the annual vehicle population by vehicle type.
        Params:
            user_selected_emissions: list of selected emission input from streamlit.
    '''
    vehicles = exhaust_emission_df['vehicle_category']
    all_selected_emissions = []

    if 'CO₂' in user_selected_emissions:
        all_selected_emissions.append(go.Bar(name = "CO₂", x = vehicles, y = exhaust_emission_df["CO₂"]))
    if 'NOx' in user_selected_emissions:
        all_selected_emissions.append(go.Bar(name = "NOx", x = vehicles, y = exhaust_emission_df["NOx"]))
    if 'CO' in user_selected_emissions:
        all_selected_emissions.append(go.Bar(name = "CO", x = vehicles, y = exhaust_emission_df["CO"]))
    if 'P' in user_selected_emissions:
        all_selected_emissions.append(go.Bar(name = "P", x = vehicles, y = exhaust_emission_df["P"]))
    if len(user_selected_emissions) == 0:
        return "Please select at least one emission."


    exhaust_emission_chart = go.Figure(data = all_selected_emissions)    
    exhaust_emission_chart.update_layout(barmode = 'group')
    exhaust_emission_chart.update_yaxes(type = 'log')

    return exhaust_emission_chart


if __name__ == "__main__":
    print(exhaust_emission_df)
    test = [0, 0, 0, 0]
    test = np.array(test)
    test2 = exhaust_emission_df['CO₂'].values
    
    print(test.sum())
    print(type(test))
    print(type(test2))
    print(exhaust_emission_df['CO₂'].values.tolist())


    exhaust_emission_df['test'] = np.multiply(test, test2)
    print(exhaust_emission_df)