import pyttsx3

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate
text = 'Hello - World 456'
print(type(text))

for i in range(5):
    # engine.say(text)
    files = "test_" + str(i) + ".aiff"
    print(files)

    '''Save to file hangs in the 3rd run'''
    # engine.save_to_file(text, files)
    # engine.runAndWait()
    
    engine.say(text)
    engine.runAndWait()