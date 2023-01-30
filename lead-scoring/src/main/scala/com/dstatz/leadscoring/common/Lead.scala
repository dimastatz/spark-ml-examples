package com.dstatz.leadscoring.common

import org.joda.time.DateTime

case class Lead(
    Id: String,
    Company: String,
    ConvertedAccountId: String,
    ConvertedContactId: String,
    ConvertedData: DateTime,
    Country: String,
    CreateDate: DateTime,
    Domain: String,
    Email: String,
    Industry: String,
    IsConverted: String,
    LastModified: DateTime,
    State: String,
    Title: String
)
