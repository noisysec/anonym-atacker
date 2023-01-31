import os
import urllib
from twisted.internet import task, reactor
import time

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
os.system("nohup php change.php > /dev/null 2>&1 &")
os.system("clear")
print(colored(255,0,0, '''
                                .-. .-..---. ,-.  .---.-.   .-. .---.,---.   ,--,   
                                |  \| / .-. )|(| ( .-._) \_/ )/( .-._) .-' .' .')   
                                |   | | | |(_|_)(_) \   \   (_|_) \  | `-. |  |(_)  
                                | |\  | | | || |_  \ \   ) (  _  \ \ | .-' \  \     
                                | | |)\ `-' /| ( `-'  )  | | ( `-'  )|  `--.\  `-.  
                                /(  (_))---' `-'`----'  /(_|  `----' /( __.' \____\ 
                               (__)   (_)  DARK ARMY    (__)         (__)            
'''))
def main():
        webUrl = urllib2.urlopen("https://api.proxy.com/loadmod/USA/RUSSIA/INDIA/[1]/?method=local&type=php")
print(colored(255,0,0, 'Wait...'))

timeout = 3.0 # Sixty seconds

def doWork():
        print("Preparing... Your ip is changing...")
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        webUrl = urllib2.urlopen("https://api.proxy.com/loadmod/USA/RUSSIA/INDIA/[1]/?method=local&type=php")

time.sleep(3)
print(colored(255,0,0, 'Youre ANONYMOUS'))
