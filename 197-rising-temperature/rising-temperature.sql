# Write your MySQL query statement below
SELECT w2.id
FROM weather w1
INNER JOIN weather w2
ON w1.recordDate = w2.recordDate - INTERVAL 1 DAY
WHERE w2.temperature > w1.temperature