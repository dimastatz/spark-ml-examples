package com.dstatz.leadscoring.tests

import com.typesafe.config._
import play.api.libs.json._
import com.dstatz.leadscoring.common._

object TestHelpers {
  org.slf4j.LoggerFactory
    .getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME)
    .asInstanceOf[ch.qos.logback.classic.Logger]
    .setLevel(ch.qos.logback.classic.Level.WARN)

  def getConfig: Config = {
    ConfigFactory.load("test.conf")
  }

  def serialize[T](lead: T): String = {
    implicit val fooWrites: OWrites[T] = Json.writes[T]
    Json.toJson(lead).toString()
  }
}
