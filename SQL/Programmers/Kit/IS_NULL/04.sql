-- 프로그래머스
-- SQL 고득점 Kit : IS NULL
-- NULL 처리하기

-- Oracle
SELECT
    ANIMAL_TYPE,
    NVL(NAME, 'No name'),
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

-- MySQL
SELECT
    ANIMAL_TYPE,
    CASE WHEN NAME IS NULL THEN 'No name'
    ELSE NAME END AS NAME
    ,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
ORDER BY ANIMAL_ID ASC;