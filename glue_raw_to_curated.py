import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
import boto3

sc = SparkContext()
glueContext = GlueContext(sc)

spark = glueContext.spark_session
glue_client = boto3.client('glue')

response = glue_client.get_tables(DatabaseName='jlr')
tables = response['TableList']

for table in tables:
    table_name = table['Name']
    dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
        database = "jlr",
        table_name = table_name
    )
    data_frame = dynamic_frame.toDF()
    paquet_file_name=table_name.split('_')[0][3:]
    target_path = f"s3://jlr-data/curated/{paquet_file_name}"
    data_frame.write.parquet(target_path, mode="overwrite", compression="uncompressed")

# Stop SparkContext
sc.stop()