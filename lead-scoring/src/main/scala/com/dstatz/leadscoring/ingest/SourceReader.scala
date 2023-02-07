package com.dstatz.leadscoring.ingest

trait SourceReader {
  def readSource(
      leadsPath: String,
      eventsPath: String,
      tasksPath: String
  ): Source
}
