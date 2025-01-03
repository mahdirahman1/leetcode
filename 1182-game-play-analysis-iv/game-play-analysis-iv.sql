# Write your MySQL query statement below
SELECT ROUND(COUNT(player_id)/(SELECT COUNT(DISTINCT(player_id)) FROM activity),2) AS fraction
FROM activity
WHERE (player_id, event_date)
IN 
(SELECT player_id, DATE_ADD(min(event_date), INTERVAL 1 DAY)
FROM activity
GROUP by player_id
)
