import datetime
import time
import subprocess

############
# Settings #
############
# specify recordings length
hours, minutes, seconds = 1, 0, 0
framerate = 25

#############
# Recording #
#############
length = hours * 60 * 60 + minutes * 60 + seconds
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d_%H-%M-%S")
filename  = f"screen_{now}.mp4"

capture_command = ["bash", "screencapture.sh", filename]
kill_command    = ["bash", "kill_ffmpeg.sh"]

print(" ".join(capture_command))
process = subprocess.Popen( capture_command, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
time.sleep(length)
print("Ending recording...")
print(" ".join(kill_command))
process.terminate()
process.kill()
process.wait()
subprocess.call(kill_command)
print(process.returncode)
print(process.stdout)
