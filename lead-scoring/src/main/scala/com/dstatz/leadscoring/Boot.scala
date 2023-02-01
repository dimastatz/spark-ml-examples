package com.dstatz.leadscoring

import org.apache.log4j.LogManager
import com.dstatz.leadscoring.common._
import com.dstatz.leadscoring.ingest.SourceReadersFactory

object Boot {
  private lazy val log = LogManager.getLogger(Boot.getClass)
  def main(args: Array[String]): Unit = {
    println("lead-scoring is started")
    log.info("creating spark session")
    val session = SessionFactory.getSparkSession()
    val sourceReader = SourceReadersFactory.getSourceReader(session)

    sourceReader.readLeads.collect()
    session.close()
  }
}
