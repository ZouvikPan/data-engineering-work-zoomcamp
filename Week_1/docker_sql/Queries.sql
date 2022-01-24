/*How many taxi trips were there on January 15?*/

SELECT COUNT(tpep_pickup_datetime)
FROM yellow_taxi_data
WHERE date(tpep_pickup_datetime)= CAST('2021-01-15' AS DATE);

/*On which day it was the largest tip in January?*/

SELECT tip_amount, tpep_pickup_datetime
FROM yellow_taxi_data
WHERE tip_amount=(SELECT MAX(tip_amount) FROM yellow_taxi_data);

/*What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)?*/

SELECT index, "PULocationID", "DOLocationID", total_amount
FROM yellow_taxi_data
WHERE total_amount=(SELECT MAX(total_amount) FROM yellow_taxi_data);

/*What was the most popular destination for passengers picked up in central park on January 14? Ans- 237 corresponds to Manhattan Upper East Side South*/

SELECT "DOLocationID", COUNT("DOLocationID") AS value_occurence
FROM (SELECT * FROM yellow_taxi_data WHERE DATE(tpep_pickup_datetime)=CAST('2021-01-14' AS DATE) AND "PULocationID"=43) AS jan14
GROUP BY "DOLocationID"
ORDER BY value_occurence DESC
LIMIT 1;