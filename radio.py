import sys 
from subprocess import Popen, PIPE, STDOUT
import os

# * Vaelg en afspiller, og udkommenter den anden. PT er valget mellem VLC eller mplayer
afspillerprogram = "mplayer"
#afspillerprogram = "vlc -I ncurses"


#  * Saetter variablerne
try:
  hovedfunktion = sys.argv[1]
except IndexError:
  pass

try:
  underfunktion = sys.argv[2]
except IndexError:
  pass

# * Tjekker om afspillingsprogrammet findes, ellers stopper den afviklingen af scriptet og beder om at det bliver installeret.
def peterlyberthtesten(afspillerprogram):
    afspiller = afspillerprogram.split( )
    if os.path.exists("/usr/bin/"+afspiller[0]):
      pass
    else:
      print "\n"
      print "*************************************..::Hey du!::..***********************************"
      sys.exit("Fejl! Du har ikke afspillingsprogrammet " + afspiller[0] + " installeret. Installer det eller brug en anden afspiller \n")

# * Tjekker om "systemmappen", altsaa den gemte mappe med information om afspiller osv. findes i $HOME mappen. Derefter koerer testen om afspiller programmet findes. Opkaldt efter ham som ikke liige tjekkede om mplayer var installeret.
peterlyberthtesten(afspillerprogram)


# * Oplysninger om kanaler. Skal laeses paa foelgende maade
# * ("Forkortelse","Url-Til-lyd","Beskrivelse",copyright-for-stream)
oversigt = [
  # * Alle DR radio kanaler
  ( "drp1",  "http://live-icy.gss.dr.dk:8000/Channel3_HQ.mp3", "Danmarks Radio P1","Danmarks Radio" ),
  ( "drp2",  "http://live-icy.gss.dr.dk:8000/Channel4_HQ.mp3", "Danmarks Radio P2","Danmarks Radio" ),
  ( "drp3", "http://live-icy.gss.dr.dk:8000/Channel5_HQ.mp3", "Danmarks Radio P3","Danmarks Radio"),
  ( "drp4syd", "http://live-icy.gss.dr.dk:8000/Channel12_HQ.mp3", "Danmarks Radio P4 Syd","Danmarks Radio"),
  ( "drp4fyn", "http://live-icy.gss.dr.dk:8000/Channel7_HQ.mp3", "Danmarks Radio P4 Fyn","Danmarks Radio" ),
  ( "drp4kbh", "http://live-icy.gss.dr.dk:8000/Channel8_HQ.mp3", "Danmarks Radio P4 Koebenhavn","Danmarks Radio" ),
  ( "drp4bornholm", "http://live-icy.gss.dr.dk:8000/Channel6_HQ.mp3", "Danmarks Radio P4 Bornholm","Danmarks Radio" ),
  ( "drp4midtvest", "http://live-icy.gss.dr.dk:8000/Channel9_HQ.mp3", "Danmarks Radio P4 Midt & Vest","Danmarks Radio" ),
  ( "drp4nord", "http://live-icy.gss.dr.dk:8000/Channel10_HQ.mp3", "Danmarks Radio P4 Nordjylland","Danmarks Radio" ),
  ( "drp4sjaelland", "http://live-icy.gss.dr.dk:8000/Channel11_HQ.mp3", "Danmarks Radio P4 Sjaelland","Danmarks Radio" ),
  ( "drp4trekanten", "http://live-icy.gss.dr.dk:8000/Channel13_HQ.mp3", "Danmarks Radio P4 Trekanten","Danmarks Radio" ),
  ( "drp4oest", "http://live-icy.gss.dr.dk:8000/Channel14_HQ.mp3", "Danmarks Radio P4 Oestjylland","Danmarks Radio" ),
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

# * Alt vedr. hjaelp funktionen
def help(helpfunktion):  
  if helpfunktion == "afspil":
    print ""
    print "Syntaks: radio afspil <kanalvalg>"
    print ""
    print "<kanalvalg>	-	Beskrivelse"
    print "----------------------------------"
    for kanal in oversigt:
      print kanal[0]+"	-	"+kanal[2]
   
  if helpfunktion == "kanaler":
    help("afspil")
        
  if helpfunktion == "alt":
    print ""
    print "Syntaks: radio <funktion>"
    print ""
    print "afspil	-	Afspiller en given radio kanal. Eksempel: radio afspil drp2"
    print "help kanaler -	Viser en liste over kanaler"
    print "indstil -	Lader dig bestemme hvilket program du vil bruge til at afspille med"
    print "help	-	Viser dig denne side over funktioner"  

def indstil(indstilling):
    if indstilling == "afspiller":
      global afspillerprogram
      afspillervalg = raw_input("Skriv navnet paa afspilleren du vil bruge: ")
      afspillerprogram = config.afspillerprogrammer[afspillervalg]
      #afspil("drp3")

# * Alt vedr. selve afspillingen
def afspil(radiokanalvalg):
  
  for radiokanal in oversigt:
    if radiokanal[0] == radiokanalvalg:
      stationfundet = "ja"
      
      print "*************************************************"
      print " - Du lytter til: " + radiokanal[2]
      print " - Du afspiller med: " + afspillerprogram
      print " "
      print " - Copyright (Program): GPLv2"
      print " - Copyright (Stream): " + radiokanal[3]
      print "*************************************************"
      print "Tryk Ctrl+C eller q for at stoppe afspillingen"
      
      player_choice_and_radio_station = afspillerprogram + " " + radiokanal[1]
      p = Popen(player_choice_and_radio_station, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
      output = p.stdout.read()
      
      stationfundet = "nej"
 
  # * Hvis radiokanalen ikke blev fundet, da viser den listen over kanaler
  if stationfundet == "nej":
      help("afspil")


# * Alt vedr. valg af funktion!
try:
  if hovedfunktion == "afspil":
    afspil(underfunktion)
  else:
    pass
except NameError:
    help("afspil")

try:
  if hovedfunktion == "help":
    help(underfunktion)
  else:
    pass
except NameError:
    help("alt")

try:
  if hovedfunktion == "indstil":
    indstil(underfunktion)
  else:
    pass
except NameError:
    help("alt")