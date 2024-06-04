#  <img width="25" height=25 alt="DALL·E" src="https://github.com/sfdeggb/Emind/assets/95692531/77fd75ca-9ab9-4746-8a01-966f8c1902e0"> EMIND:AI Music Recommendation and Generation Copliot
<img width="1000" height=200 alt="DALL·E 2024-06-04 19 40 04 - Design a horizontal logo for 'Music Agent', an AI-powered music recommendation and generation system  The logo should prominently feature musical elem-2" src="https://github.com/sfdeggb/Emind/assets/95692531/342e8269-3b7b-469c-a0cc-7a10a4b52725">


## Interview
EMIND is a multi-functional AI music recommendation and generation system designed to deliver the best music experience through sentiment analysis and personalized recommendations. The system integrates a variety of functions, including text to music, lyrics to melody, voice synthesis, timbre conversion, accompaniment generation, music classification, music separation and lyrics recognition. Using deep learning and multimodal analysis techniques, it is able to generate matching music based on the user's mood. The system uses LLM as the intellectual brain of the system to complete complex music tasks through interaction with local code. It's essentially an AI agent.
## ScreenShot
Below are some screen shots of the system:
![image](https://github.com/sfdeggb/Emind/assets/95692531/fa7ebdb0-8a38-4eee-98a4-d9f78c1144f6)

## Get Stared 
Before you get Started the project,you need to ensure you have the below conditation:
1. Ubuntu 18.04
2. python 3.9
3. NIVIDA CUDA 10.2

On your sysytem you need to run the fllowing code to install necessary os libiray.<br>
``` 
Make sure git-lfs is installed
sudo apt-get update
sudo apt-get install -y git-lfs

Install music-related libs
sudo apt-get install -y libsndfile1-dev
sudo apt-get install -y fluidsynth
sudo apt-get install -y ffmpeg
sudo apt-get install -y lilypond
```

then you can install the necessray packages according to the requremnents.txt.The code is fllowing as!

```
pip install --upgrade pip

pip install semantic-kernel
pip install -r requirements.txt
pip install numpy==1.23.0
pip install protobuf==3.20.3
```

Finally I guess the hardest part of the following is that you need to download a lot of models from the open source community!<br>
**In order to achieve melody generation you need to do：** <br>
firstly, you need to change to models floder.the path is defaule in the project.
then you can do this.  
1> Download the checkpoint and database from the following [link](https://drive.google.com/drive/folders/1TpWOMlRAaUL-R6CRLWfZK1ZeE1VCaubp).  
2> Place the downloaded checkpoint file in the music-ckpt folder.  
3> Create a folder named database to store the downloaded database files.<br>
**In order to achieve the vocal synthesis you need to do this.** <br>
1> make a dictoray named DiffSinger in its models floder.  
2> Down the checkpoint and config from the following [link](https://github.com/MoonInTheRiver/DiffSinger/releases/download/pretrain-model/0228_opencpop_ds100_rel.zip) and unzip it in checkpoints folder. <br>
**In order to achieve the addition of timbre you need to do this**<br>
1> make a dictoray named DDSP in its models floder.  
2> run the fllowing code!  
```
pip install gsutil
mkdir violin; gsutil cp gs://ddsp/models/timbre_transfer_colab/2021-07-08/solo_violin_ckpt/* violin/
mkdir flute; gsutil cp gs://ddsp/models/timbre_transfer_colab/2021-07-08/solo_flute_ckpt/* flute/
```
Finally you can started the project by run `Emind_server.py`

## References
MUZIC:https://github.com/microsoft/muzic<br>
DDSP：https://github.com/magenta/ddsp<br>
DiffSinger： https://github.com/MoonInTheRiver/DiffSinger?tab=readme-ov-file<br>
