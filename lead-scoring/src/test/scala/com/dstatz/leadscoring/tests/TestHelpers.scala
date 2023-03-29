package com.dstatz.leadscoring.tests

import com.typesafe.config._

object TestHelpers {
  org.slf4j.LoggerFactory
    .getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME)
    .asInstanceOf[ch.qos.logback.classic.Logger]
    .setLevel(ch.qos.logback.classic.Level.WARN)

  def getConfig: Config = {
    ConfigFactory.load("test.conf")
  }
}
