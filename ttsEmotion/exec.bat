@echo off
echo "before c:"
c: 
echo "before activate"
call C:\Users\innovation_lab\Anaconda3\envs\nemo_tn\Lib\venv\scripts\nt\activate.bat
echo "before d:"
d:
echo "this is a test"
echo %1
python D:\hideki\NLP\Omniverse-Virtual-Assisstant-main\Omniverse-Virtual-Assisstant-main\main.py %1