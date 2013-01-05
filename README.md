This is a mini-project that is part of my masters program at university of Birmingham. Preech is a sublime Text 2 plugin that  adds speech based programming functionality to sublime in order to allow programmers to dictate their code. Preech uses CMU sphinx to perform Speech-To-text. The project is still in pre-alpha state and is not yet usable.


Check out a demo video: http://youtu.be/58OhMEKnHa0

Prerequisites
=============
- Java SE: Java SE 6 Development Kit or better. Go to http://java.sun.com, and select "J2SE" from popular downloads. Download JDK.
- Sublime text 2 (http://www.sublimetext.com/2)

How to test it 
=================
- download the entire master repository as a .Zip file by clicking on "zip" above. 
- Unzip the file and rename the folder to "preech"
- Open your sublime text 2 editor
- Click on preferences > browse packages ...
- copy the folder "preech" (that you just unzipped) into the folder that shows up (the packages folder)
- restart sublime text 2
- click File , you should see the Preech menu there (http://i.imgur.com/piqj3.png)


Starting speech recognition
------------------------------
- it's best to have your command panel open when testing to see the recognized words and any other errors. you can open it by clicking CTRL + ` (that's not a colon it's the key above your TAB key on most keyboards) 
- Start a new file. don't call it anything so that sublime's autocomplete doesn't interfere with the speech
- MAKE SURE THE CURSOR IS IN THE FILE , then click on file > Preech > Start Dictation 




