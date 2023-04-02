package com.dstatz.leadscoring.tests

import org.apache.spark.sql.SparkSession
import org.scalatest.funsuite.AnyFunSuite
import com.dstatz.leadscoring.processing.Cruncher

class TestCruncher extends AnyFunSuite {
  val spark: SparkSession = TestHelpers.getSparkSession

  test("test get changes") {
    import spark.implicits._
    val df = Seq((1, "bat"), (2, "mouse"), (2, "horse"))
      .toDF("number", "word")

    val resultDf = Cruncher.getChanges(df)
    assert(df.count() == resultDf.count())
  }
}
