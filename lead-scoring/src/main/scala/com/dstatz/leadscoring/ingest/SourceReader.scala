package com.dstatz.leadscoring.ingest

trait SourceReader {
  def readSource: Source
}
