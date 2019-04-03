import csv
import pandas as pd
from scipy import stats

#ANOVA one-way test
class ANOVAPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		#get column group name
		f = open(self.myfile, 'r')
		csv_f = csv.reader(f)
		col_group_name = csv_f.__next__()

		#create dataframe object
		data = pd.read_csv(self.myfile)

		#use list comprehension of grouped data based 
		#on first column. iterate thru groupby tuples
		self.values_per_group = [col for col_name, \
				col in data.groupby(col_group_name[0])[col_group_name[1]]]
	
	    
	def output(self, filename):
		f, p = stats.f_oneway(*self.values_per_group)
		print("F-value statistic = ", f, ", p-value = ", p)