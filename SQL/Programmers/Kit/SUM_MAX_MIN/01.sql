-- 프로그래머스
-- SQL 고득점 Kit : SUM, MAX, MIN
-- 가격이 제일 비싼 식품의 정보 출력하기

-- ORACLE
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE IN (
    SELECT MAX(PRICE)
        FROM FOOD_PRODUCT
)


-- MySQL
-- limit 활용하여 top 1개 출력
SELECT
*
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
limit 1