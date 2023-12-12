import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/aersa/wan_wan/kansetsutsuu_ude.png")

print(img.shape)

print(plt.imshow(img))
