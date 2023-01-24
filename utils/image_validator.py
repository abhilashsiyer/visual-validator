from image_kit.file_uploader import upload_image
from image_kit.retrieve_file import get_file_url, delete_compare_file_if_existing
from opencv_image.image_compare import validate_image


# Requirements to handle
# Delete previous to_compare file
# On failure give


def visual_validate_image(file, file_tag, project, branch_name, test_matrix_id):
    base_file_url = get_file_url("base-" + file_tag, "project-" + project, "branch-" + branch_name)

    if base_file_url:
        delete_compare_file_if_existing("to_compare-" + file_tag, "project-" + project, "branch-" + branch_name,
                                        "testMatrixId-" + test_matrix_id)
        image_to_compare_url = upload_image(file, "to_compare-" + file_tag, "project-" + project,
                                            "branch-" + branch_name,
                                            "testMatrixId-" + test_matrix_id)
        response = validate_image(base_file_url, image_to_compare_url)
        return response
    else:
        url = upload_image(file, "base-" + file_tag, "project-" + project, "branch-" + branch_name)
        return {'message': 'File uploaded as base', "base_image_url": url, "validation_result": True}
