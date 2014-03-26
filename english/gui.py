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
    f_out.write('delta,midgamma,lowgamma,theta,highalpha,lowalpha,highbeta,lowbeta,state,answer\n')

    un_or_dont = ''

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

        self.un_btn = Button(frame, text="Understand", command=self.know)
        self.un_btn.pack(side=LEFT)
        self.un_btn['state']='disable'
        self.un_btn['width']='20'

        self.don_btn = Button(frame, text="Don't understand", command=self.dont_know)
        self.don_btn.pack(side=LEFT)
        self.don_btn['state']='disable'
        self.don_btn['width']='20'

        self.A_btn = Button(frame, text="A", command=self.process_A)
        self.A_btn.pack(side=LEFT)
        self.A_btn['state']='disable'
        self.A_btn['width']='20'

        self.B_btn = Button(frame, text="B", command=self.process_B)
        self.B_btn.pack(side=LEFT)
        self.B_btn['state']='disable'
        self.B_btn['width']='20'

        self.C_btn = Button(frame, text="C", command=self.process_C)
        self.C_btn.pack(side=LEFT)
        self.C_btn['state']='disable'
        self.C_btn['width']='20'

        self.sta_btn = Button(frame, text="Start", command=self.start_record)
        self.sta_btn.pack(side=LEFT)
        self.sta_btn['width']='20'

        for i in range(11,41):
            self.audio_seq.append(i)
        random.shuffle(self.audio_seq)

        answer_sheet = open("answer_sheet.txt",'r')

        for row in answer_sheet:

            self.ques.append(row.split('::')[1])
            self.answer.append(row.split('::')[2])

        print "english audio sequence:"+str(self.audio_seq)


        self.object1.start()


    def know(self):
        print 'I know'
        self.un_or_dont = 'know'
        self.un_btn['state']='disable'
        self.don_btn['state']='disable'
        self.A_btn['state']='normal'
        self.B_btn['state']='normal'
        self.C_btn['state']='normal'
        choices = self.ques[int(self.audio_seq[self.progress])-11].split('(')
        for cho in choices:
        	self.text.insert(INSERT, cho+'\n')
        self.text.see(END)

    def dont_know(self,):
        print 'dont know'
        self.un_or_dont = "don't know"
        self.un_btn['state']='disable'
        self.don_btn['state']='disable'
        self.A_btn['state']='normal'
        self.B_btn['state']='normal'
        self.C_btn['state']='normal'
        choices = self.ques[int(self.audio_seq[self.progress])-11].split('(')
        for cho in choices:
        	self.text.insert(INSERT, cho+'\n')
        self.text.see(END)

    def process_A(self):
        print 'choose A'

        if self.answer[int(self.audio_seq[self.progress])-11][0] == 'A':
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'correct'
            self.write_data(self.un_or_dont,'correct')
        else:
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'wrong'
            self.write_data(self.un_or_dont,'wrong')
        self.sta_btn['state'] = 'normal'
        self.A_btn['state']='disable'
        self.B_btn['state']='disable'
        self.C_btn['state']='disable'
        self.progress+=1

    def process_B(self):
        print 'choose B'

        if self.answer[int(self.audio_seq[self.progress])-11][0] == 'B':
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'correct'
            self.write_data(self.un_or_dont,'correct')
        else:
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'wrong'
            self.write_data(self.un_or_dont,'wrong')
        self.sta_btn['state'] = 'normal'
        self.A_btn['state']='disable'
        self.B_btn['state']='disable'
        self.C_btn['state']='disable'
        self.progress+=1

    def process_C(self):
        print 'choose C'

        if self.answer[int(self.audio_seq[self.progress])-11][0] == 'C':
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'correct'
            self.write_data(self.un_or_dont,'correct')
        else:
            print 'the answer is:'+self.answer[int(self.audio_seq[self.progress])-11]
            print 'wrong'
            self.write_data(self.un_or_dont,'wrong')
        self.sta_btn['state'] = 'normal'
        self.A_btn['state']='disable'
        self.B_btn['state']='disable'
        self.C_btn['state']='disable'
        self.progress+=1


    def start_record(self):

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

            self.text.insert(INSERT,'\n\n')
            self.text.insert(INSERT, 'progress:'+str(self.progress)+':\n')
            self.text.insert(INSERT, 'question:'+str(self.audio_seq[self.progress])+':\n')
            self.text.see(END)
            print str(self.audio_seq[self.progress])

            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(str(self.audio_seq[self.progress])+'.mp3', True)
            sound.play()


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

                self.un_btn['state']='normal'
                self.don_btn['state']='normal'
                self.sta_btn['state'] = 'disabled'

            
                #for i in range(0,5):
                #    self.row_data.append(int(np.std(np.array(delta[0:RECORD_TIME-i]))))
                #    self.row_data.append(int(np.std(np.array(midgamma[0:RECORD_TIME-i]))))
                #    self.row_data.append(int(np.std(np.array(lowgamma[0:RECORD_TIME-i]))))
                #    self.row_data.append(int(np.std(np.array(theta[0:RECORD_TIME-i]))))

            sound.stop()

    def write_data(self,state,correct):

        for ele in self.row_data:
            for data in ele[:-1]:
                self.f_out.write(str(data)+'-')
            self.f_out.write(str(ele[-1]))
            self.f_out.write(',')
        self.f_out.write(state+','+correct+'\n')
        self.row_data = []
        print '=============write=============='





root = Tk()

app = App(root)

root.mainloop()
root.destroy()