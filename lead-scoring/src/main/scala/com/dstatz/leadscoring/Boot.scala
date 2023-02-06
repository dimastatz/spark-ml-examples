package com.dstatz.leadscoring

import com.typesafe.config._
import org.apache.log4j.LogManager
import com.dstatz.leadscoring.common._
import org.apache.spark.sql.SparkSession

object Boot {
  private lazy val log = LogManager.getLogger(Boot.getClass)

  def main(args: Array[String]): Unit = {
    import com.dstatz.leadscoring.common.App._

    log.info(s"starting spark app ${args.length}")
    implicit val conf: Config = ConfigFactory.load()
    implicit val factory: App.Factory = new App.Factory(conf)
    implicit val session: SparkSession = factory.getSparkSession

    import factory._
    readSource
      .process()
      .trainIfRequired()
      .score()
      .report()

    log.info("Closing Spark Session")
    session.close()
  }
}
