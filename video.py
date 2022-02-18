import cv2
import os

def makevideo(framen,res,fps):
    image_folder = '.'
    video_name = 'misc/video.avi'

    video = cv2.VideoWriter(video_name, 0, fps, res)
    for i in range(framen):
        video.write(cv2.imread(os.path.join(image_folder, f"frames/frame{i}.png")))

    cv2.destroyAllWindows()
    video.release()