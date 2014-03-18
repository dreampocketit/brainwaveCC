from NeuroPy import NeuroPy
import time
import datetime
import requests
from pac import transform as pt 
from pac import sel as ps

USER_ID = '1'
RECORD_TIME = datetime.datetime.now()
btn_color = 0
MSG_POOR_SIGNAL = 3
MSG_ATTENTION = 3
MSG_MEDITATION = 3
MSG_BLINK = 10
MSG_EEG_POWER_HIGHALPHA = 0
MSG_EEG_POWER_LOWALPHA = 0
MSG_EEG_POWER_HIGHBETA = 0
MSG_EEG_POWER_LOWBETA = 0
MSG_EEG_POWER_MIDGAMMA = 0
MSG_EEG_POWER_LOWGAMMA = 0
MSG_EEG_POWER_THETA = 0
MSG_EEG_POWER_DELTA  = 0

object1=NeuroPy("/dev/tty.MindWaveMobile-DevA",57600)
object1.start()
import Orange
iris = Orange.data.Table("chosen.csv")  #import training data
ann = Orange.classification.neural.NeuralNetworkLearner(iris, n_mid=10, reg_fact=1, max_iter=300, rand=None)



def sendToPyServer( USER_ID,RECORD_TIME,btn_color,MSG_POOR_SIGNAL,MSG_ATTENTION,MSG_MEDITATION,MSG_BLINK  , MSG_EEG_POWER_HIGHALPHA,MSG_EEG_POWER_LOWALPHA,MSG_EEG_POWER_HIGHBETA,MSG_EEG_POWER_LOWBETA,MSG_EEG_POWER_MIDGAMMA,MSG_EEG_POWER_LOWGAMMA,MSG_EEG_POWER_THETA,MSG_EEG_POWER_DELTA ):

	post_data = {'MSG_BLINK':MSG_BLINK, 'MSG_MEDITATION':MSG_MEDITATION, 'MSG_ATTENTION':MSG_ATTENTION, 'MSG_POOR_SIGNAL':MSG_POOR_SIGNAL, 'MSG_EEG_POWER_DELTA':MSG_EEG_POWER_DELTA, 'MSG_EEG_POWER_HIGHALPHA':MSG_EEG_POWER_HIGHALPHA, 'MSG_EEG_POWER_HIGHBETA':MSG_EEG_POWER_HIGHBETA, 'MSG_EEG_POWER_LOWALPHA':MSG_EEG_POWER_LOWALPHA, 'MSG_EEG_POWER_LOWBETA':MSG_EEG_POWER_LOWBETA, 'MSG_EEG_POWER_LOWGAMMA':MSG_EEG_POWER_LOWGAMMA, 'MSG_EEG_POWER_MIDGAMMA':MSG_EEG_POWER_MIDGAMMA, 'MSG_EEG_POWER_THETA':MSG_EEG_POWER_THETA, 'USER_ID':USER_ID, 'btn_color':btn_color, 'RECORD_TIME':RECORD_TIME}

	post_response = requests.post(url='http://140.114.134.8:5000/writeEEG', data=post_data)
	return


while True:
	
	MSG_POOR_SIGNA = object1.poorSignal
	MSG_ATTENTION = object1.attention
	MSG_MEDITATION = object1.meditation
	MSG_EEG_POWER_HIGHALPHA = object1.highAlpha
	MSG_EEG_POWER_LOWALPHA = object1.lowAlpha
	MSG_EEG_POWER_HIGHBETA = object1.highBeta
	MSG_EEG_POWER_LOWBETA = object1.lowBeta
	MSG_EEG_POWER_MIDGAMMA = object1.midGamma
	MSG_EEG_POWER_LOWGAMMA = object1.lowGamma
	MSG_EEG_POWER_THETA = object1.theta
	MSG_EEG_POWER_DELTA  = object1.delta

	print object1.poorSignal
	print MSG_EEG_POWER_HIGHBETA


	time.sleep(1)





