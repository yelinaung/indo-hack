import time
import cv2 as cv
import sys
import numpy as np
from PIL import Image


def create_resized_mask(img, mask):
    # create a copy of the original image
    img_mask_bg = img.copy()
    # fill up the whole image with same color
    img_mask_bg[:] = (255, 255, 255)

    img_bg = Image.fromarray(img_mask_bg)

    mask = Image.fromarray(mask)
    bg_w, bg_h = img_bg.size
    img_w, img_h = mask.size

    # calculate the offset to put the mask image in the center
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

    # overlap the two image
    img_bg.paste(mask, offset, None)

    return img_bg


def remove_water_mark(img, mask, radius=10, flag=cv.INPAINT_TELEA):
    t1 = time.time()
    result = cv.inpaint(src=img, inpaintMask=mask, inpaintRadius=radius, flags=flag)
    t2 = time.time()
    print(f"it takes {t2 - t1}")
    return result


def main():
    file_name = sys.argv[1]
    mask_name = sys.argv[2]

    img = cv.imread(file_name, cv.IMREAD_UNCHANGED)
    mask = cv.imread(mask_name, 0)

    result = remove_water_mark(img=img, mask=mask)

    cv.imwrite(f"removed_{file_name}", result)


# how to run
# python watermark.py sample_portrait.jpg mask_portrait_fixed_size.jpg
if __name__ == "__main__":
    main()
