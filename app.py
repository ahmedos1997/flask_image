from flask import Flask, jsonify, request, send_from_directory
from actions import bp as actionbp
from filters import bp as filterbp
from android import bp as androidbp
from helpers import allowed_extension, get_secure_filename_filepath

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = ['png','jpg','jpeg']

app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

app.register_blueprint(actionbp)
app.register_blueprint(filterbp)
app.register_blueprint(androidbp)


@app.route('/images', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file was seleted'}), 400
        
        file = request.files['file']

        if file.filename == '':
            return jsonify({'error' : 'No file was selected'}), 400
        
        if not allowed_extension(file.filename):
            return jsonify({'error': 'the extension in not supported.'}), 400
        
        filename , filepath = get_secure_filename_filepath(file.filename)
        file.save(filepath)
        return jsonify({
            'message': 'file successfuly uploaded',
            'filename': filename
        }), 201
    return jsonify('nice')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)