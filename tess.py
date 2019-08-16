import sys
import cv2
import pytesseract
from PIL import Image


def upscale(file_name):
    img = cv2.imread(file_name)
    # TODO change this according to the size of the img instead of hardcode value
    res = cv2.resize(img, dsize=(540, 140), interpolation=cv2.INTER_CUBIC)
    img = Image.fromarray(res, 'RGB')
    return img


def extract_text(image):
    custom_oem_psm_config = r'--oem 3 --psm 6 -l eng'
    result = pytesseract.image_to_string(image, config=custom_oem_psm_config)
    return result


def main():
    file_name = sys.argv[1]
    upscaled_img = upscale(file_name)
    result = extract_text(upscaled_img)
    print(result)


if __name__ == '__main__':
    main()
