from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import os, subprocess, signal

def kill_gphoto2():
    pipe = subprocess.Popen(["ps", "-A"], stdout=subprocess.PIPE)
    out, err = pipe.communicate()

    for line in out.splitlines():
        #print line
        if "gvfsd-gphoto2" in line:
            pid = int( line.split(None, 1)[0] )
            os.kill(pid, signal.SIGKILL)

def clean_camera_SD():
    print "cleaning ..."
    ds_dir = "/store_00020001/DCIM/100CANON"
    delete_cmd = ["--folder", ds_dir, "-R", "--delete-all-files"]
    gp(delete_cmd)

def getSinglePhoto():
    print "tajing your photo ..."
    trigger_cmd = ["--capture-image"]
    gp(trigger_cmd)
    sleep(3)
    transferPhoto()
    sleep(3)

def transferPhoto():
    print "Copying photos"
    get_cmd = ["--get-all-files"]
    gp(get_cmd)

kill_gphoto2()
getSinglePhoto()
clean_camera_SD()