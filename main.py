from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("My PySpark App") \
    .getOrCreate()

# Read a CSV file
transactions_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("ecommerce_transactions.csv")

# Display the first few rows of the DataFrame
transactions_df.show()


