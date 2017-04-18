"""
 A simple Python modle for recording matplotlib animation

 author: Atsushi Sakai
"""

import matplotlib.pyplot as plt
import subprocess

iframe = 0


def save_frame():
    """
    Save a frame for movie
    """
    global iframe

    plt.savefig("recoder" + str(iframe) + '.png')
    iframe += 1


def save_movie_mp4(fname, d_pause):
    """
    Save movie as mp4
    """
    cmd = "ffmpeg -f image2 -r " + str(1.0 / d_pause) + \
        " -i recoder%01d.png -vcodec mpeg4 -y " + fname
    subprocess.call(cmd, shell=True)

    cmd = "rm recoder*.png"
    subprocess.call(cmd, shell=True)


def save_movie_gif(fname, d_pause):
    """
    Save movie as gif
    """
    cmd = "convert " + \
        " recoder*.png " + fname
    subprocess.call(cmd, shell=True)
    cmd = "rm recoder*.png"
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    print("A sample recording start")
    import math

    time = range(10)

    x1 = [math.cos(t / 10.0) for t in time]
    y1 = [math.sin(t / 10.0) for t in time]
    x2 = [math.cos(t / 10.0) + 2 for t in time]
    y2 = [math.sin(t / 10.0) + 2 for t in time]

    for ix1, iy1, ix2, iy2 in zip(x1, y1, x2, y2):
        plt.plot(ix1, iy1, "xr")
        plt.plot(ix2, iy2, "xb")
        plt.axis("equal")
        plt.pause(0.1)

        save_frame()  # save each frame

    #  save_movie_mp4("animation.mp4", 0.1)
    save_movie_gif("animation.gif", 0.1)
