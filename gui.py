from Tkinter import *
import numpy as np
from NeuroPy import NeuroPy
import time
from AppKit import NSSound


sound = NSSound.alloc()

class App:

    object1=NeuroPy("/dev/tty.MindWaveMobile-DevA",57600)
    row_data = []
    f_out = open('output.csv','w')
    f_out.write('delta,midgamma,lowgamma,state\n')

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Understand", command=self.know)
        self.hi_there.pack(side=LEFT)

        self.hi_there = Button(frame, text="Don't understand", command=self.dont_know)
        self.hi_there.pack(side=LEFT)

        self.hi_there = Button(frame, text="Start", command=self.start_record)
        self.hi_there.pack(side=LEFT)

        self.object1.start()


    def know(self):
        print 'I know'
        print self.row_data
        self.write_data('know')

    def dont_know(self):
        print 'dont know'
        print self.row_data
        self.write_data("don't know")

    def start_record(self):
        delta = []
        midgamma = []
        lowgamma = []


        sound.initWithContentsOfFile_byReference_('Cloud Nothings - Stay Useless.mp3', True)
        sound.play()


        for i in range(1,6):
            if self.object1.poorSignal!=0:
                print "because signal("+str(self.object1.poorSignal)+") is bad, we skip this round."
                break
            else:
                delta.append(self.object1.delta)
                midgamma.append(self.object1.midGamma)
                lowgamma.append(self.object1.lowGamma)
                print 'record'
                time.sleep(1)
        if len(delta)==5:
            print "std(delta)="+str(int(np.std(np.array(delta))))
            print "std(midgamma)="+str(int(np.std(np.array(midgamma))))
            print "std(lowgamma)="+str(int(np.std(np.array(lowgamma))))

            self.row_data=[int(np.std(np.array(delta))),int(np.std(np.array(midgamma))),int(np.std(np.array(lowgamma)))]

        sound.stop()

    def write_data(self,state):

        for ele in self.row_data:
            self.f_out.write(str(ele)+',')
        self.f_out.write(state+'\n')





root = Tk()

app = App(root)

root.mainloop()
root.destroy()