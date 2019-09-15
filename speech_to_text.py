import azure.cognitiveservices.speech as speechsdk
import json
import time

def getSetting(key):
    with open('./config.json', 'r') as conf:
        return json.loads(conf.read())[key]
    
"""
Go to the website below for more details about the code.
https://docs.microsoft.com/da-dk/azure/cognitive-services/speech-service/quickstart-python#sample-code
"""    


# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "0eafaa07632e4872b8dba79022e3e27b", "northeurope"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result = speech_recognizer.recognize_once()

# Checks result.
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
        
        
print("Almost ready")
time.sleep(4)
print("start again")
speech_recognizer.start_continuous_recognition_async()
time.sleep(10)
speech_recognizer.stop_continuous_recognition_async()

        