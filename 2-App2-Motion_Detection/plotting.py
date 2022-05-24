from motion_detector import df 
from bokeh.plotting import figure, output_file, show

p = figure(width=100, height=100, x_axis_type = "datetime", title="Motion Graph")
q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("Graph.html")
show(p)