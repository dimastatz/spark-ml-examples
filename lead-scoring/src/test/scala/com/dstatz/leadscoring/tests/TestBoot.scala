package com.dstatz.leadscoring.tests

import scala.util._
import com.dstatz.leadscoring.Boot
import org.scalatest.funsuite.AnyFunSuite

class TestBoot extends AnyFunSuite {
  test("run boot main") {
    val result = Try(Boot.main(Array[String]()))
    assert(result.isFailure)
  }
}
