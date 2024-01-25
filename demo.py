# Import necessary libraries
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import layout
import pandas as pd

# Sample DataFrame
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# Create a ColumnDataSource
source = ColumnDataSource(df)

# Create a Bokeh plot
plot = figure(title="Bokeh Plot", width=400, height=400)
plot.line('x_values', 'y_values', source=source, line_width=2, line_color="green")

# Create layout
layout = layout([[plot]])
show(layout)
# Function to update data periodically
def update_data():
    new_data = {'x_values': [1, 2, 3, 4, 100],
                'y_values': [2, 4, 6, 8, 0]}  # Update this with your new data
    source.data = new_data

# Periodically update data every second (adjust as needed)
curdoc().add_periodic_callback(update_data, 1000000)

# Show the plot
curdoc().add_root(layout)
