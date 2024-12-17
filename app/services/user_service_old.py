# routes/users.py
import os
from flask import Blueprint, request, jsonify, g
from werkzeug.utils import secure_filename
from config.minio_client import minio_client, bucket_name, MINIO_ENDPOINT
from models import db, User
from auth import login_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/<int:user_id>/profile-picture', methods=['POST'])
@login_required
def upload_profile_picture(user_id):
    if g.user.id != user_id:
        return jsonify({'error': 'Not authorized to update this profile'}), 403
    
    if 'profilePicture' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['profilePicture']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate image (optional)
    # Example: Ensure MIME type is allowed
    allowed_types = ['image/jpeg', 'image/png']
    if file.content_type not in allowed_types:
        return jsonify({'error': 'Invalid image format. Allowed: JPEG, PNG'}), 400
    
    filename = secure_filename(file.filename)
    file_ext = filename.rsplit('.', 1)[-1].lower()
    object_name = f"profile_{user_id}.{file_ext}"

    # Optional: Resize or process the image with Pillow if desired
    # from PIL import Image
    # image = Image.open(file)
    # image = image.resize((300, 300))
    # image_bytes = io.BytesIO()
    # image.save(image_bytes, format='JPEG')
    # image_bytes.seek(0)
    # minio_client.put_object(bucket_name, object_name, image_bytes, length=len(image_bytes.getvalue()), content_type='image/jpeg')

    # If not resizing, upload directly
    # To upload directly from file, we must read it as bytes:
    file.seek(0, os.SEEK_END)
    file_length = file.tell()
    file.seek(0)
    
    minio_client.put_object(
        bucket_name=bucket_name, 
        object_name=object_name, 
        data=file, 
        length=file_length, 
        content_type=file.content_type
    )

    # Construct the file URL. Assuming you can access the files at MINIO_PUBLIC_ENDPOINT
    MINIO_PUBLIC_ENDPOINT = os.getenv('MINIO_PUBLIC_ENDPOINT', f"http://{MINIO_ENDPOINT}")
    file_url = f"{MINIO_PUBLIC_ENDPOINT}/{bucket_name}/{object_name}"

    # Update user record
    g.user.profile_picture_url = file_url
    db.session.commit()

    return jsonify({'message': 'Profile picture uploaded successfully', 'profilePictureUrl': file_url}), 200
