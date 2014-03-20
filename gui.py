from Tkinter import *
from NeuroPy import NeuroPy
import time
from AppKit import NSSound
sound = NSSound.alloc()

class App:

    #object1=NeuroPy("/dev/tty.MindWaveMobile-DevA",57600)

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

        #self.object1.start()


    def know(self):
        print 'I know'

    def dont_know(self):
        print 'dont know'

    def start_record(self):
        print sound.initWithContentsOfFile_byReference_('Cloud Nothings - Stay Useless.mp3', True)
        sound.play()
        for i in range(1,6):
            #print self.object1.poorSignal
            #print self.object1.delta
            print 'record'
            time.sleep(1)
        
        sound.stop()





root = Tk()

app = App(root)

root.mainloop()
root.destroy()