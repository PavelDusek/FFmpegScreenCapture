kill `ps aux | grep "ffmpeg -f x11grab" | awk 'NR==1 {print $2}'`
