import cv2
import numpy as np

net_torch=cv2.dnn.readNetFromTorch("./data/torch_enet_model.net")

net_tensorflow = cv2.dnn.readNetFromTensorflow("./data/tensorflow_inception_graph.pb")

