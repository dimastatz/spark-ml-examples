from mongoengine import Document
from pyspark.sql import SparkSession, DataFrame


def to_spark_dataframe(spark: SparkSession, doc: Document, exclude: list) -> DataFrame:
    rows = doc.objects().as_pymongo()
    lst = [dict([(k, v) for k, v in d.items() if not k in exclude]) for d in rows]
    return spark.createDataFrame(lst)


def create_session(name='pyspark-example', host='127.0.0.1') -> SparkSession:
    return SparkSession.builder \
        .appName(name) \
        .config('spark.driver.bindAddress', host) \
        .getOrCreate()
    

def crunch(spark: SparkSession) -> DataFrame:
    return None

