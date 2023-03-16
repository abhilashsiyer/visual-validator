import uuid

import cv2
import imutils
from skimage import io
from skimage import metrics
import base64

from image_kit.file_uploader import upload_image
from multiprocessing import Process


def validate_image(file_url_as_base, file_url_for_compare, status_bar_height, display_height, display_width,
                   file_tag, project, branch_name, test_case_name, device_model, test_matrix_id):
    # load the two input images
    imageA = url_to_image(file_url_as_base)
    imageB = url_to_image(file_url_for_compare)

    print("Values dimensions", status_bar_height, display_height, display_width)

    croppedImageA = imageA[int(status_bar_height):int(display_height), 0:int(display_width)]
    croppedImageB = imageB[int(status_bar_height):int(display_height), 0:int(display_width)]

    # Match size of both images
    # Get height and width of imageA

    # convert the images to grayscale
    grayA = cv2.cvtColor(croppedImageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(croppedImageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = metrics.structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    print("Diff value ", diff)

    if score >= 1.0:  # change to 1.0
        return {"message": "Validation successful with base", "validationResult": "Success"}
    else:

        p = Process(target=upload_diff_result, args=(diff, croppedImageB, "result-" + file_tag, project, branch_name,
                                                     test_case_name, device_model, test_matrix_id))
        p.start()
        return {"message": "Validation failed with base", "validationResult": "Failed"}


def url_to_image(url):
    image = io.imread(url)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image_bgr


def upload_diff_result(diff, croppedImageB, file_tag, project, branch_name, test_case_name, device_model, test_matrix_id):
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(croppedImageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    retval, buffer = cv2.imencode('.png', croppedImageB)
    print('retval', retval)
    png_as_b64 = base64.b64encode(buffer)

    upload_image(png_as_b64, file_tag, project, branch_name, test_case_name, device_model,
                                test_matrix_id)
