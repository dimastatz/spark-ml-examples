from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


spark = SparkSession.builder \
    .appName("pyspark-howto-app-1") \
    .config("spark.driver.bindAddress","127.0.0.1") \
    .getOrCreate()

data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Define the schema for the DataFrame
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create the DataFrame from the list and the schema
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()

