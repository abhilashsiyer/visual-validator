from image_kit.file_uploader import upload_image
from image_kit.retrieve_file import get_file_url
from opencv_image.image_compare import validate_image


def visual_validate_image(file, file_tag):
    existing_file_url = get_file_url(file_tag)
    if existing_file_url:
        image_to_compare_url = upload_image(file, "to_compare_" + file_tag)
        response = validate_image(existing_file_url, image_to_compare_url)
        return response
    else:
        url = upload_image(file, file_tag)
        return {'message': 'File uploaded as base', "base_image_url": url, "validation_result": True}
