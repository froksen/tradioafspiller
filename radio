#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys 
from subprocess import Popen, PIPE, STDOUT
import os
import time
import urllib
import gst
import pygst 

class RadioAfspiller(): 
    radioAfspiller = "gstreamer"
    radioNavn = "Ukendt"
    radioForkortelse ="ukendt"
    radioUrl = "Null"
    radioCopyright = "Ukendt"
    
    def setradioAfspiller(self, Afspiller):
        self.radioAfspiller = Afspiller
        
    def getradioAfspiller(self):
        return self.radioAfspiller
    
    def setradioForkortelse(self, Forkortelse):
        self.radioForkortelse = Forkortelse
    
    def getForkortelse(self):
        return self.radioForkortelse
    
    def fixradioUrl(self,  Url):
        # Henter og åbner den onlinefil
        onlineFil = urllib.urlopen(Url)
        onlineread = onlineFil.readline()
        onlineread = onlineread.replace ('\n', '')
        onlineread = onlineread.replace ('\r', '')
        onlineFil.close()
        
        return onlineread
        
    def setradioUrl(self, Url):       
        self.radioUrl = Url
        
    def getradioUrl(self):
        return self.radioUrl
    
    def setradioNavn(self, Navn):
        self.radioNavn = Navn
    
    def getradioNavn(self):
        return self.radioNavn
    
    def setradioCopyright(self, copyright):
        self.radioCopyright = copyright
    
    def getradioCopyright(self):
        return self.radioCopyright
    
    def setupUI(self):
        print "*************************************************"
        print " - Du lytter til: " + self.getradioNavn()
        print " - Du afspiller med: " + "GStreamer"
        print " "
        print " - Copyright (Program): GPLv2"
        print " - Copyright (Stream): " + self.getradioCopyright()
        print "*************************************************"
        print "Skriv:"
       # print " prog - Afspil med " + self.getradioAfspiller()
        print " stop - Stoppe afspillingen, alt. tryk enter uden at skrive noget"
        print "			--::::--"
   
    def playRadio(self):
        music_stream_uri = self.getradioUrl()
        
        if music_stream_uri[-3:] == "m3u":
            music_stream_uri = self.fixradioUrl(music_stream_uri)
        
        #Sætter Ui'en som brugeren ser.
        self.setupUI()
        
        player = gst.element_factory_make("playbin", "player")
        player.set_property('uri', music_stream_uri)
        player.set_state(gst.STATE_PLAYING)    
        raw_input('Valg [stop]:')


class RadioHelp():
    def kanaler(self):
        print "Kanal forkortelse" + " - " + "Kanal navn"
        for kanalINFO in oversigt:
            print kanalINFO[0] + " - " + kanalINFO[2]
            
    def funktioner(self):
        print ""
        print "Syntaks: radio <funktion>"
        print ""
        print "afspil	-	Afspiller en given radio kanal. Eksempel: radio afspil drp2"
        #print "help kanaler -	Viser en liste over kanaler"
        #print "indstil -	Lader dig bestemme hvilket program du vil bruge til at afspille med"
        print "help	-	Viser dig denne side over funktioner"  

#Sætter standard variabler
radioafspiller = RadioAfspiller()
radiohelp = RadioHelp()

# * Oplysninger om kanaler. Skal læses på følgende måde
# * ("Forkortelse","Url-Til-lyd","Beskrivelse",copyright-for-stream)
oversigt = [
  # * Alle DR radio kanaler
  ( "drp1",  "http://live-icy.gss.dr.dk:8000/Channel3_HQ.mp3", "Danmarks Radio P1","Danmarks Radio" ),
  ( "drp2",  "http://live-icy.gss.dr.dk:8000/Channel4_HQ.mp3", "Danmarks Radio P2","Danmarks Radio" ),
  ( "drp3", "http://live-icy.gss.dr.dk:8000/Channel5_HQ.mp3", "Danmarks Radio P3","Danmarks Radio"),
  ( "drp4syd", "http://live-icy.gss.dr.dk:8000/Channel12_HQ.mp3", "Danmarks Radio P4 Syd","Danmarks Radio"),
  ( "drp4fyn", "http://live-icy.gss.dr.dk:8000/Channel7_HQ.mp3", "Danmarks Radio P4 Fyn","Danmarks Radio" ),
  ( "drp4kbh", "http://live-icy.gss.dr.dk:8000/Channel8_HQ.mp3", "Danmarks Radio P4 København","Danmarks Radio" ),
  ( "drp4bornholm", "http://live-icy.gss.dr.dk:8000/Channel6_HQ.mp3", "Danmarks Radio P4 Bornholm","Danmarks Radio" ),
  ( "drp4midtvest", "http://live-icy.gss.dr.dk:8000/Channel9_HQ.mp3", "Danmarks Radio P4 Midt & Vest","Danmarks Radio" ),
  ( "drp4nord", "http://live-icy.gss.dr.dk:8000/Channel10_HQ.mp3", "Danmarks Radio P4 Nordjylland","Danmarks Radio" ),
  ( "drp4sjælland", "http://live-icy.gss.dr.dk:8000/Channel11_HQ.mp3", "Danmarks Radio P4 Sjælland","Danmarks Radio" ),
  ( "drp4trekanten", "http://live-icy.gss.dr.dk:8000/Channel13_HQ.mp3", "Danmarks Radio P4 Trekanten","Danmarks Radio" ),
  ( "drp4øst", "http://live-icy.gss.dr.dk:8000/Channel14_HQ.mp3", "Danmarks Radio P4 Østjylland","Danmarks Radio" ),
  ( "drp5", "http://live-icy.gss.dr.dk:8000/Channel25_HQ.mp3", "Danmarks Radio P5","Danmarks Radio" ),
  ( "drp6", "http://live-icy.gss.dr.dk:8000/Channel29_HQ.mp3", "Danmarks Radio P6 Beat","Danmarks Radio"),
  ( "drp7", "http://live-icy.gss.dr.dk:8000/Channel21_HQ.mp3", "Danmarks Radio P7 Mix","Danmarks Radio"),
  ( "drp8", "http://live-icy.gss.dr.dk:8000/Channel22_HQ.mp3", "Danmarks Radio P8 Jazz","Danmarks Radio"),
  ( "drmama", "http://live-icy.gss.dr.dk:8000/Channel18_HQ.mp3", "Danmarks Radio Mama","Danmarks Radio"),
  ( "drdansk", "http://live-icy.gss.dr.dk:8000/Channel19_HQ.mp3", "Danmarks Radio Dansk Top","Danmarks Radio"),
  ( "drrama", "http://live-icy.gss.dr.dk:8000/Channel24_HQ.mp3", "Danmarks Radio Ramasjang Radio","Danmarks Radio"),
  ( "drklassisk", "http://live-icy.gss.dr.dk:8000/Channel23_HQ.mp3", "Danmarks Radio Klassisk","Danmarks Radio"),
  ( "drnyheder", "http://live-icy.gss.dr.dk:8000/Channel2_HQ.mp3", "Danmarks Radio Nyheder","Danmarks Radio"),

  # * Andre
  ("radiomojn", "http://mojn.radiostreaming.dk:8050/mojn.m3u","Radio Mojn","Radio Mojn"),
  ("novafm", "http://stream.novafm.dk/nova128.m3u", "Nova FM","Nova.FM"),
  ("skalafm", "http://skala.radiostreaming.dk/Skala128.m3u","Skala.FM", "Skala.FM"),
  ("thevoice", "http://stream.voice.dk/voice128","The Voice", "The Voice"),  
  ]

def onRadioselected(radioForkortelse):
    kanalfundet = 0
    
    for kanal in oversigt:
        if kanal[0] == radioForkortelse:
           radioafspiller.setradioNavn(kanal[2])
           radioafspiller.setradioUrl(kanal[1])
           radioafspiller.setradioCopyright(kanal[3])
           
           kanalfundet = 1
            
           #Starter affspillingingen
           radioafspiller.playRadio()
           

    if kanalfundet == 0:
        radiohelp.kanaler()
        
        print "\n \nUkendt Kanal. Se listen herover"
    else:
        pass

arg1 = 0
try:
    arg1 = sys.argv[1]
except IndexError:
    radiohelp.funktioner()
    pass

arg2 = 0
try:
    arg2 = sys.argv[2]
except IndexError:
    pass

if arg1 == "afspil":
   onRadioselected(arg2)
elif arg1 == "help":
    radiohelp.funktioner()
else:
    for kanal in oversigt:
        if kanal[0] == arg1:
             onRadioselected(arg1)
            
