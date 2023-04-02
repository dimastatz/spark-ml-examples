package com.dstatz.leadscoring.tests

import com.typesafe.config._
import org.apache.spark.sql.SparkSession

object TestHelpers {
  org.slf4j.LoggerFactory
    .getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME)
    .asInstanceOf[ch.qos.logback.classic.Logger]
    .setLevel(ch.qos.logback.classic.Level.WARN)

  def getConfig: Config = {
    ConfigFactory.load("test.conf")
  }

  def getSparkSession: SparkSession = {
    SparkSession
      .builder()
      .master("local[1]")
      .appName("spark-template")
      .config("spark.driver.bindAddress", "127.0.0.1")
      .getOrCreate()
  }
}
