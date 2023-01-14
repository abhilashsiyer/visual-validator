from aioflask import Flask, request, jsonify
from utils.image_validator import visual_validate_image
import asyncio
app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/visual-validate', methods=['POST'])
async def upload_file_for_visual_validation():
    file = request.files['file']
    file_tag = request.form['tag']

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        download_url = await visual_validate_image(file, file_tag)
        return jsonify({'message': 'File uploaded successfully', 'downloadURL': download_url})
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
