import boto3
import pymysql
import os

def export_mysql_data_to_csv(connection_params, query):
    try:
        conn = pymysql.connect(**connection_params)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print(f"Error exporting data from MySQL: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def upload_to_s3(data, bucket_name, object_key):
    try:
        s3 = boto3.client('s3')
        csv_content = '\n'.join([','.join(map(str, row)) for row in data])
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=csv_content)

        print(f"Data uploaded to S3/{object_key}")
    except Exception as e:
        print(f"Error uploading data to S3: {e}")

def lambda_handler(event, context):
    connection_params = {
        'host': '<host-name>',
        'user': '<user-name>',
        'password': '<password>',
        'database': '<database>',
        'port': 3306
    }

    bucket_name = 'jlr-data'

    tables = {x[0]:f'SELECT * FROM {x[0]}' for x in  export_mysql_data_to_csv(connection_params,'SHOW TABLES;')}

    for table_name, query in tables.items():
        object_key = f"raw/{table_name}.csv"

        data = export_mysql_data_to_csv(connection_params, query)

        if data:
            upload_to_s3(data, bucket_name, object_key)
        else:
           print(f"No data fetched from MySQL for table {table_name}. Skipping.")

    return {
        'statusCode': 200,
        'body': 'All data exported and uploaded to S3 successfully!'
    }