package com.dstatz.leadscoring.ingest

import com.dstatz.leadscoring.common._
import org.apache.spark.sql.SparkSession

class FileSourceReader(session: SparkSession) extends SourceReader {
  override def readSource(
      leadsPath: String,
      eventsPath: String,
      tasksPath: String
  ): Source = {
    import session.implicits._
    val leads = session.read.json(leadsPath).as[Lead]
    val tasks = session.read.json(tasksPath).as[Task]
    val events = session.read.json(eventsPath).as[Event]
    Source(leads, tasks, events)
  }
}
