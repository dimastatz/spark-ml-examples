package com.dstatz.leadscoring.common

import org.apache.spark.sql.SparkSession

object SessionFactory {
  def getSparkSession(): SparkSession = {
    SparkSession
      .builder()
      .master("local[1]")
      .appName("lead-score-example")
      .config("spark.driver.bindAddress", "127.0.0.1")
      .getOrCreate()
  }
}
