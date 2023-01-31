from flask import Flask, request, jsonify
from utils.image_validator import visual_validate_image, get_base_file_url, delete_to_compare_file, \
    upload_base_branch_file, update_main_with_base_branch
import base64
import json

# !pip install flask flask-restful

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!";


@app.route('/visual-validate/', methods=['POST'])
def upload_file_for_visual_validation():
    file = request.files['file']
    image_string = base64.b64encode(file.read())
    tag = request.form['tag']
    project = request.form['project']
    branch_name = request.form['branchName']
    test_matrix_id = request.form['testMatrixId']
    test_case_name = request.form['testCaseName']
    base_file_url = request.form['baseFileUrl']
    device_model = request.form['deviceModel']

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        validation_resp = visual_validate_image(image_string, base_file_url, tag, project, branch_name, test_matrix_id,
                                                test_case_name, device_model)
        print("validation_resp", validation_resp)
        return validation_resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


@app.route('/upload_base_branch_file/', methods=['POST'])
def upload_a_base_branch_file():
    file = request.files['file']
    image_string = base64.b64encode(file.read())
    tag = request.form['tag']
    project = request.form['project']
    branch_name = request.form['branchName']
    test_case_name = request.form['testCaseName']

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        download_url = upload_base_branch_file(image_string, tag, project, branch_name, test_case_name)
        return jsonify({'message': 'File uploaded successfully', 'downloadURL': download_url})
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


@app.route('/get_base_file_url/', methods=['POST'])
def get_base_file():
    tag = request.form['tag']
    project = request.form['project']
    test_case_name = request.form['testCaseName']
    device_model = request.form['deviceModel']
    branch = request.form['branch']

    base_branch_file_url = get_base_file_url(tag, project, test_case_name, device_model, branch)
    print("base_branch_file_url", base_branch_file_url)

    if "Failed" in base_branch_file_url:
        print("No branch url")
        base_main_file_url = get_base_file_url(tag, project, test_case_name, device_model, "main")
        print("base_main_file_url", base_main_file_url)

        if "Failed" in base_main_file_url:
            print("No base url")
            return jsonify({'baseFileUrl': "Failed"})
        else:
            print("Base main url found")
            return jsonify({'baseFileUrl': base_main_file_url})
    else:
        print("Base branch url found")
        return jsonify({'baseFileUrl': base_branch_file_url})


@app.route('/update_main_with_base_branch/', methods=['POST'])
def update_main_with_base_branch_img():
    tag = request.form['tag']
    project = request.form['project']
    test_case_name = request.form['testCaseName']
    branch_name = request.form['branchName']
    device_model = request.form['deviceModel']

    return update_main_with_base_branch(tag, project, test_case_name, branch_name)


@app.route('/delete_to_compare_file/', methods=['POST'])
def delete_to_compare():
    tag = request.form['tag']
    project = request.form['project']
    test_case_name = request.form['testCaseName']
    branch_name = request.form['branchName']
    test_matrix_id = request.form['testMatrixId']

    return delete_to_compare_file(tag, project, branch_name, test_matrix_id, test_case_name)


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run()
