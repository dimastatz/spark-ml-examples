package com.dstatz.leadscoring.tests

import org.scalatest.funsuite.AnyFunSuite

class TestDataCollector extends AnyFunSuite {
  private val tasks = getClass.getResource("/ingest/tasks.json").getPath
  private val leads = getClass.getResource("/ingest/leads.json").getPath
  private val events = getClass.getResource("/ingest/events.json").getPath

  test("read leads") {
    assert(1 == 1)
  }
}
