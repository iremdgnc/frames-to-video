import cv2
import glob
from natsort import natsorted


def create_video(frames_file):
    img_array = []
    files = glob.glob(frames_file)
    sorted_frames = natsorted(files)

    for filename in sorted_frames:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


if __name__ == "__main__":
    create_video(
        frames_file = ''
    )
