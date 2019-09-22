#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:12:36 2019

@author: younessubhi
"""

### TEXT TO SPEECH ###
import settingsAzure
import os, requests, time
from xml.etree import ElementTree

subscription_key = settingsAzure.key1

class TextToSpeech(object):
    def __init__(self, subscription_key):
        self.subscription_key = subscription_key
        self.tts = input("What would you like to convert to speech: ")
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    '''
    The TTS endpoint requires an access token. This method exchanges your
    subscription key for an access token that is valid for ten minutes.
    '''
    def get_token(self):
        fetch_token_url = settingsAzure.endpoint1
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self):
        base_url = 'https://northeurope.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        voice.set('name', 'da-DK-HelleRUS') # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)'
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        '''
        If a success response is returned, then the binary audio is written
        to file in your working directory. It is prefaced by sample and
        includes the date.
        '''
        if response.status_code == 200:
            with open('sample-' + self.timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

    def get_voices_list(self):
        base_url = 'https://northeurope.tts.speech.microsoft.com/'
        path = 'cognitiveservices/voices/list'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
        }
        response = requests.get(constructed_url, headers=headers)
        if response.status_code == 200:
            print("\nAvailable voices: \n" + response.text)
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

if __name__ == "__main__":
    app = TextToSpeech(subscription_key)
    app.get_token()
    app.save_audio()
    #app.get_voices_list()
    

###
#import requests
#import settingsAzure
#import time
#from xml.etree import ElementTree
#import os
#
#subscription_key = settingsAzure.key1
#
#try:
#    input = raw_input
#except NameError:
#    pass
#
#
#class TextToSpeech(object):
#    def __init__(self, subscription_key):
#        self.subscription_key = settingsAzure.key1
#        self.tts = input("What would you like to convert to speech: ")
#        self.timestr = time.strftime("%Y%m%d-%H%M")
#        self.access_token = None
#        
#def get_token(self):
#    fetch_token_url = settingsAzure.endpoint1
#    headers = {
#        'Ocp-Apim-Subscription-Key': self.subscription_key
#    }
#    response = requests.post(fetch_token_url, headers=headers)
#    self.access_token = str(response.text)
#
#def save_audio(self):
#    base_url = 'https://northeurope.tts.speech.microsoft.com/cognitiveservices/v1'
#    path = 'cognitiveservices/v1'
#    constructed_url = base_url + path
#    headers = {
#        'Authorization': 'Bearer ' + self.access_token,
#        'Content-Type': 'application/ssml+xml',
#        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
#        'User-Agent': 'KimSpeech'
#    }
#    xml_body = ElementTree.Element('speak', version='1.0')
#    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
#    voice = ElementTree.SubElement(xml_body, 'voice')
#    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
#    voice.set(
#        'name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
#    voice.text = self.tts
#    body = ElementTree.tostring(xml_body)
#
#    response = requests.post(constructed_url, headers=headers, data=body)
#    if response.status_code == 200:
#        with open('sample-' + self.timestr + '.wav', 'wb') as audio:
#            audio.write(response.content)
#            print("\nStatus code: " + str(response.status_code) +
#                  "\nYour TTS is ready for playback.\n")
#    else:
#        print("\nStatus code: " + str(response.status_code) +
#              "\nSomething went wrong. Check your subscription key and headers.\n")
#
#if __name__ == "__main__":
#    subscription_key = settingsAzure.key1
#    app = TextToSpeech(subscription_key)
#    app.get_token()
#    app.save_audio()
#    
#####

#
#def get_token(subscription_key):
#    fetch_token_url = settingsAzure.endpoint1
#    headers = {
#        'Ocp-Apim-Subscription-Key': subscription_key
#    }
#    response = requests.post(fetch_token_url, headers=headers)
#    access_token = str(response.text)
#    print(access_token)
#    
#import os, requests, time
#from xml.etree import ElementTree
#
##if 'SPEECH_SERVICE_KEY' in os.environ:
##    subscription_key = os.environ['subscription_key']
##else:
##    print('Environment variable for your subscription key is not set.')
##    exit()
#
#class TextToSpeech(object):
#    def __init__(self, subscription_key):
#        self.subscription_key = subscription_key
#        self.tts = input("What would you like to convert to speech: ")
#        self.timestr = time.strftime("%Y%m%d-%H%M")
#        self.access_token = None
#
#    '''
#    The TTS endpoint requires an access token. This method exchanges your
#    subscription key for an access token that is valid for ten minutes.
#    '''
#    def get_token(self):
#        fetch_token_url = settingsAzure.endpoint1
#        headers = {
#            'Ocp-Apim-Subscription-Key': self.subscription_key
#        }
#        response = requests.post(fetch_token_url, headers=headers)
#        self.access_token = str(response.text)
#
#    def save_audio(self):
#        base_url = settingsAzure.endpoint2
#        path = 'cognitiveservices/v1'
#        constructed_url = base_url + path
#        headers = {
#            'Authorization': 'Bearer ' + self.access_token,
#            'Content-Type': 'application/ssml+xml',
#            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
#            'User-Agent': 'YOUR_RESOURCE_NAME'
#        }
#        xml_body = ElementTree.Element('speak', version='1.0')
#        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
#        voice = ElementTree.SubElement(xml_body, 'voice')
#        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
#        voice.set('name', 'en-US-Guy24kRUS') # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)'
#        voice.text = self.tts
#        body = ElementTree.tostring(xml_body)
#
#        response = requests.post(constructed_url, headers=headers, data=body)
#        '''
#        If a success response is returned, then the binary audio is written
#        to file in your working directory. It is prefaced by sample and
#        includes the date.
#        '''
#        if response.status_code == 200:
#            with open('sample-' + self.timestr + '.wav', 'wb') as audio:
#                audio.write(response.content)
#                print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
#        else:
#            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
#
#    def get_voices_list(self):
#        base_url = settingsAzure.endpoint2
#        path = 'cognitiveservices/voices/list'
#        constructed_url = base_url + path
#        headers = {
#            'Authorization': 'Bearer ' + self.access_token,
#        }
#        response = requests.get(constructed_url, headers=headers)
#        if response.status_code == 200:
#            print("\nAvailable voices: \n" + response.text)
#        else:
#            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
#
#if __name__ == "__main__":
#    app = TextToSpeech(subscription_key)
#    app.get_token()
#    app.save_audio()
#    # Get a list of voices https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech#get-a-list-of-voices
#    # app.get_voices_list()