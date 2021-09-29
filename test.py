import pandas as pd
import utility as util
from datetime import datetime

if __name__ == "__main__":
	df = pd.read_csv("book_with_grids.csv")
	for i in range(30):
		all_fields = df[df['grid']==i]['fields']
		if len(all_fields) != 0:
			print(all_fields.values[0].split(','))
	
		# for idx, field in enumerate(all_fields):
		# 	print(idx)
		# 	print(field)
	