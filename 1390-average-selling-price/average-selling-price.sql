# Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(p.price * s.units) / SUM(s.units),2),0) as average_price
FROM prices p
LEFT JOIN unitssold s
ON p.product_id = s.product_id AND s.purchase_date BETWEEN p.start_date AND p.end_date
GROUP by p.product_id