# Allsky module for the removal of light pollution

This module for the Allsky Camera project will process the captured image and apply jbeale script (https://forums.raspberrypi.com/viewtopic.php?t=348014#p2085037) to it

## Installation

1 - Place the file ``lightpollution.sh`` in a folder of your choice (it's advisable to save it somewhere on the home folder, for instance ~/myscripts)
2 - Make the .sh file executable by running chmod + lightpollution.sh
3 - Copy the allsky_lightpollution.py file to the allsky/scripts/module folder
4 - Over at the Allsky Module manager, in Night Capture enable the module and fill the the scriptlocation

## Credits

- [jbeale](https://forums.raspberrypi.com/viewtopic.php?t=348014#p2085037)
- [Alex-developer](https://github.com/AllskyTeam/allsky-modules/discussions/82#discussioncomment-8361878)
