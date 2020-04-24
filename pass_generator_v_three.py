'''
Locking folders with passsword.
'''

# Imports
import base64
import os
import time
import sys

pw = 344

encode = base64.b64encode(pw)

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    pw = str(raw_input('ENter your password to lock or unlock your folder: '))
    if pw == base64.b64decode(encode):
        # change directory path to where you have LOcker Folder
        os.chdir(r'/home/benny/Desktop/tttses')
        # if locker folder or recycle bin does not exist then we will create locker folder
        if not os.path.exists('Locker'):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.makedir('Locker')
            else:
                os.popen('attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}",'Locker')
                sys.exit()
        else:
            os.rename("Locker","Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            sys.exit()
    
    else:
        print("Wrong Password!,Please Enter the right password")
        time.sleep(5)
        goto(1)