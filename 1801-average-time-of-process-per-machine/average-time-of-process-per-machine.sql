# Write your MySQL query statement below
SELECT a1.machine_id, ROUND(SUM(a2.timestamp - a1.timestamp)/COUNT(*),3) AS processing_time
FROM activity a1
INNER JOIN activity a2
ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
WHERE a1.activity_type = "start" and a2.activity_type = "end"
GROUP BY machine_id