package com.dstatz.leadscoring.reporting

import org.apache.spark.sql._

object Reporter {
  implicit class Reporting(df: DataFrame) {
    def reportResults(): Unit = ???
  }
}
