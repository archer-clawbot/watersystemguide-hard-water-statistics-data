# Data dictionary: hard-water-statistics-2026.csv

UTF-8, comma-separated, RFC 4180 quoting, one header row, one statistic per row.

| Column | Type | Description |
|---|---|---|
| `id` | string | Stable row identifier: a section prefix plus a two-digit sequence (for example `hardness-01`). Unique per row. |
| `section` | string | Topic section the statistic belongs to on the source page (12 sections; see README). |
| `statistic` | string | The statistic as written on the Water System Guide page, checked against the source's exact wording or table value. |
| `source_publisher` | string | Organization that published the source (agency, university, utility, survey publisher or company). |
| `source_title` | string | Title of the source page, report or table. |
| `source_url` | URL | Link to the primary source that was fetched and checked. |
| `source_date` | string | The source's own publication or data date, as stated by the source. Free text, because sources date themselves differently (for example `2019-10-22 (page updated 2026-08-24)` or a data year). |
| `retrieved` | date (YYYY-MM-DD) | Date the source was fetched and the statistic verified. |
