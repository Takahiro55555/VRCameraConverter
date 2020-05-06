import cv2
import numpy as np


def capture_camera(mirror=True, size=None):
    """カメラ画像をキャプチャし表示する
    コピペ元：https://qiita.com/wkentaro/items/3d3bee56445894da879e

    Keyword Arguments:
        mirror {bool} -- [description] (default: {True})
        size {[type]} -- [description] (default: {None})
    """
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        # フレームを表示する
        cv2.imshow('camera capture', convert_frame(frame))

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()


def convert_frame(frame, width=1334, height=750, draw_marker=False):
    frame_height, frame_width, _ = frame.shape

    magnification = height / frame_height  # 拡大率
    resized_image_width = int(frame_width*magnification)
    resized_image = cv2.resize(frame, (resized_image_width, height))


    if draw_marker:
        # 画像の中心にマーカーを描画する
        cv2.drawMarker(resized_image, (int(resized_image_width/2)-25, int(height/2)-25), (0, 0, 255),
                    markerType=cv2.MARKER_CROSS, markerSize=50, thickness=1, line_type=cv2.LINE_8)

    trimed_image_width = int(width / 2)
    trimed_image = resized_image[0:height, int(resized_image_width/2) - int(
        trimed_image_width/2): int(resized_image_width/2) + int((trimed_image_width/2))]

    # NOTE: 同じ画像を2枚横に並べているが、２眼カメラを導入した際はきちんと左右の画像をそれぞれ設定すること
    converted_frame = np.hstack([trimed_image, trimed_image])  # 2つの配列（画像）を横に結合

    return converted_frame


if __name__ == "__main__":
    capture_camera(mirror=False)
