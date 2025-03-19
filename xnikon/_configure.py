# -*- coding: utf-8 -*-
"""
Created on 2025/03/19 20:58:58
@author: Whenxuan Wang
@email: wwhenxuan@gmail.com
"""
from PIL import Image
import piexif

from typing import Optional, Dict

zeroth_ifd = {
        piexif.ImageIFD.Make: "NIKON CORPORATION",  # 相机制造厂商的名字
        piexif.ImageIFD.Model: "NIKON D750",  # 使用相机的具体型号
    }

exif_ifd = {
        piexif.ExifIFD.LensMake: "",  # 镜头制造厂商的名称
        piexif.ExifIFD.LensModel: "",   # 镜头的具体型号
        piexif.ExifIFD.FNumber: (2200, 100),  # 拍摄照片的光圈值，以分数的形式存储
        piexif.ExifIFD.ISOSpeedRatings: 160,  # 拍摄照片的感光度
        piexif.ExifIFD.FocalLength: (7000, 100),  # 使用镜头的焦距，以分数的形式存储
        piexif.ExifIFD.FocalLengthIn35mmFilm: 70,  # 镜头的35mm等效焦距
        piexif.ExifIFD.ExposureTime: (1, 50),  # 拍摄照片的曝光时间
        piexif.ExifIFD.DateTimeOriginal: "2025:03:17 00:56:51",  # 照片拍摄的具体时间
        piexif.ExifIFD.WhiteBalance: 0,  # 白平衡设置，0表示自动白平衡
        piexif.ExifIFD.ExposureProgram: 3,  # 表示曝光程序
        piexif.ExifIFD.MeteringMode: 0,  # 表示测光模式
    }



def read_configure(image_path: str, return_bytes: bool = False) -> bytes | Dict:
    """读取一张图片的EXIF配置"""
    exif_dict = piexif.load(image_path)
    # 是否要以字符串的形式返回
    if return_bytes is True:
        return piexif.dump(exif_dict)
    return exif_dict

def reconfigure():
    """重新修改图像的EXIF数据"""


if __name__ == '__main__':
    dic = read_configure('../images/cat.jpg')
    for key, value in dic.items():
        if isinstance(value, dict):
            for k, v in value.items():
                print(key, k, v)
        else:
            print(key, value)
