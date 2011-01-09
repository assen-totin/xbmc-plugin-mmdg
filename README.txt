GENERAL

This is a simple XBMC add-on to generate random waltz theme following Mozarts' Musicl Dice Game (Musikalisches Würfelspiel). 

Each waltz consist of two parts: a menuet (16 bars of music) and a trio (another 16 bars). Mozart wrote a total of 272 pieces which get randomly combined to produce an unique piece of music every time (originally cmobinations were obtained using dice roll, hence the name)

Python coding: Assen Totin, <assen.totin@gmail.com>

Original score and table of combinations: Wolfgang Amadeus Mozart (1756-1791)

WAV files found at Princeton University's public FTP, ftp://ftp.cs.princeton.edu/pub/cs126/mozart/mozart.jar 


INSTALL

Move the "plugin.audio.mozart" directory into your "addons" directory.


NOTES

This implementation uses pre-built WAV files. While this makes it compatible with all ports of XBMC, it has one small disadvantage: the WAV files are about 35 MB and take some time to initially download them. This can be circumvented by using MIDI files, which will be much smaller (all 272 take less than 1 MB). However, this will make the add-on less compatible, since not all platforms can XBMC play MIDI files out of the box (e.g., on Linux you need to manually install a soundfont of approx 100 MB, which no all users decide to do). It will be probably best to have both implemented plus acheck whether the host supports MIDI (then use it), else revert to WAV. 


