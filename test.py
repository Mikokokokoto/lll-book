import pandas as pd
import utility as util
from datetime import datetime
import numpy as np

GRID = np.zeros((3, 10))

if __name__ == "__main__":
	# df = pd.read_csv("book_with_grids.csv")
	for i in range(20):
		GRID[i//10][i%10] += 1
		print(GRID)

	# fields = []
	# for element in df.itertuples():
	# 	lst = (element[6].split(','))
	# 	for element in lst:
	# 		if element not in fields:
	# 			fields.append(element)
	# print(fields)
		# for idx, field in enumerate(all_fields):
		# 	print(idx)
		# 	print(field)

	# lst = ['Illumination_lx', 'Range select', 'Supply voltage_V', 
	# 'rssi', 'Humidity_%', 'Temperature_°C', 'awair_score', 'co2_ppm', 
	# 'pm2.5_μg/m3', 'voc_ppb', 'T-Sensor', 'PIR Status', 'Supply voltage (OPTIONAL)_V', 
	# 'Supply voltage availability', 'Contact', 'Concentration_ppm', 'H-Sensor']