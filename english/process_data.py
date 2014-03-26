import csv
import numpy as np

def cal_std(sta, sto, arr):
	return int(np.std(np.array(arr[sta:sto])))

def fil(sta, sto):
	f = open(str(sta)+'-'+str(sto)+'.csv','w')
	f.write('delta,midgamma,lowgamma,theta,highalpha,lowalpha,highbeta,lowbeta,state\n')


	for row in csv.DictReader(open('output.csv','rU')):
		delta = row['delta'].split('-')
		delta = [ int(x) for x in delta ]

		midgamma = row['midgamma'].split('-')
		midgamma = [ int(x) for x in midgamma ]

		lowgamma = row['lowgamma'].split('-')
		lowgamma = [ int(x) for x in lowgamma ]

		theta = row['theta'].split('-')
		theta = [ int(x) for x in theta ]

		highalpha = row['highalpha'].split('-')
		highalpha = [ int(x) for x in highalpha ]

		lowalpha = row['lowalpha'].split('-')
		lowalpha = [ int(x) for x in lowalpha ]

		highbeta = row['highbeta'].split('-')
		highbeta = [ int(x) for x in highbeta ]

		lowbeta = row['lowbeta'].split('-')
		lowbeta = [ int(x) for x in lowbeta ]



		f.write(str(cal_std(sta,sto,delta))+',')
		f.write(str(cal_std(sta,sto,midgamma))+',')
		f.write(str(cal_std(sta,sto,lowgamma))+',')
		f.write(str(cal_std(sta,sto,theta))+',')
		f.write(str(cal_std(sta,sto,highalpha))+',')
		f.write(str(cal_std(sta,sto,lowalpha))+',')
		f.write(str(cal_std(sta,sto,highbeta))+',')
		f.write(str(cal_std(sta,sto,lowbeta))+',')
		f.write(str(row['state'])+'\n')


fil(1,5)




	