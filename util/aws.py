import os
import boto3

def enviar_parquet_s3(parquet_buffer, datenow, access_key, secret_key, session_token): 
    # Upload Parquet file to S3
#    os.environ['AWS_ACCESS_KEY_ID'] = access_key
#    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_key
#    os.environ['AWS_SESSION_TOKEN'] = session_token

#    session = boto3.Session(
#        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
#        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
#        aws_session_token=os.environ["AWS_SESSION_TOKEN"],
#   )

#    s3_client = session.client('s3')
    s3_client = boto3.client('s3')

    bucket_name = 'fiap-bucket-s3'
    s3_file_name = 'raw/b3_{}.parquet'.format(datenow)

    s3_client.upload_fileobj(parquet_buffer, bucket_name, s3_file_name)

    print(f"File successfully uploaded to S3://{bucket_name}/{s3_file_name}")