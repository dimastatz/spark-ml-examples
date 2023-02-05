package com.dstatz.leadscoring.reporting

import org.apache.spark.sql._
import com.typesafe.config.Config

object Reporter {
  implicit class Reporting(df: DataFrame)(implicit
      session: SparkSession,
      conf: Config
  ) {
    def reportResults(): Unit = ???
  }
}
