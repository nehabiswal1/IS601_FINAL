# config/minio_client.py
import os
from minio import Minio

MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', 'localhost:9001')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'DD3MzAVNo1kEZCLAfvTV')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'tVONit3oJKSFWc3zBaw8qryHKyK8mF39OwLVgMiw')

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False  # Set to True if using HTTPS
)

bucket_name = 'profile-picture'

# Ensure bucket exists
found = minio_client.bucket_exists(bucket_name)
if not found:
    minio_client.make_bucket(bucket_name)
