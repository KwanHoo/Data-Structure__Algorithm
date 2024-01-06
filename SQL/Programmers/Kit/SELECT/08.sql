-- 프로그래머스
-- SQL 고득점 Kit : SELECT
-- 12세 이하인 여자 환자 목록 출력하기

-- Oracle
SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM FOOD_FACTORY
WHERE
    ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID ASC;