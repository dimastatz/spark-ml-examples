package com.dstatz.leadscoring.common

import com.typesafe.config.Config
import org.apache.spark.sql.SparkSession
import com.dstatz.leadscoring.ingest.SourceReader

class AppFactory(conf: Config) {
  def getSparkSession: SparkSession = {
    SparkSession
      .builder()
      .master("local[1]")
      .appName("lead-score-example")
      .config("spark.driver.bindAddress", "127.0.0.1")
      .getOrCreate()
  }

  def getSourceReader: SourceReader = ???
}
