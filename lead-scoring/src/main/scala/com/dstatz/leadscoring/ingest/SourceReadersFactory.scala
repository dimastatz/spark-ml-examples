package com.dstatz.leadscoring.ingest

import org.apache.spark.sql._

object SourceReadersFactory {
  def getSourceReader(session: SparkSession): SourceReader = ???
}
