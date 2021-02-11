# AWS S3 Uploader

Simple script for uploading to an s3 bucket

## Quickstart
1. Put your secret access key and access key id into `/secrets` as `.key` files
2. Update `.env` target file to the relative path to your target file and target bucket.
    ```bash
    export TARGET_FILE=""
    export BUCKET=""
    ```
3. Run the upload script
    ```bash
    ./s3.sh
    ```