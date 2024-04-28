from pyspark.sql.functions import input_file_name, col
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Write to Redshift") \
    .config("spark.hadoop.fs.s3a.access.key", "<ACCESS-KEY>") \
    .config("spark.hadoop.fs.s3a.secret.key", "<ACCESS-SECRET-KEY>") \
    .config("spark.redshift.logLevel", "DEBUG") \
    .getOrCreate()

parquet_path = "s3://jlr-data/curated/*/*.parquet"
original_path='s3://jlr-data/curated/'
df = spark.read.parquet(parquet_path)

#Exatrcting table names from file path
table_names = df.select(input_file_name().alias("file_path")) \
                 .rdd.map(lambda row: row.file_path.split("/")[-2]) \
                 .distinct() \
                 .collect()
                 
print(table_names)

# Write data to Redshift for each table
redshift_mode = "overwrite" 
temp_dir = "s3://jlr-data/temp/"

redshift_url = "jdbc:redshift://<reshift-endpoint>/<database>?user=<username>&password=<password>"

for table_name in table_names:
    # Read Parquet files for the current table
    parquet_table_path = f"{original_path}{table_name}/"
    table_df = spark.read.parquet(parquet_table_path)

    # Convert column names to snake case with all letters in lowercase
    cols = table_df.columns
    new_cols = [col.replace(" ", "_").replace("-", "_").lower() for col in cols]
    renamed_df = table_df.toDF(*new_cols)

    # Write the data to Redshift
    renamed_df.write \
        .format("io.github.spark_redshift_community.spark.redshift") \
        .option("forward_spark_s3_credentials", "true") \
        .option("url", redshift_url) \
        .option("dbtable", table_name.lower()) \
        .option("tempdir", temp_dir) \
        .mode(redshift_mode) \
        .save()

    print(f"Data written to Redshift table: {table_name.lower()}")
print(f"Data written to Redshift tables")