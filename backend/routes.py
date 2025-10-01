from flask import request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from backend.app import app, db
from backend.models import User, SystemFile, CustomFile
import os

ALLOWED_EXTENSIONS = {'pdf'}
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_image_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Could not verify'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@app.route('/system-files', defaults={'parent_id': None})
@app.route('/system-files/<int:parent_id>')
@jwt_required()
def get_system_files(parent_id):
    files = SystemFile.query.filter_by(parent_id=parent_id).all()
    return jsonify([{'id': file.id, 'name': file.name, 'is_folder': file.is_folder} for file in files])

@app.route('/system-files', methods=['POST'])
@jwt_required()
def create_system_file():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403

    data = request.get_json()
    new_file = SystemFile(
        name=data['name'],
        is_folder=data['is_folder'],
        path=os.path.join(app.config['UPLOAD_FOLDER'], 'system', data['name']),
        parent_id=data.get('parent_id')
    )
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'System file created!'})

@app.route('/system-files/<int:file_id>', methods=['PUT'])
@jwt_required()
def rename_system_file(file_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403

    file = SystemFile.query.filter_by(id=file_id).first_or_404()
    data = request.get_json()
    file.name = data['name']
    db.session.commit()
    return jsonify({'message': 'System file renamed!'})

@app.route('/system-files/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_system_file(file_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403

    file = SystemFile.query.filter_by(id=file_id).first_or_404()
    db.session.delete(file)
    db.session.commit()
    return jsonify({'message': 'System file deleted!'})

@app.route('/custom-files', defaults={'parent_id': None})
@app.route('/custom-files/<int:parent_id>')
@jwt_required()
def get_custom_files(parent_id):
    user_id = get_jwt_identity()
    files = CustomFile.query.filter_by(user_id=user_id, parent_id=parent_id).all()
    return jsonify([{'id': file.id, 'name': file.name, 'is_folder': file.is_folder} for file in files])

@app.route('/custom-files', methods=['POST'])
@jwt_required()
def create_custom_file():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_file = CustomFile(
        name=data['name'],
        is_folder=data['is_folder'],
        path=os.path.join(app.config['UPLOAD_FOLDER'], 'custom', str(user_id), data['name']),
        user_id=user_id,
        parent_id=data.get('parent_id')
    )
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'File created!'})

@app.route('/custom-files/<int:file_id>', methods=['PUT'])
@jwt_required()
def rename_custom_file(file_id):
    user_id = get_jwt_identity()
    file = CustomFile.query.filter_by(id=file_id, user_id=user_id).first_or_404()
    data = request.get_json()
    file.name = data['name']
    db.session.commit()
    return jsonify({'message': 'File renamed!'})

@app.route('/custom-files/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_custom_file(file_id):
    user_id = get_jwt_identity()
    file = CustomFile.query.filter_by(id=file_id, user_id=user_id).first_or_404()
    db.session.delete(file)
    db.session.commit()
    return jsonify({'message': 'File deleted!'})

@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    user_id = get_jwt_identity()
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Create a directory for the user if it doesn't exist
        user_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'custom', str(user_id))
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        file.save(os.path.join(user_dir, filename))
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'message': 'File type not allowed'}), 400

@app.route('/uploads/<path:filename>')
@jwt_required()
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({'username': user.username})

@app.route('/profile/picture', methods=['POST'])
@jwt_required()
def upload_profile_picture():
    user_id = get_jwt_identity()
    if 'profile_picture' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['profile_picture']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_image_file(file.filename):
        filename = secure_filename(file.filename)
        user_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'profile_pictures', str(user_id))
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        file.save(os.path.join(user_dir, filename))
        # Update user model with profile picture path
        return jsonify({'message': 'Profile picture uploaded successfully'})
    else:
        return jsonify({'message': 'Image file type not allowed'}), 400

@app.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json()
    if user.check_password(data['old_password']):
        user.set_password(data['new_password'])
        db.session.commit()
        return jsonify({'message': 'Password changed successfully'})
    else:
        return jsonify({'message': 'Incorrect old password'}), 401

@app.route('/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username, 'is_admin': u.is_admin} for u in users])

@app.route('/admin/users/<int:user_id>/custom-files', methods=['GET'])
@jwt_required()
def get_user_custom_files(user_id):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403
    files = CustomFile.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': file.id, 'name': file.name, 'is_folder': file.is_folder} for file in files])

@app.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({'username': user.username})

@app.route('/profile/picture', methods=['POST'])
@jwt_required()
def upload_profile_picture():
    user_id = get_jwt_identity()
    if 'profile_picture' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['profile_picture']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_image_file(file.filename):
        filename = secure_filename(file.filename)
        user_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'profile_pictures', str(user_id))
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        file.save(os.path.join(user_dir, filename))
        # Update user model with profile picture path
        return jsonify({'message': 'Profile picture uploaded successfully'})
    else:
        return jsonify({'message': 'Image file type not allowed'}), 400

@app.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    data = request.get_json()
    if user.check_password(data['old_password']):
        user.set_password(data['new_password'])
        db.session.commit()
        return jsonify({'message': 'Password changed successfully'})
    else:
        return jsonify({'message': 'Incorrect old password'}), 401
