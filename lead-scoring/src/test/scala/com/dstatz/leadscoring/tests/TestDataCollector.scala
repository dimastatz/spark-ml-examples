package com.dstatz.leadscoring.tests

import scala.util.Try
import com.typesafe.config.ConfigFactory
import org.scalatest.funsuite.AnyFunSuite
import com.dstatz.leadscoring.common.AppFactory

class TestDataCollector extends AnyFunSuite {
  test("create spark session") {
    val conf = ConfigFactory.load()
    val factory = new AppFactory(conf)
    val session = factory.getSparkSession
    val sourceReader = Try(factory.getSourceReader)
    assert(sourceReader.isFailure)
    session.close()
  }

  test("read leads") {}
}
