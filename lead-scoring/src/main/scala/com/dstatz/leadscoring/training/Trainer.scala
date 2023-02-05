package com.dstatz.leadscoring.training

import org.apache.spark.sql._

object Trainer {
  implicit class ModelTrainer(df: DataFrame) {
    def trainIfRequired(): DataFrame = ???
  }
}
