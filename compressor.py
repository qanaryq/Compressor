import os
import ffmpeg

cwd = os.getcwd()

if not os.path.exists("Videos"):
    os.mkdir(os.path.join(cwd, "Videos"))

if not os.path.exists("Output_Videos"):
    os.mkdir(os.path.join(cwd, "Output_Videos"))

command = input(
    "Enter ffmpeg command as shown (inputfile), (outputfile), (resolution), (bitrate): "
)

simple_com = "".join(c for c in [ch for ch in command if ch not in ["(", ")", ","]]).split(" ")

inp = ""
out = ""
resolution = []
bitrate = ""
options = []

for com in simple_com:
    try:
        if com.startswith("input_file"):
            inp = os.path.join(cwd, "Videos", com.split("=")[1])

        if com.startswith("output_file"):
            
            out = os.path.join(cwd, "Output_Videos", com.split("=")[1])

        if com.startswith("resolution"):
            resolution = com.split("=")[1].split("x")

        if com.startswith("bitrate"):
            bitrate = com.split("=")[1]

        if com.startswith("reverse"):
            options.append("reverse=1")

    except IndexError:
        continue

input_video = ffmpeg.input(inp)
output_video = (
    input_video.filter("scale", resolution[0], resolution[1])
    .output(out, vb=bitrate, vcodec="h264_nvenc", acodec="aac", audio_bitrate="196k", preset="fast",map="0")
)

ffmpeg.run(output_video)
