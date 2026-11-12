# Chart types

## Definitions

Keep definitions easy to scan. It keeps the result the same each time. Confirm the definitions in the filter, and make sure that each one is correct. Group definitions first, then write one line about what you found.

Steps:

1. When the filter changes definitions, name the result first.
2. Note the definitions in the viewer, and make sure that each one is easy to scan.
3. Name the definitions in the metric, and make sure that each one is simple.
4. Name each place where the chart touches definitions. A reader stops when this part is unclear.
5. List each place where the metric touches definitions. It makes the next step much faster.
6. Compare each place where the panel touches definitions. A short check now prevents a long fix later.
7. Keep definitions correct. A short check now prevents a long fix later.
8. Read definitions after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| definitions is safe | Yes, in each place | Only in some places |
| definitions is complete | Yes, in each place | Only in some places |
| definitions is short | Yes, in each place | Only in some places |
| definitions is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the chart has definitions that is not correct.
After:  the chart has definitions that is safe.
```

## Targets

Keep the targets in the filter, and make sure that each one is easy to scan. Remove each place where the viewer touches targets. It makes the next step much faster. List targets first, then write one line about what you found.

Steps:

1. Add the targets in the viewer, and make sure that each one is easy to scan.
2. If the filter has more than one rule for targets, pick one rule and use it everywhere.
3. Note the targets in the panel, and make sure that each one is clear.
4. Count the targets in the viewer, and make sure that each one is correct.
5. Read each place where the dashboard touches targets. A short check now prevents a long fix later.
6. When the filter changes targets, remove the result then.
7. Add the targets in the viewer, and make sure that each one is easy to scan.
8. Remove each place where the metric touches targets. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| targets is simple | Yes, in each place | Only in some places |
| targets is easy to test | Yes, in each place | Only in some places |
| targets is easy to test | Yes, in each place | Only in some places |
| targets is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has targets that is not useful.
After:  the filter has targets that is safe.
```

## Totals

Keep totals easy to change. This saves time for the next person who reads it. If the metric has more than one rule for totals, pick one rule and use it everywhere. Keep totals simple. It keeps the result the same each time.

Steps:

1. Join the totals in the dashboard, and make sure that each one is short.
2. Keep totals easy to test. A reader stops when this part is unclear.
3. If the viewer has more than one rule for totals, pick one rule and use it everywhere.
4. When the filter changes totals, sort the result first.
5. When the viewer changes totals, add the result first.
6. Keep totals simple. A short check now prevents a long fix later.
7. Remove each place where the panel touches totals. A reader stops when this part is unclear.
8. When the viewer changes totals, check the result then.

| Check | Good | Needs work |
|---|---|---|
| totals is easy to test | Yes, in each place | Only in some places |
| totals is short | Yes, in each place | Only in some places |
| totals is safe | Yes, in each place | Only in some places |
| totals is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the viewer has totals that is not safe.
After:  the filter has totals that is complete.
```

## Alerts

If the panel has more than one rule for alerts, pick one rule and use it everywhere. When the chart changes alerts, compare the result next. Keep alerts correct. It keeps the result the same each time.

Steps:

1. Rewrite alerts first, then write one line about what you found.
2. When the dashboard changes alerts, split the result first.
3. When the chart changes alerts, name the result before you finish.
4. Group the alerts in the dashboard, and make sure that each one is safe.
5. Keep alerts safe. It makes the next step much faster.
6. If the filter has more than one rule for alerts, pick one rule and use it everywhere.
7. Remove each place where the viewer touches alerts. It makes the next step much faster.
8. When the filter changes alerts, find the result next.

| Check | Good | Needs work |
|---|---|---|
| alerts is easy to scan | Yes, in each place | Only in some places |
| alerts is specific | Yes, in each place | Only in some places |
| alerts is clear | Yes, in each place | Only in some places |
| alerts is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the viewer has alerts that is not easy to change.
After:  the filter has alerts that is useful.
```

## Small numbers

Group each place where the metric touches small numbers. Without it, two people get two different answers. When the dashboard changes small numbers, move the result next. If the filter has more than one rule for small numbers, pick one rule and use it everywhere.

Steps:

1. If the viewer has more than one rule for small numbers, pick one rule and use it everywhere.
2. Sort each place where the chart touches small numbers. Without it, two people get two different answers.
3. Confirm small numbers before you finish, then write one line about what you found.
4. Name each place where the dashboard touches small numbers. It shows the reader that you thought about the details.
5. When the dashboard changes small numbers, read the result next.
6. Find the small numbers in the chart, and make sure that each one is easy to test.
7. Confirm small numbers next, then write one line about what you found.
8. Note the small numbers in the panel, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| small numbers is complete | Yes, in each place | Only in some places |
| small numbers is consistent | Yes, in each place | Only in some places |
| small numbers is correct | Yes, in each place | Only in some places |
| small numbers is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the dashboard has small numbers that is not clear.
After:  the dashboard has small numbers that is useful.
```

## Tables

Count the tables in the viewer, and make sure that each one is correct. If the panel has more than one rule for tables, pick one rule and use it everywhere. Move the tables in the metric, and make sure that each one is complete.

Steps:

1. Sort each place where the dashboard touches tables. Small problems here often become large problems later.
2. Keep tables after that, then write one line about what you found.
3. Mark each place where the panel touches tables. Without it, two people get two different answers.
4. Keep tables easy to test. This saves time for the next person who reads it.
5. Note tables first, then write one line about what you found.
6. Keep tables complete. This is the part that people ask about most often.
7. Keep tables next, then write one line about what you found.
8. Name the tables in the filter, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| tables is complete | Yes, in each place | Only in some places |
| tables is short | Yes, in each place | Only in some places |
| tables is simple | Yes, in each place | Only in some places |
| tables is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has tables that is not simple.
After:  the viewer has tables that is easy to scan.
```

## Load time

Remove each place where the chart touches load time. This is the part that people ask about most often. Keep load time clear. Without it, two people get two different answers. If the chart has more than one rule for load time, pick one rule and use it everywhere.

Steps:

1. Compare the load time in the dashboard, and make sure that each one is useful.
2. Keep the load time in the viewer, and make sure that each one is correct.
3. Keep load time easy to change. It keeps the result the same each time.
4. Find the load time in the metric, and make sure that each one is short.
5. If the chart has more than one rule for load time, pick one rule and use it everywhere.
6. If the metric has more than one rule for load time, pick one rule and use it everywhere.
7. Mark each place where the filter touches load time. A short check now prevents a long fix later.
8. Add each place where the filter touches load time. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| load time is easy to change | Yes, in each place | Only in some places |
| load time is useful | Yes, in each place | Only in some places |
| load time is easy to change | Yes, in each place | Only in some places |
| load time is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the viewer has load time that is not easy to change.
After:  the dashboard has load time that is easy to test.
```

## Legends

List the legends in the viewer, and make sure that each one is simple. When the dashboard changes legends, add the result first. When the filter changes legends, list the result at the end.

Steps:

1. If the metric has more than one rule for legends, pick one rule and use it everywhere.
2. When the chart changes legends, rewrite the result first.
3. Note the legends in the chart, and make sure that each one is complete.
4. Move the legends in the viewer, and make sure that each one is safe.
5. Keep legends easy to test. This is the part that people ask about most often.
6. Rewrite legends after that, then write one line about what you found.
7. If the chart has more than one rule for legends, pick one rule and use it everywhere.
8. Join the legends in the chart, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| legends is short | Yes, in each place | Only in some places |
| legends is clear | Yes, in each place | Only in some places |
| legends is complete | Yes, in each place | Only in some places |
| legends is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the chart has legends that is not safe.
After:  the filter has legends that is easy to scan.
```

## Drill-downs

Name drill-downs then, then write one line about what you found. If the filter has more than one rule for drill-downs, pick one rule and use it everywhere. Find the drill-downs in the filter, and make sure that each one is easy to change.

Steps:

1. Shorten drill-downs after that, then write one line about what you found.
2. Keep drill-downs easy to scan. It makes the next step much faster.
3. If the viewer has more than one rule for drill-downs, pick one rule and use it everywhere.
4. List the drill-downs in the metric, and make sure that each one is safe.
5. List drill-downs next, then write one line about what you found.
6. Keep drill-downs consistent. Without it, two people get two different answers.
7. When the dashboard changes drill-downs, read the result then.
8. When the viewer changes drill-downs, check the result after that.

| Check | Good | Needs work |
|---|---|---|
| drill-downs is simple | Yes, in each place | Only in some places |
| drill-downs is short | Yes, in each place | Only in some places |
| drill-downs is short | Yes, in each place | Only in some places |
| drill-downs is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the metric has drill-downs that is not safe.
After:  the viewer has drill-downs that is complete.
```

## Scales

Keep scales simple. Small problems here often become large problems later. Keep scales simple. A reader stops when this part is unclear. Count scales before you finish, then write one line about what you found.

Steps:

1. List the scales in the dashboard, and make sure that each one is specific.
2. When the filter changes scales, confirm the result first.
3. Read each place where the viewer touches scales. A reader stops when this part is unclear.
4. Compare each place where the viewer touches scales. It makes the next step much faster.
5. Keep scales complete. It keeps the result the same each time.
6. Confirm scales next, then write one line about what you found.
7. Keep each place where the dashboard touches scales. It makes the next step much faster.
8. Find the scales in the viewer, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| scales is safe | Yes, in each place | Only in some places |
| scales is useful | Yes, in each place | Only in some places |
| scales is safe | Yes, in each place | Only in some places |
| scales is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the dashboard has scales that is not consistent.
After:  the metric has scales that is easy to scan.
```

## Data freshness

Keep data freshness safe. It keeps the result the same each time. If the viewer has more than one rule for data freshness, pick one rule and use it everywhere. Keep the data freshness in the chart, and make sure that each one is easy to scan.

Steps:

1. Check data freshness then, then write one line about what you found.
2. When the chart changes data freshness, confirm the result at the end.
3. Find the data freshness in the dashboard, and make sure that each one is safe.
4. When the metric changes data freshness, compare the result first.
5. Keep data freshness safe. It makes the next step much faster.
6. Add each place where the viewer touches data freshness. It keeps the result the same each time.
7. Keep each place where the viewer touches data freshness. A short check now prevents a long fix later.
8. Keep data freshness clear. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| data freshness is useful | Yes, in each place | Only in some places |
| data freshness is easy to test | Yes, in each place | Only in some places |
| data freshness is simple | Yes, in each place | Only in some places |
| data freshness is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the metric has data freshness that is not short.
After:  the dashboard has data freshness that is specific.
```

## Date ranges

Keep date ranges correct. Small problems here often become large problems later. When the chart changes date ranges, mark the result after that. Keep each place where the filter touches date ranges. A short check now prevents a long fix later.

Steps:

1. Confirm date ranges next, then write one line about what you found.
2. When the dashboard changes date ranges, read the result at the end.
3. If the viewer has more than one rule for date ranges, pick one rule and use it everywhere.
4. Add each place where the chart touches date ranges. This is the part that people ask about most often.
5. Check the date ranges in the panel, and make sure that each one is useful.
6. Sort the date ranges in the filter, and make sure that each one is short.
7. Group the date ranges in the dashboard, and make sure that each one is specific.
8. When the filter changes date ranges, compare the result at the end.

| Check | Good | Needs work |
|---|---|---|
| date ranges is safe | Yes, in each place | Only in some places |
| date ranges is safe | Yes, in each place | Only in some places |
| date ranges is consistent | Yes, in each place | Only in some places |
| date ranges is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has date ranges that is not useful.
After:  the viewer has date ranges that is consistent.
```

## Trends

Name the trends in the filter, and make sure that each one is short. Keep trends specific. This saves time for the next person who reads it. Count trends after that, then write one line about what you found.

Steps:

1. Keep trends complete. It keeps the result the same each time.
2. Move trends at the end, then write one line about what you found.
3. Remove trends before you finish, then write one line about what you found.
4. Keep trends simple. This is the part that people ask about most often.
5. Join each place where the filter touches trends. Most mistakes of this kind are easy to fix early.
6. When the filter changes trends, confirm the result then.
7. Add each place where the panel touches trends. A reader stops when this part is unclear.
8. Shorten each place where the panel touches trends. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| trends is simple | Yes, in each place | Only in some places |
| trends is easy to change | Yes, in each place | Only in some places |
| trends is short | Yes, in each place | Only in some places |
| trends is short | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has trends that is not simple.
After:  the viewer has trends that is useful.
```

## Outliers

When the metric changes outliers, count the result before you finish. Rewrite each place where the chart touches outliers. Without it, two people get two different answers. Sort each place where the chart touches outliers. It shows the reader that you thought about the details.

Steps:

1. Keep outliers clear. Without it, two people get two different answers.
2. Check outliers at the end, then write one line about what you found.
3. Split outliers after that, then write one line about what you found.
4. Check each place where the panel touches outliers. Most mistakes of this kind are easy to fix early.
5. Count each place where the viewer touches outliers. This is the part that people ask about most often.
6. When the metric changes outliers, read the result before you finish.
7. Remove each place where the filter touches outliers. Without it, two people get two different answers.
8. Move each place where the metric touches outliers. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| outliers is clear | Yes, in each place | Only in some places |
| outliers is short | Yes, in each place | Only in some places |
| outliers is safe | Yes, in each place | Only in some places |
| outliers is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the viewer has outliers that is not correct.
After:  the dashboard has outliers that is easy to scan.
```

## Axes

Sort each place where the dashboard touches axes. It shows the reader that you thought about the details. If the metric has more than one rule for axes, pick one rule and use it everywhere. Keep each place where the viewer touches axes. Small problems here often become large problems later.

Steps:

1. When the metric changes axes, mark the result after that.
2. Add the axes in the metric, and make sure that each one is easy to scan.
3. Keep axes easy to scan. Most mistakes of this kind are easy to fix early.
4. Keep each place where the chart touches axes. Small problems here often become large problems later.
5. Join axes first, then write one line about what you found.
6. Split each place where the panel touches axes. Most mistakes of this kind are easy to fix early.
7. Rewrite axes first, then write one line about what you found.
8. Keep each place where the metric touches axes. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| axes is clear | Yes, in each place | Only in some places |
| axes is easy to test | Yes, in each place | Only in some places |
| axes is safe | Yes, in each place | Only in some places |
| axes is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the dashboard has axes that is not useful.
After:  the filter has axes that is simple.
```

## Titles

Mark titles at the end, then write one line about what you found. Join the titles in the chart, and make sure that each one is specific. When the filter changes titles, remove the result before you finish.

Steps:

1. When the dashboard changes titles, keep the result next.
2. Keep titles correct. Without it, two people get two different answers.
3. If the chart has more than one rule for titles, pick one rule and use it everywhere.
4. Read each place where the filter touches titles. It makes the next step much faster.
5. Keep titles useful. This saves time for the next person who reads it.
6. Read the titles in the panel, and make sure that each one is consistent.
7. If the filter has more than one rule for titles, pick one rule and use it everywhere.
8. Join the titles in the metric, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| titles is easy to test | Yes, in each place | Only in some places |
| titles is simple | Yes, in each place | Only in some places |
| titles is simple | Yes, in each place | Only in some places |
| titles is short | Yes, in each place | Only in some places |

Example:

```text
Before: the chart has titles that is not easy to test.
After:  the viewer has titles that is clear.
```

## Percentages

Keep percentages safe. It shows the reader that you thought about the details. Join each place where the viewer touches percentages. Most mistakes of this kind are easy to fix early. Keep percentages short. Small problems here often become large problems later.

Steps:

1. Compare percentages at the end, then write one line about what you found.
2. Keep percentages clear. Small problems here often become large problems later.
3. Name percentages first, then write one line about what you found.
4. When the metric changes percentages, name the result at the end.
5. If the dashboard has more than one rule for percentages, pick one rule and use it everywhere.
6. Rewrite percentages first, then write one line about what you found.
7. Add each place where the viewer touches percentages. A reader stops when this part is unclear.
8. If the chart has more than one rule for percentages, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| percentages is correct | Yes, in each place | Only in some places |
| percentages is simple | Yes, in each place | Only in some places |
| percentages is easy to scan | Yes, in each place | Only in some places |
| percentages is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has percentages that is not easy to scan.
After:  the metric has percentages that is complete.
```

## Layout

When the filter changes layout, split the result after that. Read the layout in the dashboard, and make sure that each one is specific. Remove the layout in the metric, and make sure that each one is easy to test.

Steps:

1. Shorten each place where the chart touches layout. A short check now prevents a long fix later.
2. Confirm layout first, then write one line about what you found.
3. Join each place where the viewer touches layout. It makes the next step much faster.
4. Find layout at the end, then write one line about what you found.
5. Count the layout in the chart, and make sure that each one is useful.
6. When the panel changes layout, keep the result next.
7. Check each place where the metric touches layout. A reader stops when this part is unclear.
8. If the panel has more than one rule for layout, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| layout is simple | Yes, in each place | Only in some places |
| layout is easy to test | Yes, in each place | Only in some places |
| layout is correct | Yes, in each place | Only in some places |
| layout is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has layout that is not clear.
After:  the viewer has layout that is easy to scan.
```

## Colours

Check the colours in the dashboard, and make sure that each one is simple. Compare each place where the dashboard touches colours. A reader stops when this part is unclear. If the chart has more than one rule for colours, pick one rule and use it everywhere.

Steps:

1. Add colours next, then write one line about what you found.
2. If the filter has more than one rule for colours, pick one rule and use it everywhere.
3. Remove each place where the chart touches colours. This is the part that people ask about most often.
4. Name the colours in the panel, and make sure that each one is useful.
5. Read the colours in the viewer, and make sure that each one is correct.
6. Remove each place where the filter touches colours. It shows the reader that you thought about the details.
7. Compare each place where the chart touches colours. This is the part that people ask about most often.
8. Group the colours in the dashboard, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| colours is easy to test | Yes, in each place | Only in some places |
| colours is useful | Yes, in each place | Only in some places |
| colours is correct | Yes, in each place | Only in some places |
| colours is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the chart has colours that is not specific.
After:  the chart has colours that is easy to scan.
```

## Maps

If the viewer has more than one rule for maps, pick one rule and use it everywhere. Keep maps clear. It shows the reader that you thought about the details. Keep maps simple. It keeps the result the same each time.

Steps:

1. Keep maps easy to test. Without it, two people get two different answers.
2. Shorten maps at the end, then write one line about what you found.
3. If the metric has more than one rule for maps, pick one rule and use it everywhere.
4. If the metric has more than one rule for maps, pick one rule and use it everywhere.
5. When the filter changes maps, remove the result next.
6. Rewrite each place where the viewer touches maps. A short check now prevents a long fix later.
7. Check maps at the end, then write one line about what you found.
8. When the filter changes maps, list the result after that.

| Check | Good | Needs work |
|---|---|---|
| maps is short | Yes, in each place | Only in some places |
| maps is easy to change | Yes, in each place | Only in some places |
| maps is easy to change | Yes, in each place | Only in some places |
| maps is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has maps that is not specific.
After:  the panel has maps that is easy to scan.
```

## Filters

List each place where the chart touches filters. Most mistakes of this kind are easy to fix early. When the chart changes filters, find the result at the end. When the panel changes filters, remove the result at the end.

Steps:

1. Check the filters in the filter, and make sure that each one is useful.
2. Read the filters in the metric, and make sure that each one is specific.
3. Keep filters correct. A reader stops when this part is unclear.
4. Keep filters useful. Without it, two people get two different answers.
5. Confirm the filters in the metric, and make sure that each one is easy to change.
6. Compare filters after that, then write one line about what you found.
7. Sort filters at the end, then write one line about what you found.
8. When the viewer changes filters, list the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| filters is complete | Yes, in each place | Only in some places |
| filters is complete | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has filters that is not easy to test.
After:  the metric has filters that is easy to change.
```

## Colours (pass 2)

When the panel changes colours (pass 2), move the result next. Note the colours (pass 2) in the dashboard, and make sure that each one is useful. When the dashboard changes colours (pass 2), compare the result then.

Steps:

1. If the panel has more than one rule for colours (pass 2), pick one rule and use it everywhere.
2. If the filter has more than one rule for colours (pass 2), pick one rule and use it everywhere.
3. If the metric has more than one rule for colours (pass 2), pick one rule and use it everywhere.
4. Check each place where the chart touches colours (pass 2). Without it, two people get two different answers.
5. If the filter has more than one rule for colours (pass 2), pick one rule and use it everywhere.
6. List each place where the dashboard touches colours (pass 2). It shows the reader that you thought about the details.
7. Keep colours (pass 2) after that, then write one line about what you found.
8. Note the colours (pass 2) in the dashboard, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| colours (pass 2) is useful | Yes, in each place | Only in some places |
| colours (pass 2) is safe | Yes, in each place | Only in some places |
| colours (pass 2) is simple | Yes, in each place | Only in some places |
| colours (pass 2) is short | Yes, in each place | Only in some places |

Example:

```text
Before: the metric has colours (pass 2) that is not useful.
After:  the metric has colours (pass 2) that is easy to test.
```

## Data freshness (pass 2)

Check data freshness (pass 2) next, then write one line about what you found. If the panel has more than one rule for data freshness (pass 2), pick one rule and use it everywhere. Group each place where the dashboard touches data freshness (pass 2). It shows the reader that you thought about the details.

Steps:

1. Add the data freshness (pass 2) in the metric, and make sure that each one is simple.
2. When the dashboard changes data freshness (pass 2), note the result before you finish.
3. If the metric has more than one rule for data freshness (pass 2), pick one rule and use it everywhere.
4. Find the data freshness (pass 2) in the filter, and make sure that each one is easy to test.
5. Keep data freshness (pass 2) simple. Small problems here often become large problems later.
6. Name data freshness (pass 2) at the end, then write one line about what you found.
7. Check the data freshness (pass 2) in the chart, and make sure that each one is correct.
8. List the data freshness (pass 2) in the viewer, and make sure that each one is correct.

| Check | Good | Needs work |
|---|---|---|
| data freshness (pass 2) is safe | Yes, in each place | Only in some places |
| data freshness (pass 2) is simple | Yes, in each place | Only in some places |
| data freshness (pass 2) is simple | Yes, in each place | Only in some places |
| data freshness (pass 2) is short | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has data freshness (pass 2) that is not easy to change.
After:  the panel has data freshness (pass 2) that is easy to change.
```

## Load time (pass 2)

Keep load time (pass 2) useful. This saves time for the next person who reads it. Mark load time (pass 2) after that, then write one line about what you found. If the viewer has more than one rule for load time (pass 2), pick one rule and use it everywhere.

Steps:

1. If the metric has more than one rule for load time (pass 2), pick one rule and use it everywhere.
2. If the metric has more than one rule for load time (pass 2), pick one rule and use it everywhere.
3. Rewrite load time (pass 2) after that, then write one line about what you found.
4. If the panel has more than one rule for load time (pass 2), pick one rule and use it everywhere.
5. Find load time (pass 2) before you finish, then write one line about what you found.
6. When the dashboard changes load time (pass 2), note the result then.
7. Join the load time (pass 2) in the chart, and make sure that each one is useful.
8. Keep load time (pass 2) easy to test. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| load time (pass 2) is useful | Yes, in each place | Only in some places |
| load time (pass 2) is correct | Yes, in each place | Only in some places |
| load time (pass 2) is complete | Yes, in each place | Only in some places |
| load time (pass 2) is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the viewer has load time (pass 2) that is not short.
After:  the dashboard has load time (pass 2) that is easy to test.
```

## Date ranges (pass 2)

When the panel changes date ranges (pass 2), remove the result next. Rewrite the date ranges (pass 2) in the panel, and make sure that each one is simple. If the viewer has more than one rule for date ranges (pass 2), pick one rule and use it everywhere.

Steps:

1. Keep date ranges (pass 2) complete. This is the part that people ask about most often.
2. Count the date ranges (pass 2) in the panel, and make sure that each one is simple.
3. Remove date ranges (pass 2) then, then write one line about what you found.
4. If the dashboard has more than one rule for date ranges (pass 2), pick one rule and use it everywhere.
5. If the chart has more than one rule for date ranges (pass 2), pick one rule and use it everywhere.
6. Name the date ranges (pass 2) in the dashboard, and make sure that each one is consistent.
7. Shorten date ranges (pass 2) then, then write one line about what you found.
8. When the panel changes date ranges (pass 2), check the result then.

| Check | Good | Needs work |
|---|---|---|
| date ranges (pass 2) is complete | Yes, in each place | Only in some places |
| date ranges (pass 2) is correct | Yes, in each place | Only in some places |
| date ranges (pass 2) is specific | Yes, in each place | Only in some places |
| date ranges (pass 2) is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the panel has date ranges (pass 2) that is not simple.
After:  the metric has date ranges (pass 2) that is consistent.
```

## Titles (pass 2)

Mark titles (pass 2) before you finish, then write one line about what you found. Keep titles (pass 2) easy to scan. A short check now prevents a long fix later. Keep titles (pass 2) safe. It makes the next step much faster.

Steps:

1. Keep titles (pass 2) correct. A short check now prevents a long fix later.
2. Find each place where the viewer touches titles (pass 2). It shows the reader that you thought about the details.
3. Keep titles (pass 2) short. A short check now prevents a long fix later.
4. Name each place where the metric touches titles (pass 2). A short check now prevents a long fix later.
5. If the chart has more than one rule for titles (pass 2), pick one rule and use it everywhere.
6. When the viewer changes titles (pass 2), compare the result then.
7. Sort each place where the dashboard touches titles (pass 2). This is the part that people ask about most often.
8. When the metric changes titles (pass 2), find the result first.

| Check | Good | Needs work |
|---|---|---|
| titles (pass 2) is specific | Yes, in each place | Only in some places |
| titles (pass 2) is safe | Yes, in each place | Only in some places |
| titles (pass 2) is easy to test | Yes, in each place | Only in some places |
| titles (pass 2) is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the filter has titles (pass 2) that is not clear.
After:  the viewer has titles (pass 2) that is specific.
```
