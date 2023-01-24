from flask import Flask,request, jsonify
from utils.image_validator import visual_validate_image
import base64
# !pip install flask flask-restful

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!";


@app.route('/visual-validate/', methods=['POST'])
def upload_file_for_visual_validation():
    print('request')
    print(request.files['file'])
    file = request.files['file']
    image_string = base64.b64encode(file.read())
    # fileStream = request.get_data()
    # print(fileStream.)
    tag = request.form['tag']
    project = request.form['project']
    branch_name = request.form['branchName']
    test_matrix_id = request.form['testMatrixId']

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        download_url = visual_validate_image(image_string, tag, project, branch_name, test_matrix_id)
        return jsonify({'message': 'File uploaded successfully', 'downloadURL': download_url})
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run()
