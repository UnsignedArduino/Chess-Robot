from cv.configuration import (
    CHESSBOARD_SQUARE,
    CHESSBOARD_SQUARE_BORDER,
    CHESSBOARD_START,
)
from cv.types import CV2NumpyImage


def chessboard_cv_crop_image_x_y_width_height(
    image: CV2NumpyImage, x: int, y: int, width: int, height: int
) -> CV2NumpyImage:
    return image[y : y + height, x : x + width]


def chessboard_cv_crop_image_x1_y1_x2_y2(
    image: CV2NumpyImage, x1: int, y1: int, x2: int, y2: int
) -> CV2NumpyImage:
    return image[y1:y2, x1:x2]


def chessboard_cv_split_into_squares(image: CV2NumpyImage) -> list[CV2NumpyImage]:
    result = []

    for y in range(7, 0, -1):
        for x in range(0, 7):
            result.append(
                chessboard_cv_crop_image_x_y_width_height(
                    image,
                    CHESSBOARD_START + x * CHESSBOARD_SQUARE - CHESSBOARD_SQUARE_BORDER,
                    CHESSBOARD_START + y * CHESSBOARD_SQUARE - CHESSBOARD_SQUARE_BORDER,
                    CHESSBOARD_SQUARE + CHESSBOARD_SQUARE_BORDER * 2,
                    CHESSBOARD_SQUARE + CHESSBOARD_SQUARE_BORDER * 2,
                )
            )

    return result
