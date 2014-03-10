_AUTHOR_='C.C.T'


import csv
import numpy
import numpy as np

TIME_LENGTH=3

delta_s = 'MSG_EEG_POWER_DELTA'
high_alpha_s = 'MSG_EEG_POWER_HIGHALPHA'
high_beta_s = 'MSG_EEG_POWER_HIGHBETA'
low_alpha_s = 'MSG_EEG_POWER_LOWALPHA'
low_beta_s = 'MSG_EEG_POWER_LOWBETA'
low_gamma_s = 'MSG_EEG_POWER_LOWGAMMA'
mid_gamma_s = 'MSG_EEG_POWER_MIDGAMMA'
theta_s = 'MSG_EEG_POWER_THETA'

f = open('test_data.csv', 'r')  
f_new = open('revised.csv', 'w')

queue = []
record_progress = 0


first = True
for i in range(1, TIME_LENGTH+1): #for raw data
	if first:
		f_new.write(delta_s+'_'+str(i)+','+high_alpha_s+'_'+str(i)+','+high_beta_s+'_'+str(i)+','+low_alpha_s+'_'+str(i)+','+\
					low_beta_s+'_'+str(i)+','+low_gamma_s+'_'+str(i)+','+mid_gamma_s+'_'+str(i)+','+theta_s+'_'+str(i))
		first=False
	else:
		f_new.write(','+delta_s+'_'+str(i)+','+high_alpha_s+'_'+str(i)+','+high_beta_s+'_'+str(i)+','+low_alpha_s+'_'+str(i)+','+\
					low_beta_s+'_'+str(i)+','+low_gamma_s+'_'+str(i)+','+mid_gamma_s+'_'+str(i)+','+theta_s+'_'+str(i))

f_new.write(','+delta_s+'_sd,'+high_alpha_s+'_sd,'+high_beta_s+'_sd,'+low_alpha_s+'_sd,'+\
			low_beta_s+'_sd,'+low_gamma_s+'_sd,'+mid_gamma_s+'_sd,'+theta_s+'_sd') #for standard deviation

for i in range(1, TIME_LENGTH):
	if first:
		f_new.write(delta_s+'_diff'+str(i)+','+high_alpha_s+'_diff'+str(i)+','+high_beta_s+'_diff'+str(i)+','+low_alpha_s+'_diff'+str(i)+','+\
					low_beta_s+'_diff'+str(i)+','+low_gamma_s+'_diff'+str(i)+','+mid_gamma_s+'_diff'+str(i)+','+theta_s+'_diff'+str(i))
		first=False
	else:
		f_new.write(','+delta_s+'_diff'+str(i)+','+high_alpha_s+'_diff'+str(i)+','+high_beta_s+'_diff'+str(i)+','+low_alpha_s+'_diff'+str(i)+','+\
					low_beta_s+'_diff'+str(i)+','+low_gamma_s+'_diff'+str(i)+','+mid_gamma_s+'_diff'+str(i)+','+theta_s+'_diff'+str(i)) #for diff


f_new.write(',btn_color\n') #for btn_color

for row in csv.DictReader(f):

	if row['MSG_BLINK'] == 0:
		continue
		queue = []
		record_progress = 0
	else:
		if record_progress!=TIME_LENGTH: #If is recording

			if row['btn_color']!='0':

				delta = row[delta_s]
				high_alpha = row[high_alpha_s]
				high_beta = row[high_beta_s]
				low_alpha = row[low_alpha_s]
				low_beta = row[low_beta_s]
				low_gamma = row[low_gamma_s]
				mid_gamma = row[mid_gamma_s]
				theta = row[theta_s]

				queue.append([delta, high_alpha, high_beta, low_alpha, low_beta, low_gamma, mid_gamma, theta, row['btn_color']])
				record_progress+=1

			else: #If time length is not enough
				record_progress = 0
				queue=[]
	
		else: #If queue is full, save data

			for row in queue: #write raw data
				tmp = ''

				for data in row[:-1]:
					tmp+=data+','
				f_new.write(tmp)

			arr = []
			for num in range(0, 8): 
				for next_n in range(0, TIME_LENGTH):
					arr.append(int(queue[next_n][num]))

				f_new.write(str(np.std(np.array(arr)))+',') #write std
				arr = []
				print 'this is std'

			arr = []
			for num in range(0, 8):
				for next_n in range(0, TIME_LENGTH):
					arr.append(int(queue[next_n][num]))

				for  diff in np.diff(np.array(arr)): #write diff
					f_new.write(str(diff)+',')
				print 'this is diff' 

				
				arr = []


			f_new.write(row[-1]+'\n') #write btn_color
			queue=[]
			record_progress=0


f.close()
f_new.close()


f_chosen = open('chosen.csv','w') 
output = [0,1,2,3]

for row in csv.reader(open('revised.csv')):	
	s = ''
	for col in output:
		for j in range(0, TIME_LENGTH):
			s += str(row[col+j*8]+',')

		s += str(row[col+TIME_LENGTH*8])+','

		for k in range(0, TIME_LENGTH-1):
			s+= str(row[col+(TIME_LENGTH+1)*8+k*8])+','

	f_chosen.write(s[:-1]+','+row[-1])
	f_chosen.write('\n')
f_chosen.close()

