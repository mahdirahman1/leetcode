# Write your MySQL query statement below
SELECT m1.name
FROM employee m1
INNER JOIN employee e1
ON e1.managerId = m1.id
GROUP by m1.id
HAVING COUNT(*) >= 5
