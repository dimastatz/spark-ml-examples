from pyspark.sql import SparkSession, DataFrame


def create_session(name='pyspark-example', host='127.0.0.1') -> SparkSession:
    return SparkSession.builder \
        .appName(name) \
        .config('spark.driver.bindAddress', host) \
        .getOrCreate()
    

def crunch(spark: SparkSession) -> DataFrame:
    return None

