from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


def load_list_to_df() -> DataFrame:
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

    return spark.createDataFrame(data, schema)


if __name__ == "__main__":
    load_list_to_df().show()
