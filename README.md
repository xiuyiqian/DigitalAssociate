# Build an avatar with OpenAI, Unreal and Omniverse Audio2Face
## Project Description
Turn text into audio and project it onto audio2face with emotion shown on the text.
## Project Procedure 
1.Text to speech/Audio\
2.Sentiment/Emotion Analysis\
3.Change Emotion\
4.Push Audio data to Audio2Face (GRPC Request)\
5.Building Streaming service between Audio2Face and Unreal (OSC server)\
## Demo
[![IMAGE ALT TEXT]](https://user-images.githubusercontent.com/79441444/234890837-7fd4f2a2-ab41-47e4-9fea-713c3bd09aea.mp4
 "Demo")


## How to Run the Project
Before you begin, you'll need to clone the repository with the template code used in this repo.
###
Omniverse Audio2Face is an application brings our avatars to vivid state. With [Omniverse Audio2Face](https://www.nvidia.com/en-us/omniverse/apps/audio2face/), anyone can now create realistic facial expressions and emotions to match voice-over track. 
#### ***Omniverse Audio2Face***
![](https://i.imgur.com/7ioYQHj.png)
#### Creating an environment from an environment. yml file
Make sure Anaconda is installed on your local machine.\
Create the virtual environment with following commands\
Use the following command to install packages included in requirements.yml:
```
$ conda env create -f /path/to/requirements.yml
```
#### Omniverse Audio2Face setup
Getting the python script interact with the Audio2Face to play the audio, we need to choose streaming audio player instead of playing local data.
To link the streaming player instance to the Metahuman, you need to edit the graph exactly the same as below.\
![](https://bmwgroup.sharepoint.com/:i:/r/teams/est-Innovators/Freigegebene%20Dokumente/General/Avatar/a2fScripts-setup/a2FsetUp.png?csf=1&web=1&e=SPeerd)
** To open the blueprint,

## How It Works

#### ***Text To Speech*** 
The avatar's innput text converts to audio by the [Gtts API](https://pypi.org/project/gTTS/). The synthesized voice has been used to drive the facial animation on metahumn
#### ***Emotion Analysis***
1. Use BERT Trained Model to predtict the emotion/sentiment of the analysis.\
2. Use RESTful API to adjust the emotion before pushing the audio to the A2F.\
#### ***Push Transferred Audio to A2F***











