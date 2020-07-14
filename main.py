import cv2
import os 
from license_recog.detector import LP_Detector 
from license_recog.utils import *


cfg_path = './configs/server_api.yaml'
config = get_cfg(cfg_path)

img_path = config['input']['image']
img = cv2.imread(img_path)


# init model
LP_Recognizer = LP_Detector(config)

# preprocessing 
input_img,resized,origin  = preprocess_img(img)

# predict
lp_image, is_square = LP_Recognizer.get_plate(input_img,resized,origin)

if not os.path.exists("logs/outputs"):
    os.makedirs("logs/outputs")

if lp_image is not None:
    print (f"[INFO] Check the result at: logs/outputs")
    cv2.imwrite('logs/outputs/output.png',lp_image)
    lp_string = LP_Recognizer.get_number(lp_image)
    print ("[INFO] License Plate:",lp_string)
else:
    print (f"[INFO] Didnt recognize license plate")