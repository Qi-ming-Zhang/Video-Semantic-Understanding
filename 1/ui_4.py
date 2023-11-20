import cv2 as cv
import os
import random
from model import get_caption_model, generate_caption

def totalnumber_of_videoframes(video_path):  #视频总共帧数 目前没用
    capture = cv.VideoCapture(video_path)
    len_video_frame = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    print('total number of video frames :', len_video_frame)
    n = 0
    loss_frames = []
    for i in range(len_video_frame):
        ret, frame = capture.read()  # ret返回的是True或者False，代表有没有读取到图像
        if ret:
            n += 1
        else:
            print("loss this frame")
            loss_frames.append(i)
    print('index :{}, read: {}'.format(i, n))
    print(loss_frames)


def vidio_frame_extract(video_path, save_path, index):  #把视频每一帧保存图片
    capture = cv.VideoCapture(video_path)
    while capture.isOpened():
        ret, frame = capture.read()  # frame是BGR格式
        if not ret:
            print('loss this frame')
        if frame is None:
            break
        print(frame.shape)  # (795, 1055, 3)
        cv.imshow('frame', frame)
        save_frame = "{}/{:>03d}.png".format(save_path, index)
        cv.imwrite(save_frame, frame)
        index = index + 1
    capture.release()
    cv.destroyAllWindows()


def predict(imgpath):
    captions = []
    pred_caption = generate_caption(imgpath, caption_model)


    captions.append(pred_caption)

    for _ in range(3):
        pred_caption = generate_caption(imgpath, caption_model, add_noise=True)
        print(pred_caption)
        if pred_caption not in captions:
            captions.append(pred_caption)


caption_model=get_caption_model()



if __name__ == "__main__":
    video_path = "D:/student/estvideo.mp4"  #视频路径
    save_path = "D:/student/estvideo"   #保存图片路径
    index = 0
    # totalnumber_of_videoframes(video_path)  # 先看一下视频本身实际有多少帧，再看真正保存的视频帧有多少
    vidio_frame_extract(video_path, save_path, index)  #保存图片到图片路径中
    filelist=os.listdir(save_path)
    samplelist=random.sample(filelist,1)  #调整  随机取一张图片
    for imgpath in samplelist:
        imgrealpath=os.path.join(save_path,imgpath)
        predict(imgrealpath)




