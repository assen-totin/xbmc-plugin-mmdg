#/*
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */

import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import wave, random
import os

__XBMC_Revision__ = xbmc.getInfoLabel('System.BuildVersion')
__settings__      = xbmcaddon.Addon(id='plugin.audio.mozart')
__language__      = __settings__.getLocalizedString
__version__       = __settings__.getAddonInfo('version')
__cwd__           = __settings__.getAddonInfo('path')
__addonname__    = "Mozart"
__addonid__      = "plugin.audio.mozart"
__author__      = "Assen Totin <assen.totin@gmail.com>"

BASE_URL = 'ftp://ftp.cs.princeton.edu/pub/cs126/mozart/mozart.jar'
TMP_FILE_NAME = 'mozart.jar'

CHUNK_SIZE = 1048576

OUTPUT_FILENAME = "waltz.wav"

# Obtain the full path of "userdata/add_ons" directory
def getUserdataDir():
  path = xbmc.translatePath(__settings__.getAddonInfo('profile'))
  res = 0
  if not os.path.exists(path):
    res = getWavFiles(path)
  if res == -1: return "OOPS"
  return path

# Download WAV files
def getWavFiles(path):
  import zipfile, time, urllib2

  os.makedirs(path)
  tmp_file_name = os.path.join(path,TMP_FILE_NAME)
  f = open(tmp_file_name,'wb')

  # Create a dialog
  dialog_was_canceled = 0
  dialog = xbmcgui.DialogProgress()
  dialog.create(__language__(30090), __language__(30091))
  dialog.update(1)

  # Download in chunks of CHUNK_SIZE, update the dialog
  # URL progress bar code taken from triptych (http://stackoverflow.com/users/43089/triptych):
  # See original code http://stackoverflow.com/questions/2028517/python-urllib2-progress-hook
  response = urllib2.urlopen(BASE_URL);
  total_size = response.info().getheader('Content-Length').strip()
  total_size = int(total_size)
  bytes_so_far = 0

  while 1:
    chunk = response.read(CHUNK_SIZE)
    bytes_so_far += len(chunk)

    if not chunk: break

    if (dialog.iscanceled()): 
      dialog_was_canceled = 1
      break

    f.write(chunk)
    percent = float(bytes_so_far) / total_size
    val = int(percent * 100)
    if (val >= 96): val = 96
    dialog.update(val)

  response.close()
  f.close()

  if dialog_was_canceled == 0:
    dialog.update(98, __language__(30092))

    myzip = zipfile.ZipFile(tmp_file_name,'r')
    myzip.extractall(path)
    os.remove(tmp_file_name)

    dialog.update(100, __language__(30093))
    time.sleep(1)
    dialog.close()

    # Check if dialog was canceled during unzipping
    if (dialog.iscanceled()): dialog_was_canceled = 1

  # If the dialog was canceled, remove the directory and files, then exit
  if dialog_was_canceled == 1:
    import sys, shutil
    shutil.rmtree(path)
    return -1

  return 0

# Logging
def log(msg):
  xbmc.output("### [%s] - %s" % (__addonname__,msg,),level=xbmc.LOGDEBUG )

# Log NOTICE
def log_notice(msg):
  xbmc.output("### [%s] - %s" % (__addonname__,msg,),level=xbmc.LOGNOTICE )

# Menuet table (16 bars, 2 dice)
m1 = {'2':96, '3':32, '4':69, '5':40, '6':148, '7':104, '8':152, '9':119, '10':98, '11':3, '12':54}
m2 = {'2':22, '3':6, '4':95, '5':17, '6':74, '7':157, '8':60, '9':84, '10':142, '11':87, '12':130}
m3 = {'2':141, '3':128, '4':158, '5':113, '6':163, '7':27, '8':171, '9':114, '10':42, '11':165, '12':10}
m4 = {'2':41, '3':63, '4':13, '5':85, '6':45, '7':167, '8':53, '9':50, '10':156, '11':61, '12':103}
m5 = {'2':105, '3':146, '4':153, '5':161, '6':80, '7':154, '8':99, '9':140, '10':75, '11':135, '12':28}
m6 = {'2':122, '3':46, '4':55, '5':2, '6':97, '7':68, '8':133, '9':86, '10':129, '11':47, '12':106}
m7 = {'2':11, '3':134, '4':110, '5':159, '6':36, '7':118, '8':21, '9':169, '10':62, '11':147, '12':106}
m8 = {'2':30, '3':81, '4':24, '5':100, '6':107, '7':91, '8':127, '9':94, '10':123, '11':33, '12':5}
m9 = {'2':70, '3':117, '4':66, '5':90, '6':25, '7':138, '8':16, '9':120, '10':65, '11':102, '12':35}
m10 = {'2':121, '3':39, '4':139, '5':176, '6':143, '7':71, '8':155, '9':88, '10':77, '11':4, '12':20}
m11 = {'2':26, '3':126, '4':15, '5':7, '6':64, '7':150, '8':57, '9':48, '10':19, '11':31, '12':108}
m12 = {'2':9, '3':56, '4':132, '5':34, '6':125, '7':29, '8':175, '9':166, '10':82, '11':164, '12':92}
m13 = {'2':112, '3':174, '4':73, '5':67, '6':76, '7':101, '8':43, '9':51, '10':137, '11':144, '12':12}
m14 = {'2':49, '3':18, '4':58, '5':160, '6':136, '7':162, '8':168, '9':115, '10':38, '11':59, '12':124}
m15 = {'2':109, '3':116, '4':145, '5':52, '6':1, '7':23, '8':89, '9':72, '10':149, '11':173, '12':44}
m16 = {'2':14, '3':83, '4':79, '5':170, '6':93, '7':151, '8':172, '9':111, '10':8, '11':78, '12':131}

# Trio table (16 bars, 1 dice):
t1 = {'1':72, '2':56, '3':75, '4':40, '5':83, '6':18}
t2 = {'1':6, '2':82, '3':39, '4':73, '5':3, '6':45}
t3 = {'1':59, '2':42, '3':54, '4':16, '5':28, '6':62}
t4 = {'1':25, '2':74, '3':1, '4':68, '5':53, '6':38}
t5 = {'1':81, '2':14, '3':65, '4':29, '5':37, '6':5}
t6 = {'1':41, '2':7, '3':43, '4':55, '5':17, '6':28}
t7 = {'1':89, '2':26, '3':15, '4':2, '5':44, '6':52}
t8 = {'1':13, '2':71, '3':80, '4':61, '5':70, '6':94}
t9 = {'1':36, '2':76, '3':9, '4':22, '5':63, '6':11}
t10 = {'1':5, '2':20, '3':34, '4':67, '5':85, '6':92}
t11 = {'1':46, '2':64, '3':93, '4':49, '5':32, '6':24}
t12 = {'1':79, '2':84, '3':48, '4':77, '5':96, '6':86}
t13 = {'1':30, '2':8, '3':69, '4':57, '5':12, '6':51}
t14 = {'1':95, '2':35, '3':58, '4':87, '5':23, '6':60}
t15 = {'1':19, '2':47, '3':90, '4':33, '5':50, '6':78}
t16 = {'1':66, '2':88, '3':21, '4':10, '5':91, '6':31}

infiles = []

wav_files_dir = getUserdataDir()

if wav_files_dir != 'OOPS':
  for i in range (1, 17):
    # This could have been one single call, but this will make more true to the spirit of the game
    d1 = random.randrange(6) + 1
    d2 = random.randrange(6) + 1
    d = d1 + d2
    dd = str(d)
    if i == 1: m = m1
    elif i == 2: m = m2
    elif i == 3: m = m3
    elif i == 4: m = m4
    elif i == 5: m = m5
    elif i == 6: m = m6
    elif i == 7: m = m7
    elif i == 8: m = m8
    elif i == 9: m = m9
    elif i == 10: m = m10
    elif i == 11: m = m11
    elif i == 12: m = m12
    elif i == 13: m = m13
    elif i == 14: m = m14
    elif i == 15: m = m15
    elif i == 16: m = m16
    filename = "M%s.wav" % (m[dd])
    filename = os.path.join(wav_files_dir,filename)
    infiles.append(filename)

  for i in range (1, 17):
    d = random.randrange(6) + 1
    dd = str(d)
    if i == 1: t = t1
    elif i == 2: t = t2
    elif i == 3: t = t3
    elif i == 4: t = t4
    elif i == 5: t = t5
    elif i == 6: t = t6
    elif i == 7: t = t7
    elif i == 8: t = t8
    elif i == 9: t = t9
    elif i == 10: t = t10
    elif i == 11: t = t11
    elif i == 12: t = t12
    elif i == 13: t = t13
    elif i == 14: t = t14
    elif i == 15: t = t15
    elif i == 16: t = t16
    filename = "T%s.wav" % (t[dd])
    filename = os.path.join(wav_files_dir,filename)
    infiles.append(filename)

  outfile = os.path.join(wav_files_dir,OUTPUT_FILENAME)

  data= []
  for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(0, 32):
    output.writeframes(data[i][1])
  output.close()

  listen_url = outfile
  log("PLAY URL: %s" % listen_url )

  xbmc.Player().play(listen_url)

## MIDI TEST - CRASHES ON F14 (NO SOUNDFONT)
#listen_url = os.path.join(wav_files_dir,'test.mid')
#try: 
#  xbmc.Player().play(listen_url)
#  midi_support = 1
#except: 
#  midi_support = 0

