#all audio inputs (with microphone):
ffmpeg -f x11grab -video_size 1360x768 -framerate 25 -i $DISPLAY -f alsa -i default -c:v libx264 -pix_fmt yuv420p -preset ultrafast -c:a aac $1 

