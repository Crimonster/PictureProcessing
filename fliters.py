import cv2
import numpy as np
import math
from functools import reduce
from PIL import ImageGrab


def capture(left, top, right, bottom):
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    r, g, b = cv2.split(img)
    cv2.merge([b, g, r], img)
    return img


oimg = cv2.imread('2.jpg')


# 边界填充 以边界为轴反射
def border_fill(m, n, img):
    top_size, bottom_size, left_size, right_size = (m/2, m/2, n/2, n/2)

    reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
    return reflect101


def arithmetic_mean_filter(oimg, m, n):
    """
    算术均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m,n,oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = 0
                for l in timg:
                    for u in l:
                        r += u
                dimg[j, i, d] = r / (m * n)
    return dimg


def geometric_mean_filter(oimg, m, n):
    """
    cannot work
    集合均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = 1
                for l in timg:
                    for u in l:
                        r *= int(u)
                dimg[j, i, d] = r ** (1 / m / n)

    return dimg


def harmonic_mean_filter(oimg, m, n):
    """
    谐波均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = 0
                for l in timg:
                    for u in l:
                        r += 1 / int(u if u != 0 else 1)
                dimg[j, i, d] = m * n / r
    return dimg


def inverse_harmonic_mean_filter(oimg, m, n, q):
    """
    逆谐波均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :param q: 参数阶数
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = 0
                s = 0
                for l in timg:
                    for u in l:
                        r += int(u)**(q+1)
                        s += int(u)**q
                dimg[j, i, d] = r / s if s != 0 else 255
    return dimg


def median_filter(oimg, m, n):
    """
    中职滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = []
                for l in timg:
                    for u in l:
                        r.append(u)
                r.sort()
                dimg[j, i, d] = r[len(r) // 2]
    return dimg


def max_filter(oimg, m, n):
    """
    最大值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = []
                for l in timg:
                    for u in l:
                        r.append(u)
                r.sort()
                dimg[j, i, d] = r[-1]
    return dimg


def min_filter(oimg, m, n):
    """
    最小值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = []
                for l in timg:
                    for u in l:
                        r.append(u)
                r.sort()
                dimg[j, i, d] = r[0]
    return dimg


def midpoint_filter(oimg, m, n):
    """
    中点滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = []
                for l in timg:
                    for u in l:
                        r.append(u)
                r.sort()
                dimg[j, i, d] = (r[0] + r[-1]) / 2
    return dimg


def alpha_prime_median_filter(oimg, m, n):
    """
    修正后的阿尔法均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :param d: 参数
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    bfimg = border_fill(m, n, oimg)
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(oimg.shape[1]):
            for j in range(oimg.shape[0]):
                timg = bfimg[j:j+m, i: i+n, d]
                r = []
                for l in timg:
                    for u in l:
                        r.append(u)
                r.sort()
                dimg[j, i, d] = reduce(lambda x, y: x+y, r[d//2:-d//2]) / (m * n - d)
    return dimg


def tidal_filter(oimg, h):
    """
    算术均值滤波器
    :param oimg: 原图像
    :param m: 窗口宽度
    :param n: 窗口高度
    :paran h: 函数。(d)->bool
    :return: 处理后图像
    """
    width, height, dim = oimg.shape
    dimg = np.zeros((width, height, dim), np.uint8)
    for d in range(dim):
        for i in range(dimg.shape[1]):
            for j in range(dimg.shape[0]):
                dimg[j, i, d] = oimg(j, i, d) * h(oimg(j, i, d))
    return dimg


oimg = cv2.imread('2.jpg')
cv2.imshow('oimg', oimg)
cv2.imshow('dimg', median_filter(oimg, 10, 10))
cv2.waitKey()
