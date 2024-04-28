# JLR_AWS_DataEngineering_Project

This project implements an end-to-end data pipeline on AWS for extracting, transforming, and loading data from a MySQL database into Amazon Redshift for analysis and querying.

## Architecture Overview

The data pipeline consists of the following components:

- **MySQL Database**: The source database containing the original data.
- **AWS Lambda Function**: Extracts data from the MySQL database and loads it into an S3 bucket as raw data files.
- **Amazon S3 (Raw Data)**: Stores the raw data files extracted by the Lambda function.
- **AWS Glue Crawler**: Scans the raw data in S3, infers the schema, and creates metadata tables in the Glue Data Catalog.
- **Glue Data Catalog (Raw)**: Contains metadata tables representing the structure of the raw data stored in S3.
- **AWS Glue Job (ETL)**: Reads data from the raw data tables in the Glue Data Catalog, performs transformations, and saves curated data in Parquet format back to S3.
- **S3 (Curated Data in Parquet Format)**: Stores the curated data in Parquet format for optimized querying and analysis.
- **AWS Glue Job (ETL to Redshift)**: Reads curated data from S3, applies further transformations if needed, and loads it into Amazon Redshift.
- **Amazon Redshift**: Final destination for curated data, allowing for scalable data warehousing, analysis, and querying.

## Setup Instructions

To set up and run the data pipeline:

1. **Configure MySQL Database**: Ensure that your MySQL database is accessible from AWS and contains the required data.

2. **Set up Lambda Function**: Implement a Lambda function to extract data from MySQL and load it into an S3 bucket. Configure appropriate IAM roles and permissions for Lambda.

3. **Create Glue Crawler**: Configure an AWS Glue crawler to scan the raw data in S3, infer the schema, and create metadata tables in the Glue Data Catalog.

4. **Run Glue Job (ETL)**: Create an AWS Glue job to read data from the raw data tables in the Glue Data Catalog, perform transformations, and save curated data in Parquet format back to S3.

5. **Set up Redshift Cluster**: Provision an Amazon Redshift cluster for storing curated data. Define the necessary schemas and tables.

6. **Create Glue Job (ETL to Redshift)**: Develop another AWS Glue job to read curated data from S3, apply further transformations if needed, and load it into Amazon Redshift.

7. **Execute the Pipeline**: Run the Glue jobs to execute the data pipeline. Monitor the execution and troubleshoot any issues as needed.

## Usage

Once the data pipeline is set up and running:

- Use Amazon Redshift for querying and analyzing curated data stored in the data warehouse.
- Monitor pipeline execution and performance using AWS CloudWatch and AWS Glue console.
- Modify and iterate on the pipeline as needed to accommodate changes in data sources or business requirements.

