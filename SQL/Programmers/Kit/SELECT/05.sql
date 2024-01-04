-- 프로그래머스
-- SQL 고득점 Kit : SELECT
-- 평균 일일 대여 요금 구하기

-- MySQL
-- 반올림 함수 : ROUND()

SELECT
    ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE
    CAR_TYPE = 'SUV'
GROUP BY
    CAR_TYPE


