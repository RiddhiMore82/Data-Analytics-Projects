CREATE DATABASE UBER_ANALYSIS;
USE UBER_ANALYSIS;

CREATE TABLE UberDataset(
	Trip_ID INT AUTO_INCREMENT PRIMARY KEY,
    Start_Date DATETIME,
    End_Date DATETIME,
    Category VARCHAR(50),
    Start_Stn VARCHAR(100),
    Stop_Stn VARCHAR(100),
    Miles DECIMAL(6,2),
    Purpose VARCHAR(100)
);

SHOW TABLES;

SELECT * FROM UberDataset LIMIT 3;

-- Beginner Questions
-- Total No of trips:
SELECT COUNT(*) AS Total_Trips FROM UberDataset;

-- Total distance covered (in miles):
SELECT SUM(Miles) AS Total_Miles FROM UberDataset;

-- Count of trips by category (Business vs Personal):
SELECT Category, COUNT(*) FROM UberDataset GROUP BY Category ; 

-- List all unique start locations:
SELECT DISTINCT Start FROM UberDataset;
SELECT COUNT(DISTINCT Start) FROM UberDataset;

-- List all unique trip purposes:
SELECT DISTINCT Purpose FROM UberDataset;

-- Trips where distance > 50 miles:
SELECT * FROM UberDataset WHERE Miles > 50;

-- Trips that started and ended at the same location:
SELECT Start, Stop FROM UberDataset WHERE Start = Stop;

-- Trips with NULL purpose:
SELECT COUNT(*) FROM UberDataset WHERE Purpose IS NULL;

-- Get all trips taken in January:
SELECT * FROM ( SELECT *, MONTH(STR_TO_DATE(Start_Date, '%m/%d/%Y %H:%i')) AS TripMonth FROM UberDataset) AS temp WHERE TripMonth = 1;

-- List trips where category is Personal and purpose is Meeting:
SELECT * FROM UberDataset WHERE Category = 'Personal' AND Purpose = 'Meeting'; -- NO such results in dataset..

-- Intermediate Questions:
-- Number of trips per day:
SELECT DATE(End_Date), COUNT(*) AS TripsPerDay FROM UberDataset GROUP BY DATE(End_Date);

-- Number of trips per month:
SELECT MONTH(End_Date), Count(*) AS TripsPerMonth FROM UberDataset GROUP BY MONTH(End_Date);

-- Total Miles per month:
SELECT MONTH(End_Date), SUM(Miles) AS MilesPerMonth FROM UberDataset GROUP BY MONTH(End_Date);

-- Most Frequent Start Locations:
SELECT Start  AS FrequentStartLoc, COUNT(*) AS TripCount FROM UberDataset GROUP BY Start ORDER BY TripCount DESC;

-- Most Common Trip Purposes:
SELECT Purpose  AS CommonPurpose, COUNT(*) AS TripCount FROM UberDataset GROUP BY Purpose ORDER BY TripCount DESC;

-- Miles Covered Per Purpose:
SELECT Purpose, SUM(Miles) AS MilesCovered FROM UberDataset GROUP BY Purpose; 

-- Average miles per trip by category:
SELECT Category, AVG(Miles) AS AvgMilesByCategory FROM UberDataset GROUP BY Category;

-- Top 5 longest trips:
SELECT * FROM UberDataset ORDER BY Miles DESC LIMIT 5;

-- Top 5 shortest trips:
SELECT * FROM UberDataset ORDER BY Miles LIMIT 5;

-- Trips with duration more than 1 hour:
SELECT *, TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) AS DurationInMins
FROM UberDataset
WHERE TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) > 60;

-- Trips grouped by category and purpose:
SELECT Category, COUNT(Start_Date) AS Trips FROM UberDataset GROUP BY Category;
SELECT Purpose, COUNT(Start_Date) AS Trips FROM UberDataset GROUP BY Purpose;

-- Trip count between specific date range:
SELECT COUNT(Start_Date) AS TripCount 
FROM UberDataset 
WHERE STR_TO_DATE(Start_Date, '%m/%d/%Y') 
      BETWEEN STR_TO_DATE('01/01/2016', '%m/%d/%Y') 
          AND STR_TO_DATE('03/01/2016', '%m/%d/%Y');

-- Total miles driven for Business trips only:
SELECT Category, SUM(Miles) AS TotalMiles FROM UberDataset WHERE Category = "Business";

-- Count of trips with distance between 10 and 20 miles:
SELECT COUNT(Start_Date) FROM UberDataset WHERE Miles BETWEEN 10 AND 20;

-- Advanced Questions:
-- Common Start → Stop combinations with highest frequency:
SELECT Start, Stop, COUNT(*) AS RouteCount FROM UberDataset GROUP BY Start, Stop ORDER BY RouteCount DESC LIMIT 5;

-- Most active day of the week for trips:
SELECT DAYNAME(Start_Date) AS WeekDay, COUNT(*) AS TripCount FROM UberDataset GROUP BY DAYNAME(Start_Date) ORDER BY TripCount DESC;

-- Average duration of trips per purpose:
SELECT Purpose, AVG(TIMESTAMPDIFF(MINUTE, Start_Date, End_Date)) AS AvgDurationMins FROM UberDataset WHERE Purpose IS NOT NULL GROUP BY Purpose;

-- Trip count grouped by weekday vs weekend:
SELECT 
  CASE 
    WHEN DAYOFWEEK(Start_Date) IN (1, 7) THEN 'Weekend'
    ELSE 'Weekday'
  END AS DayType, COUNT(*) AS TripCount FROM UberDataset GROUP BY DayType;

-- Top 3 categories/purposes by total distance:
SELECT Purpose, SUM(Miles) AS TotalMiles FROM UberDataset WHERE Purpose IS NOT NULL GROUP BY Purpose ORDER BY TotalMiles DESC LIMIT 3;

-- Average speed assuming trip duration in hours:
SELECT *, ROUND(Miles / (TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) / 60), 2) AS AvgSpeed_MPH FROM UberDataset WHERE TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) > 0;

-- Window function: Rank top 5 longest trips:
SELECT * FROM (SELECT *, RANK() OVER (ORDER BY Miles DESC) AS TripRank FROM UberDataset) AS RankedTrips WHERE TripRank <= 5;

-- Running total of miles by date:
SELECT DATE(Start_Date) AS TripDate, Miles, SUM(Miles) OVER (ORDER BY DATE(Start_Date)) AS RunningTotalMiles FROM UberDataset;

-- Find gaps in trip dates (dates with no trips):
-- Step 1: Generate a calendar table (if your SQL supports it)
-- Step 2: Left join calendar with trip dates and find missing ones

-- Here's a basic idea using a derived list
SELECT date_list.DateVal FROM (SELECT DATE_ADD('2016-01-01', INTERVAL n DAY) AS DateVal FROM (
    SELECT 0 AS n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL
    SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL
    SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL SELECT 11 UNION ALL
    SELECT 12 UNION ALL SELECT 13 UNION ALL SELECT 14 UNION ALL SELECT 15) AS days ) AS date_list
LEFT JOIN (SELECT DISTINCT DATE(Start_Date) AS TripDate FROM UberDataset) AS trips
ON date_list.DateVal = trips.TripDate
WHERE trips.TripDate IS NULL;

-- Categorize trips as Short (<10mi), Medium (10–30mi), Long (>30mi):
SELECT *, 
  CASE
    WHEN Miles < 10 THEN 'Short'
    WHEN Miles BETWEEN 10 AND 30 THEN 'Medium'
    ELSE 'Long'
  END AS TripCategory FROM UberDataset;

-- Create a view showing all Business trips with duration > 30 mins:
CREATE VIEW LongBusinessTrips AS SELECT *, TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) AS DurationInMins FROM UberDataset WHERE Category = 'Business' AND TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) > 30;

-- Percent of Business vs Personal trips each month:
SELECT MONTH(Start_Date) AS TripMonth, Category, ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY MONTH(Start_Date)), 2) AS Percentage FROM UberDataset GROUP BY MONTH(Start_Date), Category;

-- Calculate average distance difference between Business and Personal trips:
SELECT (SELECT AVG(Miles) FROM UberDataset WHERE Category = 'Business') - (SELECT AVG(Miles) FROM UberDataset WHERE Category = 'Personal') AS DistanceGap;

-- Group trips into time slots (Morning, Afternoon, Evening, Night):
SELECT *, 
  CASE 
    WHEN HOUR(Start_Date) BETWEEN 5 AND 11 THEN 'Morning'
    WHEN HOUR(Start_Date) BETWEEN 12 AND 16 THEN 'Afternoon'
    WHEN HOUR(Start_Date) BETWEEN 17 AND 20 THEN 'Evening'
    ELSE 'Night'
  END AS TimeSlot
FROM UberDataset;

