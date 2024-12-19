-- LV2
-- SUM, MAX, MIN
-- 가격이 제일 비싼 식품의 정보 출력하기

-- oracle
SELECT
    *
FROM
    FOOD_PRODUCT
WHERE
    PRICE IN (
    SELECT MAX(PRICE)
        FROM FOOD_PRODUCT)
-- 조건이 단일이여서 IN대신 '='연산자 사용 가능

-- mysql
SELECT
*
FROM
    FOOD_PRODUCT
ORDER BY PRICE DESC
limit 1