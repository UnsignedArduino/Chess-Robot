import logging
from time import sleep

import cv2
# noinspection PyUnresolvedReferences
from libcamera import Transform
# noinspection PyUnresolvedReferences
from picamera2 import Picamera2

from utils.logger import create_logger

logger = create_logger(name=__name__, level=logging.DEBUG)

IMAGE_SIZE = 640
CHESSBOARD_BORDER = 46
CHESSBOARD_START = CHESSBOARD_BORDER
CHESSBOARD_END = IMAGE_SIZE - CHESSBOARD_BORDER
CHESSBOARD_SQUARE = round((IMAGE_SIZE - CHESSBOARD_BORDER * 2) / 8)

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

    LINE_COLOR = (0, 0, 255)
    LINE_WIDTH = 2

    image = cv2.rectangle(
        image,
        (CHESSBOARD_BORDER, CHESSBOARD_BORDER),
        (CHESSBOARD_END, CHESSBOARD_END),
        LINE_COLOR,
        LINE_WIDTH,
    )

    for y in range(0, 8):
        image = cv2.line(
            image,
            (CHESSBOARD_START, CHESSBOARD_START + y * CHESSBOARD_SQUARE),
            (CHESSBOARD_END, CHESSBOARD_START + y * CHESSBOARD_SQUARE),
            LINE_COLOR,
            LINE_WIDTH,
        )
    for x in range(0, 8):
        image = cv2.line(
            image,
            (CHESSBOARD_START + x * CHESSBOARD_SQUARE, CHESSBOARD_START),
            (CHESSBOARD_START + x * CHESSBOARD_SQUARE, CHESSBOARD_END),
            LINE_COLOR,
            LINE_WIDTH,
        )

    cv2.imshow("live", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
