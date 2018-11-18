from plotly.offline import plot
import plotly.graph_objs as go

plot([go.Scatter(
    x=[0, 4], 
    y=[3, 5, 6], 
    name='graph'
    )])