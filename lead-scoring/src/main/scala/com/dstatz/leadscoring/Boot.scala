package com.dstatz.leadscoring

import org.apache.log4j.LogManager
import org.apache.spark.sql.SparkSession

object Boot {
  private lazy val log = LogManager.getLogger(Boot.getClass)
  def main(args: Array[String]): Unit = {
    println("lead-scoring is started")
    log.info("creating spark session")
    val session = SparkSession.builder.getOrCreate()
  }
}
