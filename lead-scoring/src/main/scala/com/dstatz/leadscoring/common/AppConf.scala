package com.dstatz.leadscoring.common

import scala.util.Try
import com.typesafe.config.Config

object AppConf {
  implicit class ConfigExt(conf: Config) {
    def getStringOrElse(key: String, default: String): String = {
      Try(conf.getString(key)).getOrElse(default)
    }
  }
}
