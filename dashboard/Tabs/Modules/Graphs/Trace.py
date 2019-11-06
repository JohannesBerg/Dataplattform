import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from typing import Union

class Trace():

	def __init__(self, data, data_layout = [], trace_mode="lines",
			trace_type="scatter", colors = ["#0c956e", "blue", "read"], 
			title="", names=[], shape=["linear"], smoothing=[0.8], 
			axis_text=["X-axis", "Y-axis"], axis_type=["linear", "linear"], 
			plot_bgcolor="#ffffff", grid_color="rgba(0, 0, 0, 0.1)", 
			paper_bgcolor="#fffaf3", show_legend=True, line_dash=["solid"],
			line_fill=Union[dict, str]):

		if data_layout == []:
			for i in range(0, len(data.columns), 2):
				print(i)
				data_layout.append([data.columns[i], data.columns[i+1 if i+1 < len(data.columns) else i]])


		self.traces = []
		for i in range(len(data_layout)):
			#cur_data = data[[data_layout[i][0], data_layout[i][1]]].copy().dropna()
			trace = {
					"mode": trace_mode,
					"type": trace_type,
					"name": names[i] if i < len(names) else "Trace",
					"x": data[data_layout[i][0]],
					"y": data[data_layout[i][1]],
					"line": {
						"dash": line_dash[i] if i < len(line_dash) else line_dash[0],
						"color": colors[i] if i < len(colors) else "blue",
						"shape": shape[i] if i < len(shape) else shape[0],
						"smoothing": smoothing[i] if i < len(smoothing) else smoothing[0],
					},
					"type": trace_type,

				}

			if isinstance(line_fill, (list, str)):
				if isinstance(line_fill, list):
					if i == line_fill[1]:
						trace["fill"] = line_fill[0]
				else:
					trace["fill"] = line_fill
				self.traces.insert(0, trace)
			else:
				self.traces.append(trace)

		layout = {
			"title": {
				"text": title,
				},
			"xaxis": {
				"type": axis_type[0],
				"title": {
					"text": axis_text[0],
				},
				"autorange": True,
				"gridcolor": grid_color,
			},
			"yaxis": {
				"type": axis_type[1] if 1 < len(axis_type) else "linear",
				"title": {
					"text": axis_text[1] if 1 < len(axis_text) else "Y-axis",
				},
				"autorange": True,
				"gridcolor": grid_color,
			},
			"plot_bgcolor": plot_bgcolor,
			"paper_bgcolor": paper_bgcolor,
			"showlegend": show_legend,
		}
		self.fig = go.Figure(data=self.traces, layout=layout)


	def get_trace(self):
		return self.fig