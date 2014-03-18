from NeuroPy import NeuroPy
import time
from pac import transform as pt 
from pac import sel as ps

object1=NeuroPy("/dev/tty.MindWaveMobile-DevA",57600)
object1.start()
import Orange
iris = Orange.data.Table("chosen.csv")  #import training data
ann = Orange.classification.neural.NeuralNetworkLearner(iris, n_mid=10, reg_fact=1, max_iter=300, rand=None)

#def return_wave():

#	delta = object1.delta
#	high_alpha = object1.highAlpha 
#	high_beta = object1.highBeta 
#	low_alpha = object1.lowAlpha 
#	low_beta = object1.lowBeta 
#	low_gamma = object1.lowGamma 
#	mid_gamma = object1.midGamma 
#	theta = object1.theta
#	return [delta,high_alpha,high_beta,low_alpha,low_beta,low_gamma,mid_gamma,theta]


#queue = []
while True:
	
	print object1.poorSignal
	print object1.delta

#	if len(queue) == 3:
		# do process data
		#print queue
		#print pt(queue,3)
#		a = ps(pt(queue,3),[0,1,2,3],3)
#		a.append(int(0))
#		print ann(a,Orange.classification.Classifier.GetProbabilities)
#		queue = []
#		queue.append(return_wave())

#	elif object1.poorSignal == 0:

#		queue.append(return_wave())
		
#	else:
#		queue = []
#		queue.append(return_wave())
#	print queue

	time.sleep(1)



