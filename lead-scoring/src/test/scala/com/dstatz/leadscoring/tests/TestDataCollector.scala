package com.dstatz.leadscoring.tests

import scala.util.Try
import org.scalatest.funsuite.AnyFunSuite
import com.dstatz.leadscoring.common.SessionFactory
import com.dstatz.leadscoring.ingest.SourceReadersFactory

class TestDataCollector extends AnyFunSuite {
  test("create spark session") {
    val session = SessionFactory.getSparkSession()
    val sourceReader = Try(SourceReadersFactory.getSourceReader(session))
    assert(sourceReader.isFailure)
    session.close()
  }
}
