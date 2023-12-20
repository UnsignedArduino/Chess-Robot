import cv2

from cv.configuration import (
    CHESSBOARD_BORDER,
    CHESSBOARD_END,
    CHESSBOARD_SQUARE,
    CHESSBOARD_START,
)
from cv.types import CV2NumpyImage


def chessboard_cv_draw_square_lines(image: CV2NumpyImage) -> CV2NumpyImage:
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

    return image
