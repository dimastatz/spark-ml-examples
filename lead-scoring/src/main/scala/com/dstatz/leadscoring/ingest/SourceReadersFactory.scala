package com.dstatz.leadscoring.ingest

import org.apache.spark.sql._
import com.typesafe.config.Config
import com.dstatz.leadscoring.common._

object SourceReadersFactory {
  def getSourceReader(
      session: SparkSession,
      conf: Config
  ): Option[SourceReader] = {
    import session.implicits._

    conf.getString("sourceType") match {
      case "fs" =>
        Some(new {} with SourceReader {
          override def readLeads: Dataset[Lead] =
            session.read.json(conf.getString("leadsPath")).as[Lead]

          override def readTasks(lead: Lead): Dataset[Task] = ???

          override def readEvents(lead: Lead): Dataset[Event] = ???
        })
      case _ => None
    }
  }
}
