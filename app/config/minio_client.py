# config/minio_client.py
import os
from minio import Minio

MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', 'minio:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'DD3MzAVNo1kEZCLAfvTV')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'tVONit3oJKSFWc3zBaw8qryHKyK8mF39OwLVgMiw')
MINIO_PUBLIC_ENDPOINT = os.getenv('MINIO_PUBLIC_ENDPOINT','minio:9001')
MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME','profile-picture')

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False  # Set to True if using HTTPS
)

# MINIO_ENDPOINT= localhost:9000 #/api/v1/service-account-credentials
# MINIO_ACCESS_KEY= DD3MzAVNo1kEZCLAfvTV
# MINIO_SECRET_KEY= tVONit3oJKSFWc3zBaw8qryHKyK8mF39OwLVgMiw
# MINIO_BUCKET_NAME=profile-picture
# MINIO_PUBLIC_ENDPOINT=localhost:9001

bucket_name = 'profile-picture'

# Ensure bucket exists
found = minio_client.bucket_exists(bucket_name)
if not found:
    minio_client.make_bucket(bucket_name)
