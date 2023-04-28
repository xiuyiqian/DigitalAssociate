import platform
import os
import threading
import _thread
import subprocess

print(platform.platform())
print("getting current process: ", os.getpid())
cmd = r"D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\exec.bat "
#chat_gpt_answer = "BMW is a German multinational manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany. Automobiles are marketed under the brands BMW, Mini and Rolls-Royce, and motorcycles are marketed under the brand BMW Motorrad.Its subsidiaries are Mini , Rolls-Royce , BMW i and BMW Bank . BMW is the world leader in sales among high-end manufacturers; It primarily competes with Audi , Volvo , Lexus , and Mercedes-Benz , among other high-end vehicles"

class myThread (threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.cmd = command
        
    def run(self):
        print ("Starting " + self.cmd)
        r = subprocess.Popen([cmd,"BMW is a German multi national manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany."], shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print ("Exiting " + self.cmd)


    
if platform.system() == "Windows":
    # Create new threads
    thread1 = myThread(cmd)
    thread1.start()
    thread1.join()
#_thread.start_new_thread(os.system, (cmd,))
else:
    print()
        


print ("Exiting Main Thread")

#subprocess.Popen([r"D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\exec.bat {0}".format(chat_gpt_answer)], shell=True)