package com.dstatz.leadscoring.common

import org.apache.spark.sql.SparkSession

object SessionFactory {
  def getSparkSession(): SparkSession = {
    SparkSession.builder.getOrCreate()
  }
}
