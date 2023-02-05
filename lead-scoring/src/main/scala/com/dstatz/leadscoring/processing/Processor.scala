package com.dstatz.leadscoring.processing

import org.apache.spark.sql._
import com.dstatz.leadscoring.common._

object Processor {
  implicit class LeadsProcessor(leads: Dataset[Lead]) {
    def process(): DataFrame = ???
  }
}
