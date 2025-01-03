# Write your MySQL query statement below
SELECT activity_date AS DAY, COUNT(DISTINCT(user_id)) AS ACTIVE_USERS
FROM activity
GROUP BY activity_date
HAVING activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'