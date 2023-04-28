# Build an avatar with OpenAI, Unreal and Omniverse Audio2Face
## Project Description
Turn text into audio and project it onto audio2face with emotion shown on the text.
## Project Procedure 
<ol>
	<li>Text to speech/Audio</li>
	<li>Sentiment/Emotion Analysis</li>
	<li>Change Emotion</li>
	<li>Push Audio data to Audio2Face (GRPC Request)</li>
	<li>Building Streaming service between Audio2Face and Unreal (OSC server)</li>
</ol>

## Demo
[![IMAGE ALT TEXT]](https://user-images.githubusercontent.com/79441444/234890837-7fd4f2a2-ab41-47e4-9fea-713c3bd09aea.mp4
 "Demo")


## How to Run the Project
Before you begin, you'll need to clone the repository with the template code used in this repo.
###
Omniverse Audio2Face is an application brings our avatars to vivid state. With [Omniverse Audio2Face](https://www.nvidia.com/en-us/omniverse/apps/audio2face/), anyone can now create realistic facial expressions and emotions to match voice-over track. 
#### ***Omniverse Audio2Face***
![](https://i.imgur.com/7ioYQHj.png)
* With [BlendShape](https://www.youtube.com/watch?v=jrZ71xtaJ5E), Metahuman facial animation can be mapped to unreal.
* Other [RESTful-API control](https://www.youtube.com/watch?v=bnLz94I9mZo)
#### Creating an environment from an environment. yml file
Make sure Anaconda is installed on your local machine.\
Create the virtual environment with following commands\
Use the following command to install packages included in requirements.yml:
```
$ conda env create -f /path/to/requirements.yml
```
#### Omniverse Audio2Face setup
Getting the python script interact with the Audio2Face to play the audio, we need to choose streaming audio player instead of playing local data.
To link the streaming player instance to the Metahuman, you need to edit the graph exactly the same as below (also under team folder "Avatar/a2fScripts-setup/a2FsetUp.png").\
![](https://drive.google.com/file/d/1YkkDBe7tQ2v7yinY4KW-bXCeLQswf48Y/view?usp=share_link)
<ol>
	<li>Open the Audio2Face Tab on the top and choose template of "CoreFull Face and Streaming</li>
	<li>In Stage section, click any Graph Node and right Click to open Graph</li>
	<li>Link the Streaming Instance to the CoreFull Face and link the other nodes as the above graph</li>
</ol>


## How It Works

#### ***Text To Speech*** 
* The avatar's innput text converts to audio by the [Gtts API](https://pypi.org/project/gTTS/). The synthesized voice has been used to drive the facial animation on metahumn
#### ***Emotion Analysis***
<ol>
	<li>Use BERT Trained Model to predtict the emotion/sentiment of the analysis.</li>
	<li>Use RESTful API to adjust the emotion before pushing the audio to the A2F.</li>
</ol>

#### ***Push Transferred Audio to A2F***
* Use GRPC Request to upload the audio file to the A2F application
#### ***Streaming Between Unreal and A2F***
* Send Blendshape weight the OSC Server by UDP protocol\
<em><strong>Replace the Blendshape weight ending code in the following address in the machine</strong></em>
```
 C:\Users\innovation_lab\Documents\Omniverse\pkg\audio2face-2022.2.0\exts\omni.audio2face.exporter\omni\audio2face\exporter\scripts\faceSolver.py
```
## Code Explain
1. Use the one of the following code example to run the script
	* call the python script directly
	```
	python main.py Input_String
	```
	* On the Innovative machine, navigate to the batch file ("digitalassociation-main/ttsEmotion/exec.bat")dir and call
	```
	exec.bat "input_str"
	```

2. In the audio2face.py
	* set self.a2f_url to your local host (IPV4/IPV6)-- the default port is 50051
	* set self.avatar_instance to your own Audio2face Streaming instace (same as the prim path of the node)

3. The EmotionPrediction.py currently is unavailable as it requires cuda to load the module. To make the moudle available again
	* run the jupyter notebook in teams-folder under "avatar/sentiment-Analysis/6_sentiment_original_fine-tuned-bert.ipynb" and save the module in the chosen dir.
	* coming back to the EmotionPrediction.py
	```
	model = TFBertModel.from_pretrained('saved_module_dir.h5')
	```
## Unsolved-Integration of Unreal and A2F
	- currently, the unreal will freeze after running python script, so I create a new thread or child-process to trigger A2F application. but the problem is still unsolved.
	- the "threadExec.py" includes both tries














