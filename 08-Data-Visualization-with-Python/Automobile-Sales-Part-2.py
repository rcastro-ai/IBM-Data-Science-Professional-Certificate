# Data Science Portfolio - IBM Professional Certificate Program
# Data Visualization with Python - Final Assignment - Part 2
# Dashboards for Automobile Sales Case Study
# Original Lab by IBM Skills Network
# Final code and testing done by Roberto Castro - github.com/rcastro-ai

#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv')

# Dataset locally available: automobile_sales.csv
#data = pd.read_csv('automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Statistics Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years 
year_list = [i for i in range(1980, 2024, 1)]

# Create the layout of the app
app.layout = html.Div([
    # Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard",
             style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Unified control container
    html.Div([
        # First dropdown (Statistics)
        html.Div([
            html.Label("Select Statistics:", style={'paddingRight': '10px'}),
            dcc.Dropdown(
                id='dropdown-statistics',
                options=dropdown_options,
                value='Select Statistics',
                placeholder='Select a report type'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}), # Set width to slightly less than half

        # Second dropdown (Year)
        html.Div([
            html.Label("Select Year:", style={'paddingRight': '10px'}),
            dcc.Dropdown(
                id='select-year',
                options=year_list,
                value=None,
                placeholder='Select-year'
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}) # Match the width here
        
    ], style={'textAlign': 'center', 'padding': '10px'}), # Center the whole control row

    # Output display
    html.Div([
        html.Div(id='output-container', className='chart-grid')
    ])
])

# Creating Callbacks

# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='value'))

def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics': 
        return False
    else: 
        return True

# Callback for chart plotting

# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='select-year', component_property='value')])

def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
# Create and display graphs for Recession Report Statistics

# Plot 1: Automobile sales fluctuate over Recession Period (year wise)
        # Use groupby to create relevant data for plotting
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
                figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))

# Plot 2: Calculate the average number of vehicles sold by vehicle type       
        # Use groupby to create relevant data for plotting
        # Hint: Use Vehicle_Type and Automobile_Sales columns
        average_sales = recession_data.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()    

        average_sales['Year'] = average_sales['Year'].astype(str)

        R_chart2 = dcc.Graph(
                figure=px.bar(average_sales,
                x='Year',
                y='Automobile_Sales',
                color='Vehicle_Type',
                barmode='group',
                title="Average Sales by Vehicle Type per Year"))
        
# Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        # Grouping data for plotting
	    # Hint: Use Vehicle_Type and Advertising_Expenditure columns
        exp_rec= recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
                figure=px.pie(exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title='Advertisement Expenditure by Vehicle Type'))

# Plot 4: bar chart for the effect of unemployment rate on vehicle type and sales
        # Grouping data for plotting
	    # Hint: Use unemployment_rate, Vehicle_Type and Automobile_Sales columns
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
                figure=px.bar(unemp_data,
                x='unemployment_rate',
                y='Automobile_Sales',
                color='Vehicle_Type',
                labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
                title='Effect of Unemployment Rate on Vehicle Type and Sales'))

        return [
                html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
                html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'})
            ]

# Create and display graphs for Yearly Report Statistics

# Yearly Statistic Report Plots
    # Check for Yearly Statistics.                             
    elif (input_year and selected_statistics == 'Yearly Statistics') :
        yearly_data = data[data['Year'] == input_year]
                                                           
# Plot 1: Yearly Automobile sales using line chart for the whole period.
        # Grouping data for plotting.
        # Hint: Use the columns Year and Automobile_Sales.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
                figure=px.line(yas, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales"))
            
# Plot 2: Total Monthly Automobile sales using line chart.
        # Grouping data for plotting.
	    # Hint: Use the columns Month and Automobile_Sales.
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        yearly_data['Month'] = pd.Categorical(yearly_data['Month'], categories=month_order, ordered=True)

        mas = yearly_data.groupby('Month', observed=False)['Automobile_Sales'].sum().reset_index()

        Y_chart2 = dcc.Graph(
                figure=px.line(mas,
                x='Month',
                y='Automobile_Sales',
                title='Total Monthly Automobile Sales'))

# Plot 3: Bar chart for average number of vehicles sold during the given year
         # Grouping data for plotting.
         # Hint: Use the columns Year and Automobile_Sales
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph( 
                figure=px.bar(avr_vdata,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

# Plot 4: Total Advertisement Expenditure for each vehicle type using pie chart
         # Grouping data for plotting.
         # Hint: Use the columns Vehicle_Type and Advertising_Expenditure
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
                figure=px.pie(exp_data,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title='Advertisement Expenditure by Vehicle Type'))

# Returning the graphs for displaying Yearly data
        return [
                html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display': 'flex'}),
                html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display': 'flex'})
        ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)

