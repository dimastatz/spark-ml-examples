from pyspark.sql import SparkSession


spark = SparkSession.builder \
        .appName("pyspark-howto-app-1") \
        .config("spark.driver.bindAddress","127.0.0.1") \
        .getOrCreate()