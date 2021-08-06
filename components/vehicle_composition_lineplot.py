import pandas as pd
import plotly.express as px



def preproc_car_composition_df(csv_path):
    '''
        Returns car composition dataframe. Preprocessed to collate tax exempted vehicles.
        Params:
            csv_path: path to data.gov csv for vehicle by vehicle type.
    '''

    car_composition_df = pd.read_csv(csv_path)

    # Reseting Tax Exempted Vehicles
    temp = car_composition_df[car_composition_df['category'] == 'Tax Exempted Vehicles']
    car_composition_df = car_composition_df[car_composition_df['category'] != 'Tax Exempted Vehicles']

    col_headers = list(temp)
    og_col_headers = col_headers.copy()

    col_headers[1], col_headers[2] = col_headers[2], col_headers[1] 
    temp = temp[col_headers]
    temp.columns = og_col_headers

    car_composition_df = pd.concat([car_composition_df, temp], axis = 0).groupby(['year', 'category']).sum().reset_index()

    # Combining Taxis and Cars
    temp_taxi_df = car_composition_df[car_composition_df['category'] == 'Taxis']
    temp_car_df = car_composition_df[car_composition_df['category'] == 'Cars and Station-wagons']
    temp_col = temp_car_df['category'].reset_index(drop = True)
    car_df = pd.concat([temp_taxi_df, temp_car_df], axis = 0)
    car_df = car_df.groupby('year').sum().reset_index().join(temp_col)

    # Combining car_df with original composition
    car_composition_df = car_composition_df.loc[(car_composition_df['category'] != 'Cars and Station-wagons') & (car_composition_df['category'] != 'Taxis')]
    car_composition_df = pd.concat([car_composition_df, car_df], axis = 0)

    return car_composition_df[['year', 'category', 'number']]


# try:
#     car_composition_df = preproc_car_composition_df("./assets/annual-motor-vehicle-population-by-vehicle-type.csv")
# except:
#     car_composition_df = preproc_car_composition_df("../assets/annual-motor-vehicle-population-by-vehicle-type.csv")


def create_lineplot():
    '''
        Returns a line plot showing the annual vehicle population by vehicle type.
        Params:
            NA: note that df for the line chart is a df input from Data.gov CSV preprocessed by preproc_car_composition_df() function.
    '''
    try:
        car_composition_df = pd.read_csv("./assets/annual_motor_vehicle_example.csv")
    except:
        car_composition_df = pd.read_csv("../assets/annual_motor_vehicle_example.csv")

    car_composition_chart = px.line(
        car_composition_df,
        x = 'year',
        y ='number',
        color = 'category',
        labels = {
            'number': 'Number of Vehicles',
            'year' : 'Year',
            'category' : 'Vehicle Category'
        }
    )

    return car_composition_chart


if __name__ == "__main__":
    # car_composition_df.to_csv('../assets/annual_motor_vehicle_example.csv', index = False)
    car_composition_df = pd.read_csv("../assets/annual_motor_vehicle_example.csv")
    print(car_composition_df[car_composition_df['category'] == 'Cars and Station-wagons']['number'])
    print(car_composition_df[car_composition_df['category'] == 'Cars and Station-wagons']['number'].sum())

