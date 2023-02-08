package com.dstatz.leadscoring.tests

import com.typesafe.config.{Config, ConfigFactory}

object TestHelpers {
  def getConfig: Config = {
    ConfigFactory.load("test.conf")
  }
}
