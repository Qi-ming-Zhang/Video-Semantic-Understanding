import cv2 as cv
import os
import random
from model import get_caption_model, generate_caption
from PIL import Image
import ui_5

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
    flag=True
    total=500+index
    while capture.isOpened() and flag:
        ret, frame = capture.read()  # frame是BGR格式
        if not ret:
            print('loss this frame')
        if frame is None:
            break
        print(frame.shape)  # (795, 1055, 3)
        cv.imshow('frame', frame)
        save_frame = "{}/{:>03d}.png".format(save_path, index)
        cv.imwrite(save_frame, frame)
        index = index + 40
        print(index)
        if index>total:
           flag=False
    capture.release()
    cv.destroyAllWindows()


def predict(imgpath):
    captions = []
    pred_caption = generate_caption(imgpath, caption_model)


    captions.append(pred_caption)
    trs_list = []
    for _ in range(3):
        pred_caption = generate_caption(imgpath, caption_model, add_noise=True)
        print('预测内容:',pred_caption)
        trs=ui_5.translate(pred_caption, 'en', 'zh')
        print('预测内容:', trs)
        trs_list.append(trs)
        if pred_caption not in captions:
            captions.append(pred_caption)

    return trs_list


caption_model=get_caption_model()



if __name__ == "__main__":
    # video_path = r"F:\图\8.20海朗德公园\058A1394.MP4"  #视频路径
    save_path = r"D:\img"   #保存图片路径
    index = 100
    # # totalnumber_of_videoframes(video_path)  # 先看一下视频本身实际有多少帧，再看真正保存的视频帧有多少
    # vidio_frame_extract(video_path, save_path, index)  #保存图片到图片路径中
    filelist=os.listdir(save_path)
    samplelist=random.sample(filelist,1)  #调整  随机取一张图片
    print(samplelist)
    for imgpath in samplelist:
        print(imgpath)
        imgrealpath=os.path.join(save_path,imgpath)
        im=Image.open(imgrealpath)
        im.show()
        predict(imgrealpath)




