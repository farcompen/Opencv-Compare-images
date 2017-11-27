#! /usr/bin python
# -*- coding:UTF-8 -*-

import matplotlib.pyplot as plt


from skimage.measure import structural_similarity as ssim

import numpy as np

import cv2



def MSE (Resim1, Resim2):

    hata = np.sum((Resim1.astype("float") - Resim2.astype("float"))**2)
    hata /= float(Resim1.shape[0]* Resim1.shape[1])
    return hata






def resim_karsilastir(Resim1, Resim2, title):

    m = MSE(Resim1, Resim2)
    s = ssim(Resim1, Resim2)

    fig = plt.figure(title)
    plt.suptitle ("MSE: %.2f, ssim: %.2f " % (m, s ))

    #ilk resmi göster
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(Resim1, cmap = plt.cm.gray)
    plt.axis ("off")

    #ikinci resim göster
    ax= fig.add_subplot(1, 2, 2)
    plt.imshow(Resim2, cmap = plt.cm.gray)
    plt.axis("off")

    plt.show()



orjinalResim = cv2.imread("resim1.jpg")

kontrastli = cv2.imread("resim2.jpg")

#resimleri gray scale yapalım

orjinal = cv2.cvtColor(orjinalResim, cv2.COLOR_BGR2GRAY)

kontrastligray = cv2.cvtColor(kontrastli, cv2.COLOR_BGR2GRAY)


fig = plt.figure("Images")
Images = ("Orjinal", orjinal), ("Kontrasli", kontrastligray)


for (i, (name, image)) in enumerate (Images):
    #resim goster
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap = plt.cm.gray)
    plt.axis("off")

plt.show()


resim_karsilastir(orjinal, orjinal, "orjinal vs  orjinal")

resim_karsilastir(orjinal, kontrastligray, "orjinal vs kontrasli")
