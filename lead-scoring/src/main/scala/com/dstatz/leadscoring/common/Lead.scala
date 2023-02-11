package com.dstatz.leadscoring.common

import java.sql._

case class Lead(
    Id: String,
    Company: String,
    ConvertedAccountId: String,
    ConvertedContactId: String,
    ConvertedData: Timestamp,
    Country: String,
    CreateDate: Timestamp,
    Domain: String,
    Email: String,
    Industry: String,
    IsConverted: String,
    LastModified: Timestamp,
    State: String,
    Title: String
)
