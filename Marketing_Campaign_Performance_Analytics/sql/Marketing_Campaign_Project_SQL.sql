CREATE DATABASE Marketing;

USE Marketing;

CREATE TABLE IF NOT EXISTS marketing_campaigns (
    Campaign_ID       INT,
    Company           VARCHAR(255),
    Campaign_Type     VARCHAR(100),
    Target_Audience   VARCHAR(100),
    Duration          VARCHAR(50),
    Channel_Used      VARCHAR(100),
    Conversion_Rate   FLOAT,
    Acquisition_Cost  INT,
    ROI               FLOAT,
    Location          VARCHAR(100),
    Language          VARCHAR(100),
    Clicks            INT,
    Impressions       INT,
    Engagement_Score  INT,
    Customer_Segment  VARCHAR(100),
    Date              DATE
);

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/marketing_campaign_dataset - Copy.csv'
INTO TABLE marketing_campaigns
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Campaign_ID, Company, Campaign_Type, Target_Audience, Duration,
Channel_Used, Conversion_Rate, Acquisition_Cost, ROI, Location,
Language, Clicks, Impressions, Engagement_Score, Customer_Segment, @date_var)
SET Date = STR_TO_DATE(@date_var, '%m/%d/%Y');

-- Q1 — Channel-wise Average ROI: Find the average ROI for each channel used, rounded to 2 decimal places. Order the results from highest to lowest average ROI.
SELECT  Channel_used, ROUND(AVG(ROI), 2) AS avg_roi
FROM marketing_campaigns
GROUP BY Channel_used
ORDER BY avg_roi DESC;

-- Q2 — Total Acquisition Cost by City: Calculate the total acquisition cost per city (Location). Display only cities where the total acquisition cost exceeds $500 million, ordered by total cost descending.
SELECT Location, SUM(Acquisition_Cost) AS total_acq_cost 
FROM Marketing_campaigns
GROUP BY Location
HAVING SUM(Acquisition_Cost) >= 500000000
ORDER BY total_acq_cost DESC;

-- Q3 — Monthly Conversion Rate Trend: Write a query to show the average conversion rate per month (extracted from the Date column) across all years. Label the months by name (Jan, Feb, etc.) and order chronologically. Identify which month has the highest and which has the lowest average conversion rate.
SELECT  MONTH(Date) AS month_num,
        DATE_FORMAT(Date, '%b') AS month_name,
        AVG(Conversion_Rate) AS avg_conv_rate
FROM Marketing_campaigns 
GROUP BY month_name, month_num
ORDER BY month_num;

-- Q4 — Campaign Type Performance by Audience Segment: For each combination of Campaign_Type and Customer_Segment, calculate the average acquisition cost, average ROI, and total number of campaigns. Filter to only show combinations that have run more than 100 campaigns. Order by average acquisition cost descending.
SELECT Campaign_Type, 
	   Customer_Segment,
	   AVG(Acquisition_Cost) AS avg_acq_cost,
       AVG(ROI) AS avg_roi,
       COUNT(*) AS total_campaigns
FROM Marketing_campaigns
GROUP BY Campaign_Type, Customer_Segment
HAVING COUNT(*) > 100
ORDER BY avg_acq_cost DESC;

-- Q5 — Top Performing Channel per City Using Window Functions: Using window functions, rank channels within each city by their average ROI. Return only the top-ranked channel per city along with its average ROI, total clicks, and total impressions. No subquery-only solutions — must use RANK() or DENSE_RANK().
WITH channel_city_stats AS (
    SELECT
        Location,
        Channel_Used,
        ROUND(AVG(ROI), 2)          AS avg_roi,
        SUM(Clicks)                  AS total_clicks,
        SUM(Impressions)             AS total_impressions
    FROM Marketing_campaigns
    GROUP BY Location, Channel_Used
),
ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY Location
            ORDER BY avg_roi DESC
        ) AS rnk
    FROM channel_city_stats
)
SELECT
    Location,
    Channel_Used,
    avg_roi,
    total_clicks,
    total_impressions
FROM ranked
WHERE rnk = 1
ORDER BY avg_roi DESC;

-- Q6 — Month-over-Month ROI Change with Anomaly Flagging: Calculate the average ROI for each month (using year + month). Then compute the month-over-month percentage change in ROI using a window function. Add a flag column that marks a row as 'Anomaly' if the MoM change is greater than +20% or less than -20%, and 'Normal' otherwise. Order by year and month.
WITH monthly_roi AS (
    SELECT
        YEAR(Date) AS yr,
        MONTH(Date) AS mo,
        DATE_FORMAT(Date, '%b %Y') AS month_label,
        ROUND(AVG(ROI), 4) AS avg_roi
    FROM marketing_campaigns
    GROUP BY yr, mo, month_label
),
mom_calc AS (
    SELECT
        yr,
        mo,
        month_label,
        avg_roi,
        LAG(avg_roi) OVER (
            ORDER BY yr, mo
        )  AS prev_roi
    FROM monthly_roi
)
SELECT
    month_label,
    avg_roi,
    prev_roi,
    ROUND(
        (avg_roi - prev_roi) / prev_roi * 100, 2
    )  AS mom_change_pct,
    CASE
        WHEN prev_roi IS NULL THEN 'N/A'
        WHEN ABS(
            (avg_roi - prev_roi) / prev_roi * 100
        ) > 20 THEN 'Anomaly'
        ELSE 'Normal'
    END AS anomaly_flag
FROM mom_calc
ORDER BY yr, mo;

