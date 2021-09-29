import pandas as pd
import utility as util
from datetime import datetime

GRID = [[0]*20]*10


def check_fields(fields, all_fields):
	for idx, field in enumerate(all_fields):
		if field in given_fields:
			return True, idx
	return False, idx

def generate_linklab_heatmap(start_datetime, end_datetime
, fields, export_filepath):
	df = pd.read_csv("book_with_grids.csv")

	for n in range(200):
		all_fields = df[df['grid']==n]['fields']
		field_lst = all_fields.values[0].split(',')
		condition, param_index = check_fields(fields, field_lst)
		if len(fields) != 0 and condition:
			parameter = field_lst[param_index]
			entry = util.get_lfdf(parameter, start_datetime, end_datetime, list(df[df['grid']==n]['device_id']))
			entry_num = len(entry)
			GRID[n//20][n%20] += entry_num






			


fields --> devices 


if __name__ == "__main__":
	s= datetime(2021,8,20) # start datetime
	e= datetime(2021,9,20) # end datetime

	generate_linklab_heatmap(s, e, 0, 0)
	