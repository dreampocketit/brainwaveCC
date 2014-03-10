import numpy as np


def transform(queue, TIME_LENGTH):

	final = []
	for row in queue: #write raw data

		for data in row:

			final.append(data)
				
	arr = []
	for num in range(0, 8): 
		for next_n in range(0, TIME_LENGTH):
			arr.append(queue[next_n][num])
		final.append(np.std(np.array(arr))) #write std
		arr = []

	for num in range(0, 8): 
		for next_n in range(0, TIME_LENGTH):
			arr.append(queue[next_n][num])
		

		for  diff in np.diff(np.array(arr)): #write diff
			final.append(diff)
		arr=[]

	return final

def sel(arr, output, TIME_LENGTH):
	s = []
	for col in output:
		for j in range(0, TIME_LENGTH):
			s.append(arr[col+j*8])

		s.append(arr[col+TIME_LENGTH*8])

		for k in range(0, TIME_LENGTH-1):
			s.append(arr[col+(TIME_LENGTH+1)*8+k*8])

	return s

#print transform([[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[4,4,4,4,4,8,9,10]],3)
output = [0,1,2,4]
asd = ['MSG_EEG_POWER_DELTA_1','MSG_EEG_POWER_HIGHALPHA_1','MSG_EEG_POWER_HIGHBETA_1','MSG_EEG_POWER_LOWALPHA_1','MSG_EEG_POWER_LOWBETA_1','MSG_EEG_POWER_LOWGAMMA_1','MSG_EEG_POWER_MIDGAMMA_1','MSG_EEG_POWER_THETA_1','MSG_EEG_POWER_DELTA_2','MSG_EEG_POWER_HIGHALPHA_2','MSG_EEG_POWER_HIGHBETA_2','MSG_EEG_POWER_LOWALPHA_2','MSG_EEG_POWER_LOWBETA_2','MSG_EEG_POWER_LOWGAMMA_2','MSG_EEG_POWER_MIDGAMMA_2','MSG_EEG_POWER_THETA_2','MSG_EEG_POWER_DELTA_3','MSG_EEG_POWER_HIGHALPHA_3','MSG_EEG_POWER_HIGHBETA_3','MSG_EEG_POWER_LOWALPHA_3','MSG_EEG_POWER_LOWBETA_3','MSG_EEG_POWER_LOWGAMMA_3','MSG_EEG_POWER_MIDGAMMA_3','MSG_EEG_POWER_THETA_3','MSG_EEG_POWER_DELTA_sd','MSG_EEG_POWER_HIGHALPHA_sd','MSG_EEG_POWER_HIGHBETA_sd','MSG_EEG_POWER_LOWALPHA_sd','MSG_EEG_POWER_LOWBETA_sd','MSG_EEG_POWER_LOWGAMMA_sd','MSG_EEG_POWER_MIDGAMMA_sd','MSG_EEG_POWER_THETA_sd','MSG_EEG_POWER_DELTA_diff1','MSG_EEG_POWER_HIGHALPHA_diff1','MSG_EEG_POWER_HIGHBETA_diff1','MSG_EEG_POWER_LOWALPHA_diff1','MSG_EEG_POWER_LOWBETA_diff1','MSG_EEG_POWER_LOWGAMMA_diff1','MSG_EEG_POWER_MIDGAMMA_diff1','MSG_EEG_POWER_THETA_diff1','MSG_EEG_POWER_DELTA_diff2','MSG_EEG_POWER_HIGHALPHA_diff2','MSG_EEG_POWER_HIGHBETA_diff2','MSG_EEG_POWER_LOWALPHA_diff2','MSG_EEG_POWER_LOWBETA_diff2','MSG_EEG_POWER_LOWGAMMA_diff2','MSG_EEG_POWER_MIDGAMMA_diff2','MSG_EEG_POWER_THETA_diff2','btn_color']
print sel(asd,output,3)