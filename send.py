import requests

def sendToPyServer( USER_ID,RECORD_TIME,btn_color,MSG_POOR_SIGNAL,MSG_ATTENTION,MSG_MEDITATION,MSG_BLINK  , MSG_EEG_POWER_HIGHALPHA,MSG_EEG_POWER_LOWALPHA,MSG_EEG_POWER_HIGHBETA,MSG_EEG_POWER_LOWBETA,MSG_EEG_POWER_MIDGAMMA,MSG_EEG_POWER_LOWGAMMA,MSG_EEG_POWER_THETA,MSG_EEG_POWER_DELTA ):

	post_data = {'MSG_BLINK':MSG_BLINK, 'MSG_MEDITATION':MSG_MEDITATION, 'MSG_ATTENTION':MSG_ATTENTION, 'MSG_POOR_SIGNAL':MSG_POOR_SIGNAL, 'MSG_EEG_POWER_DELTA':MSG_EEG_POWER_DELTA, 'MSG_EEG_POWER_HIGHALPHA':MSG_EEG_POWER_HIGHALPHA, 'MSG_EEG_POWER_HIGHBETA':MSG_EEG_POWER_HIGHBETA, 'MSG_EEG_POWER_LOWALPHA':MSG_EEG_POWER_LOWALPHA, 'MSG_EEG_POWER_LOWBETA':MSG_EEG_POWER_LOWBETA, 'MSG_EEG_POWER_LOWGAMMA':MSG_EEG_POWER_LOWGAMMA, 'MSG_EEG_POWER_MIDGAMMA':MSG_EEG_POWER_MIDGAMMA, 'MSG_EEG_POWER_THETA':MSG_EEG_POWER_THETA, 'USER_ID':USER_ID, 'btn_color':btn_color, 'RECORD_TIME':RECORD_TIME}

	post_response = requests.post(url='http://140.114.134.8:5000/writeEEG', data=post_data)
	return





USER_ID = '1'
RECORD_TIME = 978310861
btn_color = 3
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

sendToPyServer( USER_ID,RECORD_TIME,btn_color,MSG_POOR_SIGNAL,MSG_ATTENTION,MSG_MEDITATION,MSG_BLINK  , MSG_EEG_POWER_HIGHALPHA,MSG_EEG_POWER_LOWALPHA,MSG_EEG_POWER_HIGHBETA,MSG_EEG_POWER_LOWBETA,MSG_EEG_POWER_MIDGAMMA,MSG_EEG_POWER_LOWGAMMA,MSG_EEG_POWER_THETA,MSG_EEG_POWER_DELTA )