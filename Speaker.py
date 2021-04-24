#Import library
import pyttsx3 #for Text-to-Speech (tts)
from os import system #for interacting with system
from colorama import init, Fore, Style #for colored-text, and  bright text
import pyfiglet #for making Title
from time import sleep #for waiting

init(autoreset=True, convert=True) #Initialize colorama library

Title = pyfiglet.figlet_format('Speaker', justify="center")#Declare variable Title to string
print(Fore.CYAN + Style.BRIGHT + Title) #Print in varaible Title with cyan color

print(Fore.RED + Style.BRIGHT + '1. Write: Write the message') #Info for "Write" command
print(Fore.RED + Style.BRIGHT + '2. Read: Read the message') #Info about "Read" command
print(Fore.RED + Style.BRIGHT + '   *Read cannot Pause') #Warning about "Read" command
print(Fore.RED + Style.BRIGHT + '3. Reset: Reset the message') #Info about "Reset" command 
print(Fore.RED + Style.BRIGHT + '4. Note: Open Notepad') #Info about "Note" command
print(Fore.RED + Style.BRIGHT + '5. Info: Give Info about command') #Info about itself
print(Fore.RED + Style.BRIGHT + '6. Quit to Quit program') #Info about "Quit" command
print(Fore.RED + Style.BRIGHT + 'Red for system output. Yellow for warn. Green for command') #Color-text Info

sleep(5) #Wait 5 seconds
system('cls') #Clear the terminal system('clear') for linux

message = "" #Set variable 'message' to empty or ''

while True: #Repeat until quit
    command = input(Fore.RED + '>>> ' + Fore.GREEN) #Input command and Declare variable 'message'
    if (command == "Write" or command == "write"):#Detect command "Write", "write"
        system('cls') #Clear the terminal system('clear') for linux
        message = input(Fore.RED + 'message>>> ' + Fore.RESET) #Declare variable 'message' to string
        print(Fore.RED + 'Rewrite successfully') #Alert 'Rewrite successfully with red color
    elif (command == "Read" or command == "read"): #Detect command "Read", "read"
        system('cls') #Clear the terminal system('clear') for linux
        print(Fore.RED + message) #Print variable
        print(Fore.RED + 'If nothing happen that because the message is empty') #Read Warning
        init()# initialize pyttsx3
        pyttsx3.speak(message)# pyttsx3 speak variable 'message'
        pyttsx3.init().runAndWait() # pyttsx3 Run and wait
    elif (command == "Reset" or command == "reset"):
        system('cls') #Clear the terminal system('clear') for linux
        message = "" #Set variable 'message' to empty or ''
        print(Fore.RED + 'Reset successfully') # Alert 'Reset successfully' with red color
    elif (command == "Note" or command == "note"):# Detect command "Note", "note"
        system('notepad') #Open notepad
    elif (command == "Info" or command == "info"): #Detect command "Info", "info"
        print(Fore.RED + Style.BRIGHT + '1. Write: Write the message') #Info for "Write" command
        print(Fore.RED + Style.BRIGHT + '2. Read: Read the message') #Info about "Read" command
        print(Fore.RED + Style.BRIGHT + '   *Read cannot Pause') #Warning about "Read" command
        print(Fore.RED + Style.BRIGHT + '3. Reset: Reset the message') #Info about "Reset" command 
        print(Fore.RED + Style.BRIGHT + '4. Note: Open Notepad') #Info about "Note" command
        print(Fore.RED + Style.BRIGHT + '5. Info: Give Info about command') #Info about itself
        print(Fore.RED + Style.BRIGHT + '6. Quit to Quit program') #Info about "Quit" command
        print(Fore.RED + Style.BRIGHT + 'Red for system output. Yellow for warn. Green for command') #Color-text Inf
    elif (command == "Quit" or command == "quit"): #Detect command "Quit", "quit"
        quit() #Quit program
    else: #If not registered
        print(Fore.RED + 'command: ' + Fore.YELLOW + '"' + command + '"' + Fore.RED + ' not found') #Alert command not register