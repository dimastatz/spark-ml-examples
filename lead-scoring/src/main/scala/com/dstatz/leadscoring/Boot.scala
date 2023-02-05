package com.dstatz.leadscoring

import com.typesafe.config._
import org.apache.log4j.LogManager
import com.dstatz.leadscoring.common._
import org.apache.spark.sql.SparkSession

object Boot {
  private lazy val log = LogManager.getLogger(Boot.getClass)

  def main(args: Array[String]): Unit = {
    import com.dstatz.leadscoring.scoring.Scorer._
    import com.dstatz.leadscoring.training.Trainer._
    import com.dstatz.leadscoring.processing.Processor._
    import com.dstatz.leadscoring.reporting.Reporter._

    log.info(s"starting spark app ${args.length}")
    implicit val conf: Config = ConfigFactory.load()
    implicit val factory: AppFactory = new AppFactory(conf)
    implicit val session: SparkSession = factory.getSparkSession

    import factory._
    getSourceReader.readLeads
      .process()
      .trainIfRequired()
      .score()
      .reportResults()

    log.info("Closing Spark Session")
    session.close()
  }
}
