#!/bin/bash
# Post-process timelapse images using imagemagick:
# blur each image, to model smooth light pollution background
# subtract background from image, leaving small features (eg. stars)
# brighten image (a whole lot) with an S-curve
# adjust contrast so JPEG black=0 visually matches MP4 video black level
echo "Removing Light Polution from $1"
convert \( $1 -depth 16 -brightness-contrast -3x0 \
     -blur 0x7 -write mpr:blur1 +delete \) \
  \( mpr:blur1 $1 -compose minus-dst -composite \) \
  \( -sigmoidal-contrast 6,5% \) \
  \( -brightness-contrast 0,-6 \) \
  $1
