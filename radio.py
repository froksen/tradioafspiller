import sys 
from subprocess import Popen, PIPE, STDOUT
import os


#  * Saetter variablerne
try:
  hovedfunktion = sys.argv[1]
except IndexError:
  pass

try:
  underfunktion = sys.argv[2]
except IndexError:
  pass

# * Vaelg en afspiller, og udkommenter den anden. PT er valget mellem VLC eller mplayer
afspillerprogram = "mplayer"
#afspillerprogram = "vlc -I ncurses"


# * Oplysninger om kanaler. Skal laeses paa foelgende maade
# * ("Forkortelse","Url-Til-lyd","Beskrivelse",copyright-for-stream)
oversigt = [
  # * Alle DR radio kanaler
  ( "drp1",  "http://live-icy.gss.dr.dk:8000/Channel3_HQ.mp3", "Danmarks Radio P1","Danmarks Radio" ),
  ( "drp2",  "http://live-icy.gss.dr.dk:8000/Channel4_HQ.mp3", "Danmarks Radio P2","Danmarks Radio" ),
  ( "drp3", "http://live-icy.gss.dr.dk:8000/Channel5_HQ.mp3", "Danmarks Radio P3","Danmarks Radio"),
  ( "drp4syd", "http://live-icy.gss.dr.dk:8000/Channel12_HQ.mp3", "Danmarks Radio P4 Syd","Danmarks Radio"),
  ( "drp7", "http://live-icy.gss.dr.dk:8000/Channel21_HQ.mp3", "Danmarks Radio P7","Danmarks Radio"),

  # * Andre
  ("radiomojn", "http://mojn.radiostreaming.dk:8050/mojn.m3u","Radio Mojn Soenderjyllands foerende radiostation","Radio Mojn"),
  ("novafm", "http://stream.novafm.dk/nova128.m3u", "Nova FM"),
  ("skalafm", "http://skala.radiostreaming.dk/Skala128.m3u","Skala FM"),
  ("thevoice", "http://stream.voice.dk/voice128","The Voice Danmarks Hitstation.", "The Voice"),  
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
    print "help kanaler-	Viser en liste over kanaler"
    print "help	-	Viser dig denne side over funktioner"  

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

# * Tjekker om afspillingsprogrammet findes, ellers stopper den afviklingen af scriptet og beder om at det bliver installeret.
def peterlyberthtesten(afspillerprogram):
    afspiller = afspillerprogram.split( )
    if os.path.exists("/usr/bin/"+afspiller[0]):
      pass
    else:
      print "\n"
      print "*************************************..::Hey du!::..***********************************"
      sys.exit("Fejl! Du har ikke afspillingsprogrammet " + afspiller[0] + " installeret. Installer det eller brug en anden afspiller \n")

# * Koerer testen om afspiller programmet findes. Opkaldt efter ham som ikke liige tjekkede om mplayer var installeret
peterlyberthtesten(afspillerprogram)

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