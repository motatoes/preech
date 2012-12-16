import sys
import signal



"""
libDir = "'C:\\Users\\Mohd\\Downloads\\sphinx\\sphinx 4-1\\sphinx4-1.0beta6\\lib\\"
classPaths = [
    "sphinx4.jar",
    "jsapi.jar",
    "WSJ_8gau_13dCep_16k_40mel_130Hz_6800Hz.jar"
]

import os
for classPath in classPaths:
    sys.path.append(libDir + classPath +"'" ) ;
print sys.path
"""
true = 1
false = 0



from edu.cmu.sphinx.decoder import Decoder
from edu.cmu.sphinx.decoder import ResultListener
from edu.cmu.sphinx.decoder.pruner import SimplePruner
from edu.cmu.sphinx.decoder.scorer import ThreadedAcousticScorer
from edu.cmu.sphinx.decoder.search import PartitionActiveListFactory
from edu.cmu.sphinx.decoder.search import SimpleBreadthFirstSearchManager
from edu.cmu.sphinx.frontend import DataBlocker
from edu.cmu.sphinx.frontend import FrontEnd
from edu.cmu.sphinx.frontend.endpoint import NonSpeechDataFilter
from edu.cmu.sphinx.frontend.endpoint import SpeechClassifier
from edu.cmu.sphinx.frontend.endpoint import SpeechMarker
from edu.cmu.sphinx.frontend.feature import DeltasFeatureExtractor
from edu.cmu.sphinx.frontend.feature import LiveCMN
from edu.cmu.sphinx.frontend.filter import Preemphasizer
from edu.cmu.sphinx.frontend.frequencywarp import MelFrequencyFilterBank
from edu.cmu.sphinx.frontend.transform import DiscreteCosineTransform
from edu.cmu.sphinx.frontend.transform import DiscreteFourierTransform
from edu.cmu.sphinx.frontend.util import AudioFileDataSource
from edu.cmu.sphinx.frontend.window import RaisedCosineWindower
from edu.cmu.sphinx.instrumentation import BestPathAccuracyTracker
from edu.cmu.sphinx.instrumentation import MemoryTracker
from edu.cmu.sphinx.instrumentation import SpeedTracker
from edu.cmu.sphinx.jsgf import JSGFGrammar
from edu.cmu.sphinx.linguist.acoustic import UnitManager
from edu.cmu.sphinx.linguist.acoustic.tiedstate import Sphinx3Loader
from edu.cmu.sphinx.linguist.acoustic.tiedstate import TiedStateAcousticModel
from edu.cmu.sphinx.linguist.dictionary import FastDictionary
from edu.cmu.sphinx.linguist.flat import FlatLinguist
from edu.cmu.sphinx.recognizer import Recognizer
from edu.cmu.sphinx.util import LogMath
from java.util.logging import Logger
from java.util.logging import Level
from java.net import URL
from java.util import ArrayList
from edu.cmu.sphinx.util.props import *
import sys
# if (args.length < 1) {

#current directory is passed as an argument for now cause
#os.getdir() returns System32 folde on windows ._.
currentDir =  sys.argv[1]
cm = ConfigurationManager(URL("file:" + currentDir + "\sphinx.config.xml")) ;

recognizer = cm.lookup("recognizer");
recognizer.allocate();

#start the microphone or exit if the programm if this is not possible
microphone = cm.lookup("microphone");
if (not microphone.startRecording()):
    print("Cannot start microphone.");
    recognizer.deallocate();
    exit(1);

#print("Recognizer initialize, start speaking now");

# loop the recognition until the programm exits.
while (true):
    try:
        result = recognizer.recognize();

        if (result is not None ):
            resultText = result.getBestFinalResultNoFiller();
            print(resultText);
        else:
            pass
            #print("I can't hear what you said.");
    except KeyboardInterrupt:
        print "Bye"
        sys.exit()

