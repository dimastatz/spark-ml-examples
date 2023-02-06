package com.dstatz.leadscoring.ingest

import org.apache.spark.sql.Dataset
import com.dstatz.leadscoring.common._

case class Source(
    leads: Dataset[Lead],
    tasks: Dataset[Task],
    events: Dataset[Event]
)
