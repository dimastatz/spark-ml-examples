package com.dstatz.leadscoring

import org.apache.log4j.LogManager
import com.dstatz.leadscoring.common._
import com.typesafe.config.ConfigFactory

object Boot {
  private lazy val log = LogManager.getLogger(Boot.getClass)
  def main(args: Array[String]): Unit = {
    import com.dstatz.leadscoring.scoring.Scorer._
    import com.dstatz.leadscoring.training.Trainer._
    import com.dstatz.leadscoring.processing.Processor._
    import com.dstatz.leadscoring.reporting.Reporter._

    log.info("starting spark app")

    val conf = ConfigFactory.load()
    val factory = new AppFactory(conf)

    import factory._
    getSourceReader.readLeads
      .process()
      .trainIfRequired()
      .score()
      .reportResults()
  }
}
