package com.dstatz.leadscoring.scoring

import org.apache.spark.sql._

object Scorer {
  implicit class LeadScoring(df: DataFrame) {
    def score(): DataFrame = ???
  }
}
