from AppKit import NSSound

sound = NSSound.alloc()
sound.initWithContentsOfFile_byReference_('32.mp3', True)
 
sound.play()
