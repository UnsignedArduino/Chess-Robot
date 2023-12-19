import logging
from time import sleep

import cv2
# noinspection PyUnresolvedReferences
from libcamera import Transform
# noinspection PyUnresolvedReferences
from picamera2 import Picamera2

from utils.logger import create_logger

logger = create_logger(name=__name__, level=logging.DEBUG)

logger.debug("Starting camera")
camera = Picamera2()
config = camera.create_video_configuration(
    raw={"size": (1640, 1232)},
    main={"size": (640, 640)},
    transform=Transform(hflip=True, vflip=True),
)
camera.configure(config)
camera.start()
sleep(1)

logger.debug("Starting captures")
while True:
    image = cv2.cvtColor(camera.capture_array(), cv2.COLOR_RGB2BGR)

    cv2.imshow("live", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
