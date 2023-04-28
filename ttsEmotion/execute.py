import subprocess
import platform
import os

print(platform.platform())
print("getting current process: ", os.getpid())

chat_gpt_answer = "BMW is a German multi national manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany. Automobiles are marketed under the brands BMW, Mini and Rolls-Royce, and motorcycles are marketed under the brand BMW Motorrad.Its subsidiaries are Mini , Rolls-Royce , BMW i and BMW Bank . BMW is the world leader in sales among high-end manufacturers; It primarily competes with Audi , Volvo , Lexus , and Mercedes-Benz , among other high-end vehicles"
cmd = r"D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\exec.bat"
if platform.system() == "Windows":

    #result = subprocess.call([r"D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\exec.bat {0}".format(chat_gpt_answer)])
    #os.system(r"D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\exec.bat {0}".format(chat_gpt_answer.strip()))
    r = subprocess.Popen([cmd,"BMW is a German multi national manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany."], shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print(r)
    #print("result subprocess: ", str(result))
else:
    print()
    
