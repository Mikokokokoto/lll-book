import pandas as pd
import utility as util
from datetime import datetime

GRID = [[0]*20]*10
s= datetime(2021,1,1) # start datetime
e= datetime(2021,9,20) # end datetime

def generate_linklab_heatmap(start_datetime, end_datetime
, fields, export_filepath):
	df = pd.read_csv("book_with_grids.csv")
	for idx in range(200):
		fields = df[df['grid']==idx]['fields']
		if len(fields) != 0:
			for field in fields:
				lst = list(df[df['grid']==2]['device_id'])
				print(len(util.get_lfdf(field, s, e, lst)))





if __name__ == "__main__":
	generate_linklab_heatmap(s, e, 0, 0)
	