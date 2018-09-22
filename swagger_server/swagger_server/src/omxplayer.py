import subprocess

from swagger_server.src import cec


def reset():
    pipe = ''
    subprocess.run('rm ' + pipe)
    subprocess.run('pkill omxplayer')


def send_key(key):
    pipe = ''
    # if (!pipe) return
    subprocess.run('echo -n ' + key + ' > ' + pipe)


def start():
    cec.turn_on_and_switch_tv()
    # if (!pipe && playlistVideos.length > 0)
    #     var video = playlistVideos.shift()
    #     var videoFile = video.file
    #     var option = video.option
    #     var tempPipe = 'omxcontrol' + guid()
    #     pipe = tempPipe
    #     subprocess.run('mkfifo ' + pipe)
    #     videoPlaying = true
    #     videoPause = false
    #     io.emit("pause",
    #         playing: videoPlaying,
    #         pause: videoPause
    #     )
    #     if (!option)
    #         option = ""

    #     console.log('omxplayer "' + videoFile + '" ' + option + ' < ' + pipe)
    #     subprocess.run('omxplayer "' + videoFile + '" ' + option + ' < ' + pipe, function(error, stdout, stderr)
    #         console.log(stdout)
    #         console.log("killing temp pipe")
    #         if (pipe == tempPipe)
    #             subprocess.run('rm ' + tempPipe)
    #             pipe = false

    #         if (playlistVideos.length > 0)
    #             omx.start()

    #         if (onFinish)
    #             onFinish(error, stdout, stderr)

    #     )
    #     subprocess.run('echo . > ' + tempPipe)
