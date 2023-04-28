# Running the Demo

import sys
from audio2face import Audio2FaceService
from setEmotion import setEmo

args = sys.argv[1:]
print(sys.argv)
inputStr = args[0]
setEmo(inputStr.strip())

if len(inputStr.strip())!=0:
    audio2face_service = Audio2FaceService()
    audio2face_service.make_avatar_speaks(inputStr)

# "D:\Program Files\Epic Games\UE_5.0\Engine\Binaries\ThirdParty\Python3\Win64\python.exe"