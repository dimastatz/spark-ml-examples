package com.dstatz.leadscoring.tests

import org.scalatest.funsuite.AnyFunSuite
import com.dstatz.leadscoring.common.SessionFactory

class TestDataCollector extends AnyFunSuite {
  test("create spark session") {
    val session = SessionFactory.getSparkSession()
    session.close()
  }
}
