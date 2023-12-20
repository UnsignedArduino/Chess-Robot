import logging
from time import sleep

import cv2
# noinspection PyUnresolvedReferences
from libcamera import Transform
# noinspection PyUnresolvedReferences
from picamera2 import Picamera2

from cv.board import chessboard_cv_split_into_squares
from cv.configuration import IMAGE_SIZE
from cv.debug.board import chessboard_cv_draw_square_lines
from utils.logger import create_logger

logger = create_logger(name=__name__, level=logging.DEBUG)

logger.debug("Starting camera")
camera = Picamera2()
config = camera.create_video_configuration(
    raw={"size": (1640, 1232)},
    main={"size": (IMAGE_SIZE, IMAGE_SIZE)},
    transform=Transform(hflip=True, vflip=True),
)
camera.configure(config)
camera.start()
sleep(1)

logger.debug("Starting captures")
while True:
    image = cv2.cvtColor(camera.capture_array(), cv2.COLOR_RGB2BGR)

    squares = chessboard_cv_split_into_squares(image)
    cv2.imshow("square_a1", squares[0])

    image = chessboard_cv_draw_square_lines(image)
    cv2.imshow("live", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
