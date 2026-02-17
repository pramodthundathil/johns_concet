import boto3
from botocore.exceptions import ClientError

# Credentials from johns/settings.py
ACCESS_KEY = "AKIAWLVNT2SPSXWZYY5M"
SECRET_KEY = "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"
BUCKET_NAME = 'johnsconcept'
REGION_NAME = 'ap-south-1'

def test_s3_access():
    print(f"Testing access to bucket: {BUCKET_NAME} in {REGION_NAME}")
    
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name=REGION_NAME
        )
        
        # 1. List Buckets (checks if creds are valid generally)
        print("\n1. Listing buckets...")
        try:
            response = s3.list_buckets()
            print("   Success! Buckets found:", [b['Name'] for b in response['Buckets']])
        except ClientError as e:
            print(f"   FAILED: {e}")

        # 2. Check specific bucket existence and permission
        print(f"\n2. Checking specific bucket '{BUCKET_NAME}'...")
        try:
            s3.head_bucket(Bucket=BUCKET_NAME)
            print("   Success! Bucket exists and is accessible.")
        except ClientError as e:
            print(f"   FAILED: {e}")
        
        # 3. Try to list objects in the bucket
        print("\n3. Listing objects in bucket...")
        try:
            objs = s3.list_objects_v2(Bucket=BUCKET_NAME, MaxKeys=5)
            if 'Contents' in objs:
                print(f"   Success! Found {len(objs['Contents'])} objects.")
                for obj in objs['Contents']:
                    print(f"    - {obj['Key']}")
            else:
                print("   Success! Bucket is empty or no objects found.")
        except ClientError as e:
            print(f"   FAILED: {e}")

        # 4. Try to upload a test file
        print("\n4. Uploading test file...")
        test_content = b"This is a test file from the diagnostic script."
        test_key = "test_diagnostic_file.txt"
        try:
            s3.put_object(Bucket=BUCKET_NAME, Key=test_key, Body=test_content)
            print(f"   Success! Uploaded {test_key}.")
        except ClientError as e:
            print(f"   FAILED: {e}")
        
        # 5. Try to download/get the test file (Check GetObject permission)
        print("\n5. Getting test file (GetObject permission)...")
        try:
            response = s3.get_object(Bucket=BUCKET_NAME, Key=test_key)
            print(f"   Success! Read file content: {response['Body'].read().decode('utf-8')[:20]}...")
        except ClientError as e:
            print(f"   FAILED: {e}")

        # 6. Check if file is publicly accessible via URL
        print("\n6. Checking public URL access...")
        import urllib.request
        public_url = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{test_key}"
        print(f"   URL: {public_url}")
        try:
            with urllib.request.urlopen(public_url) as response:
                 print(f"   Success! Public URL is accessible. Status: {response.status}")
        except Exception as e:
            print(f"   FAILED to access public URL: {e}")

        # 7. Try to delete the test file
        print("\n7. Deleting test file...")
        try:
            s3.delete_object(Bucket=BUCKET_NAME, Key=test_key)
            print("   Success! Deleted test file.")
        except ClientError as e:
            print(f"   FAILED: {e}")

    except Exception as e:
        print(f"\nUNEXPECTED FATAL ERROR: {e}")
    except Exception as e:
        print(f"\nUNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    test_s3_access()
