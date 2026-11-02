SELECT date_trunc('week', created_at) AS week, count(DISTINCT user_id)
FROM events
GROUP BY 1
ORDER BY 1;
