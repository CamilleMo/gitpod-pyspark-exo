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

# Count the total number of transactions in the dataset.

# Calculate the sum of total_amount for all transactions.
print("sum of total amount :")

# Find the average total_amount per transaction.
print("avg of total amount :")

# Find the total_amount spent by each customer.
print("Total amount by customer :")

# Count the number of transactions for each product.
print("count of transactions by products")

# Calculate the daily total revenue.
print("daily total revenue")

# Find the customer who spent the most money.
print("customer by spending")


# Join the transactions DataFrame with the customers and products DataFrames.



# Calculate the total revenue per product category.

# Find the most popular product in each category based on the number of transactions.

# Identify the top 3 customers with the highest spending in each category.

# Calculate the age distribution of customers who made transactions.
