# Import the library
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Load the data
ecom_sales = pd.read_csv('data/ecom_data.csv')
major_categories = list(ecom_sales['Major Category'].unique())
minor_categories = list(ecom_sales['Minor Category'].unique())
ecom_country = ecom_sales.groupby('Country')['OrderValue'].agg(['sum', 'count']).reset_index().rename(columns={'sum':'Total Sales', 'count':'Sales Volume'})

# Setting up the apps
css = '#'
app = dash.Dash(name='E Commerce Sales', external_stylesheets = css)

# Graph function


# App layout


# Callback


# Starting up the server
if __name__ == '__main__':
    app.run_server(debug=True)