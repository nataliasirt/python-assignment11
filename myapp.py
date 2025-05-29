from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas')

countries = df['country'].unique()

app = Dash(__name__)

server = app.server  

app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback for dynamic updates
@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(country):
    filtered_df = df[df['country'] == country]
    fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'GDP Per Capita for {country}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)