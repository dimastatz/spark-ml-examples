package com.dstatz.leadscoring.ingest

import org.apache.spark.sql._
import com.dstatz.leadscoring.common._

trait SourceReader {
  def readLeads: Dataset[Lead]
  def readTasks(lead: Lead): Dataset[Task]
  def readEvents(lead: Lead): Dataset[Event]
}
