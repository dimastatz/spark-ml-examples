package com.dstatz.leadscoring.tests

import scala.util.Try
import com.typesafe.config._
import com.dstatz.leadscoring.common._
import org.scalatest.funsuite.AnyFunSuite

class TestDataCollector extends AnyFunSuite {
  test("create spark session") {
    val conf: Config = ConfigFactory.load()
    val factory = new App.Factory(conf)
    val session = factory.getSparkSession
    val state = Try(factory.readSource)
    assert(state.isFailure)
    session.close()
  }

  test("read leads") {}
}
