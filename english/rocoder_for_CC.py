from Tkinter import *
import numpy as np
from NeuroPy import NeuroPy
import time
from AppKit import NSSound
import random


RECORD_TIME=7

class App:


    try:
        object1=NeuroPy("/dev/tty.MindWaveMobile-DevA",57600)
    except:
        print 'bluetooth error'

    row_data = []
    f_out = open('output.csv','w')
    f_out.write('delta,midgamma,lowgamma,theta,highalpha,lowalpha,highbeta,lowbeta,state\n')

    cor_or_not = ''

    progress = 0
    audio_seq = []

    ques = []
    answer = []



    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.text = Text(root)
        self.text.insert(INSERT, "Hello.....")
        self.text['width']=150
        self.text.pack(side=LEFT)

        self.qui_btn = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.qui_btn.pack(side=LEFT)

        self.easy_btn = Button(frame, text="easy", command=self.easy)
        self.easy_btn.pack(side=LEFT)
        self.easy_btn['state']='disable'
        self.easy_btn['width']='15'

        self.hard_btn = Button(frame, text="hard", command=self.hard)
        self.hard_btn.pack(side=LEFT)
        self.hard_btn['state']='disable'
        self.hard_btn['width']='15'

        self.sta_btn = Button(frame, text="Start", command=self.start_record)
        self.sta_btn.pack(side=LEFT)
        self.sta_btn['width']='15'

        self.object1.start()




    def easy(self):
        print 'easy'
        self.cor_or_not = 'easy'
        self.easy_btn['state']='disable'
        self.hard_btn['state']='disable'
        self.sta_btn['state'] = 'normal'
        self.text.insert(INSERT, 'easy\n')
        self.text.see(END)

    def hard(self,):
        print 'hard'
        self.cor_or_not = "hard"
        self.easy_btn['state']='disable'
        self.hard_btn['state']='disable'
        self.sta_btn['state'] = 'normal'
        self.text.insert(INSERT, 'hard\n')
        self.text.see(END)


    def start_record(self):

        progress+=1
        if self.object1.poorSignal!=0:
            print 'signal is poor'
            self.text.insert(INSERT, 'bad signal\n')
        
        else:
            delta = []
            midgamma = []
            lowgamma = []
            theta = []
            highalpha = []
            lowalpha = []
            highbeta = []
            lowbeta = []


            self.text.insert(INSERT, 'progress:'+str(self.progress)+':\n')
            self.text.see(END)



            for i in range(0,RECORD_TIME):
                if self.object1.poorSignal!=0:
                    print "because signal("+str(self.object1.poorSignal)+") is bad, we skip this round."
                    break
                else:
                    delta.append(self.object1.delta)
                    midgamma.append(self.object1.midGamma)
                    lowgamma.append(self.object1.lowGamma)
                    theta.append(self.object1.theta)
                    highalpha.append(self.object1.highAlpha)
                    lowalpha.append(self.object1.lowAlpha)
                    highbeta.append(self.object1.highBeta)
                    lowbeta.append(self.object1.lowBeta)
                    print 'recording'
                    print self.object1.poorSignal
                    time.sleep(1)

            if len(delta)==RECORD_TIME:
                #print "std(delta)="+str(int(np.std(np.array(delta))))
                #print "std(midgamma)="+str(int(np.std(np.array(midgamma))))
                #print "std(lowgamma)="+str(int(np.std(np.array(lowgamma))))
                #print "std(theta)="+str(int(np.std(np.array(theta))))

                self.row_data.append(delta)
                self.row_data.append(midgamma)
                self.row_data.append(lowgamma)
                self.row_data.append(theta)
                self.row_data.append(highalpha)
                self.row_data.append(lowalpha)
                self.row_data.append(highbeta)
                self.row_data.append(lowbeta)


                print self.row_data

                self.easy_btn['state']='normal'
                self.hard_btn['state']='normal'
                self.sta_btn['state'] = 'disabled'

            

            sound.stop()

    def write_data(self,state,correct):

        for ele in self.row_data:
            for data in ele[:-1]:
                self.f_out.write(str(data)+'-')
            self.f_out.write(str(ele[-1]))
            self.f_out.write(',')
        self.f_out.write(state+'\n')
        self.row_data = []
        print '=============write=============='





root = Tk()

app = App(root)

root.mainloop()
root.destroy()