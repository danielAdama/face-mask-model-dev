import os
import cv2

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1
IMG_SIZE = 112
CHANNEL = 3
BATCH_SIZE = 1
BATCH_SIZE2 = 2
LEARNING_RATE = 1e-4
EPOCH = 20
FONT = cv2.FONT_HERSHEY_COMPLEX
CONF_THRESH = 0.5
BASEPATH = r'mask_incorr_no'
# Derive the Training and Testing directories
TRAIN_PATH = os.path.sep.join([BASEPATH,"training"])
VAL_PATH = os.path.sep.join([BASEPATH,"validating"])
TEST_PATH = os.path.sep.join([BASEPATH,"testing"])
DATA_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/face_mask_dataset'
PROTOTXT_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/my_tensorflow/face_mask/face_detector/deploy.prototxt'
WEIGHTS_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/my_tensorflow/face_mask/face_detector/res10_300x300_ssd_iter_140000.caffemodel'
MODEL_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/my_tensorflow/face_mask/'
IMAGE_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/img_test'
MODELV1 = f"{MODEL_PATH}/{'face_mask_detector_Threeclasses.model'}"
MODELV2 = f"{MODEL_PATH}/{'mask_detectorV2.model'}"
MODELV3 = f"{MODEL_PATH}/{'mask_detectorV3.model'}"

