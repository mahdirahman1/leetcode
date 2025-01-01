# Write your MySQL query statement below
SELECT customer_id, count(*) as count_no_trans 
FROM visits v
LEFT JOIN transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
GROUP BY customer_id