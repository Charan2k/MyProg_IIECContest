# MyProg_IIECContest
#Solution for the Use Case Theory Contest of IIEC Rise Python by Vimal Daga Sir.



import pyttsx3 as tts
import os


while True:
    print("What do you want me to do: ")
    print("Chat here:", end=' ')
    p=input()
    
    
    if ("open" in p or "run" in p or "execute" in p or "launch" in p):
    
        if ("chrome" in p or "browser" in p):
            tts.speak("Do you want to open any specific website?")
            print("Yes / No: ", end=' ')
            ask=input()
            if "yes" in ask or "Yes" in ask:
                tts.speak("what website:")
                print("what website:", end=' ')
                b=input()
            else:
                tts.speak("Press Enter")
                b=input()
            
            tts.speak("Launching Chrome, Please Wait")
            x= "chrome "+b
            os.system(x)
            
            
        elif ("notepad" in p or "text editor" in p):
            tts.speak("Launching Notepad, Please Wait")
            os.system("notepad")
          
        
        elif ("media player" in p or "video player" in p):
            tts.speak("Launching Windows Media Player, Please Wait")
            os.system("wmplayer")
            
            
        elif("ms word" in p or "word" in p):
            tts.speak("Launching MS Word, PLease Wait")
            os.system("WINWORD")
            
            
        elif("ms powerpoint" in p or "powerpoint" in p):
            tts.speak("Launching MS Powerpoint, PLease Wait")
            os.system("POWERPOINT")
    
    
        elif("ms excel" in p or "excel" in p or "spreadsheet" in p):
            tts.speak("Launching MS Excel, PLease Wait")
            os.system("EXCEL")
            
    
        elif("image editor" in p or "photoshop" in p):
            tts.speak("Launching Adobe Photoshop, PLease Wait")
            os.system("Photoshop")
        
        
        elif("illustrator" in p):
            tts.speak("Launching Adobe Illustrator, PLease Wait")
            os.system("Illustrator")
        
        
        elif("after effects" in p or "video editor" in p):
            tts.speak("Launching Adobe AfterEffects, PLease Wait")
            os.system("AfterFX")
            
            
    elif("quit" in p or "exit" in p or "end" in p or "done" in p): 
        print("---------------------QUITTING---------------------")
        tts.speak("Okay, Quitting ")
        break
        
        
    else:
        tts.speak("Sorry, I am Unable to Understand. Please type in a way I can Understand")
    

