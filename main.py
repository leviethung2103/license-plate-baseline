import cv2
import os 
from license_recognition import models
from license_recognition.utils.tools import get_cfg
from license_recognition.utils.tools import preprocess_img

# show available models
models.show_avai_models()


cfg_path = './configs/server_api.yaml'

config = get_cfg(cfg_path)

# init WPOD & OCR model
wpod_model = models.build_model('wpod',cfg_path)
ocr_model = models.build_model('ocr',cfg_path)

# prepare data
img_path = config['input']['image']
img = cv2.imread(img_path)

# preprocessing 
input_img,resized,origin  = preprocess_img(img)

# predict
lp_image, is_square = wpod_model.get_plate(input_img,resized,origin)

if not os.path.exists("logs/outputs"):
    os.makedirs("logs/outputs")

if lp_image is not None:
    print (f"[INFO] Check the result at: logs/outputs")
    cv2.imwrite('logs/outputs/output.png',lp_image)
    lp_string = ocr_model.get_number(lp_image)
    print ("[INFO] License Plate:",lp_string)
else:
    print (f"[INFO] Didnt recognize license plate")