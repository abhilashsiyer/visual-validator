from image_kit.delete_file import delete_file
from image_kit.file_uploader import upload_image
from image_kit.retrieve_file import get_file_url, delete_compare_file_if_existing, get_file_id, get_file_ui_for_testcase
from image_kit.update_tags import add_tag, remove_tag
from opencv_image.image_compare import validate_image


# Requirements to handle
# Delete previous to_compare file
# On failure give


def visual_validate_image(file, base_file_url, file_tag, project, branch_name, test_matrix_id, test_case_name,
                          device_model):
    base_url_exists: bool = False

    print("start validation")

    if "https://ik.imagekit.io" in base_file_url:
        base_url_exists = True

    if "Failed" in base_file_url:
        base_url_exists = False

    if base_url_exists:

        base_branch_url_exists: bool = False

        image_to_compare_url = upload_image(file, "to_compare-" + file_tag, "project-" + project,
                                            "branch-" + branch_name, "testCaseName-" + test_case_name,
                                            "deviceModel-" + device_model, "testMatrixId-" + test_matrix_id)
        # get_file_url("base-" + file_tag, "project-" + project, "branch-" + branch_name,
        #              "testCaseName-" + test_case_name)
        base_branch_file_url = "Blah"
        print("image upload completed")

        # if "https://ik.imagekit.io" in base_branch_file_url:
        #     base_branch_url_exists = True
        #
        # if "Failed" in base_branch_file_url:
        #     base_branch_url_exists = False

        print("baseBranchURl", base_branch_file_url)

        response = validate_image(base_file_url, image_to_compare_url)

        print('validation completed')

        return response

        # if base_branch_url_exists:
        #     response = validate_image(base_branch_file_url, image_to_compare_url)
        #     return response
        # else:
        #
        #     return response
    else:
        upload_image(file, "base-" + file_tag, "project-" + project, "branch-main", "testCaseName-"
                     + test_case_name, "deviceModel-" + device_model)
        return {"message": "File uploaded as base", "validationResult": "Success"}


def get_base_file_url(file_tag, project, test_case_name, device_model, branch):
    base_file_url = get_file_url("base-" + file_tag, "project-" + project, "branch-" + branch,
                                 "testCaseName-" + test_case_name, "deviceModel-" + device_model)
    return base_file_url


# Used in UI
def get_file_urls_for_testcase( project, test_case_name, device_model, test_matrix_id):
    base_file_url = get_file_ui_for_testcase("project-" + project,
                                 "testCaseName-" + test_case_name, "deviceModel-" + device_model,
                                "testMatrixId-" + test_matrix_id)
    return base_file_url


def delete_to_compare_file(file_tag, project, branch_name, test_matrix_id, test_case_name):
    return delete_compare_file_if_existing("to_compare-" + file_tag, "project-" + project, "branch-" + branch_name,
                                           "testCaseName-" + test_case_name, "testMatrixId-" + test_matrix_id)


def upload_base_branch_file(file, file_tag, project, branch_name, test_case_name):
    url = upload_image(file, "base-" + file_tag, "project-" + project, "branch-" + branch_name, "testCaseName-"
                       + test_case_name)
    return {'message': 'File uploaded as branch base', "base_image_url": url}


def update_main_with_base_branch(file_tag, project, test_case_name, branch_name):
    branch_file_id = get_file_id("base-" + file_tag, "project-" + project, "branch-" + branch_name,
                                 "testCaseName-" + test_case_name)
    base_file_id = get_file_id("base-" + file_tag, "project-" + project, "branch-main",
                               "testCaseName-" + test_case_name)

    remove_tag(file_ids=[base_file_id], tags=["branch-main"])
    add_tag(file_ids=[branch_file_id], tags=['branch-main'])
    remove_tag(file_ids=[branch_file_id], tags=["branch-" + branch_name])
    # Use a ext DB to wait until this change is completed
    delete_file(base_file_id)

    return {"message": "Updated main img with branch image"}
