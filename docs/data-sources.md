# Data Sources

## Overview

This project combines multiple public data sources to analyse the commercial performance of modern console and PC video games.

Each source will be evaluated based on data quality, coverage, and suitability.

---

# Selected Data Sources

## VGChartz Dataset (Kaggle)

Source:

Kaggle

Status:

Selected

Purpose:

Provides historical console games sales information.

Key information:

- Game title
- Platform
- Genre
- Publisher
- Developer
- Critic score
- Regional sales
- Global sales
- Release date

Limitations:

- Sales figures are estimated.
- Primarily focused on console platforms.
- Does not contain pricing information.

---

## Steam Games Dataset (Kaggle)

Source:

Kaggle - Steam Games Dataset

Status:

Selected

Purpose:

Provides PC games information.

Key information:

- Game title
- Release date
- Publisher
- Developer
- Genre
- Price
- Reviews
- Player metric

Limitations:

- Steam data represents only PC gaming.

---

## IsThereAnyDeal API

Source:

IsThereAnyDeal

Status:

Selected

Purpose:

Provides historical pricing and promotional information for PC games.

Key information:

- Store
- Price history
- Discounts

Used for:

- Pricing analysis
- Discount analysis

Limitations:

- Primarily focused on PC storefronts.

---

## IGDB API

Source:

IGDB API

Status:


Purpose:

Provides additional game metadata.

Limitations:

- Requires API access.
- Requires additional data processing.

---

# Unused Data Sources

## SteamDB

Status:

Not used

Purpose:

SteamDB provides detailed Steam application information, including pricing and update history.

Reason not selected:

SteamDB does not provide an official public API and does not permit automated scraping. Data will instead be collected directly from Steam sources or alternative APIs where possible.