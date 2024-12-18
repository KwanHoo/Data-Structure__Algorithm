-- LV1
-- IS NULL
-- 경기도에 위치한 식품창고 목록 출력하기

-- oracle
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    NVL(FREEZER_YN, 'N') AS FREEZER_YN
FROM
    FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;

-- mysql
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    CASE WHEN FREEZER_YN IS NULL THEN 'N'
    ELSE FREEZER_YN
    END AS FREEZER_YN
FROM
    FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;;