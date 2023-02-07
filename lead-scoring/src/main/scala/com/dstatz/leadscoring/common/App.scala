package com.dstatz.leadscoring.common

import AppConf._
import com.typesafe.config._
import org.apache.spark.sql._
import com.dstatz.leadscoring.ingest._

object App {
  case class State(
      sourceData: Source,
      state: Option[DataFrame]
  )

  class Factory(conf: Config) {
    def getSparkSession: SparkSession = {
      SparkSession
        .builder()
        .master("local[1]")
        .appName("lead-score-example")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    }

    def readSource: State = {
      val reader = conf.getStringOrElse("conf.ingest.type", "default") match {
        case "default" => new FileSourceReader(getSparkSession)
      }

      val leadsPath = conf.getString("conf.ingest.leadsPath")
      val eventsPath = conf.getString("conf.ingest.eventsPath")
      val tasksPath = conf.getString("conf.ingest.tasksPath")
      State(reader.readSource(leadsPath, eventsPath, tasksPath), None)
    }
  }

  implicit class RichDataFrame(state: State)(implicit factory: Factory) {
    def process(): State = ???
    def trainIfRequired(): State = ???
    def score(): State = ???
    def report(): State = ???
  }
}
