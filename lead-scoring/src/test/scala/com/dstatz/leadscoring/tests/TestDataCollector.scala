package com.dstatz.leadscoring.tests

import com.dstatz.leadscoring.common._
import org.scalatest.funsuite.AnyFunSuite
import com.typesafe.config.ConfigValueFactory

class TestDataCollector extends AnyFunSuite {
  private val tasks = getClass.getResource("/ingest/tasks.json").getPath
  private val leads = getClass.getResource("/ingest/leads.json").getPath
  private val events = getClass.getResource("/ingest/events.json").getPath

  test("read leads") {
    val conf = TestHelpers.getConfig
      .withValue("conf.ingest.leadsPath", ConfigValueFactory.fromAnyRef(leads))
      .withValue("conf.ingest.tasksPath", ConfigValueFactory.fromAnyRef(tasks))
      .withValue(
        "conf.ingest.eventsPath",
        ConfigValueFactory.fromAnyRef(events)
      )

    val factory = new App.Factory(conf)
    val source = factory.readSource

  }
}
