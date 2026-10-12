# S3 (Simple Storage Service) connectivity
# Read the data from S3 and write the data to S3


import pandas as pd
import boto3
from io import StringIO

# Initiate a session with s3
s3 = boto3.client('s3')

def read_file_from_s3(bucket_name,file_key):
# fetch the csv file from s3
    response = s3.get_object(Bucket = bucket_name,Key = file_key)
    print("response is :",response)
    csv_content = response['Body'].read().decode('utf-8')
    data = StringIO(csv_content)
    df = pd.read_csv(data)
    print("Data frame: ",df)
    return df

def write_file_to_s3(df,bucket_name,file_key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False)
    s3.put_object(Bucket = bucket_name,Key = file_key,Body=csv_buffer.getvalue())


ans_df = read_file_from_s3("bucket-rw-aug2026","movies_data/netflix_dataset.csv")
print(ans_df.head(5))

df_to_write = ans_df[['show_id','type','description','title']]

write_file_to_s3(df_to_write,"bucket-rw-aug2026","movies_data/movie_output.csv")












