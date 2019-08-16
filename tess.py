import sys
import cv2
from PIL import Image

file_name = sys.argv[1]
img = cv2.imread(file_name)
res = cv2.resize(img, dsize=(540, 140), interpolation=cv2.INTER_CUBIC)
img = Image.fromarray(res, 'RGB')
img.save('resized_{}'.format(file_name))
