""" allsky_lightpollution.py

This module will modify the final image and apply jbeale script (https://forums.raspberrypi.com/viewtopic.php?t=348014#p2085037) to the current image
"""
import allsky_shared as s
import os 
import subprocess
import cv2

metaData = {
    "name": "Remove light pollution",
    "description": "Runs jbeale script to remove light pollution",
    "version": "v1.0.0",
    "events": [
        "night"
    ],
        "arguments":{
        "scriptlocation": ""
    },
    "argumentdetails": {
        "scriptlocation" : {
            "required": "true",
            "description": "File Location",
            "help": "The location of the script to run"
        }
    },
    "changelog": {
        "v1.0.0" : [
            {
                "author": "Emanuel Garcês",
                "authorurl": "https://github.com/effgarces/allsky_lightpollution",
                "changes": "First working version"
            }
        ]                              
    },            
    "module": "allsky_lightpollution"     
}

def lightpollution(params, event):
    script = params["scriptlocation"]

    if os.path.isfile(script):
        if os.access(script, os.X_OK):
            res = subprocess.check_output([script, s.CURRENTIMAGEPATH]) 
            s.image = cv2.imread(s.CURRENTIMAGEPATH)
            result = "Script {0} Executed.".format(script)
        else:
            s.log(0,"ERROR: Script {0} is not executable".format(script))
            result = "Script {0} Is NOT Executeable.".format(script)
    else:
        s.log(0,"ERROR: cannot access {0}".format(script))
        result = "Script {0} Not FOund.".format(script)

    return result
