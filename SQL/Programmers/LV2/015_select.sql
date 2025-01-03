-- LV2
-- SELECT
-- 3월에 태어난 여성 회원 목록 출력하기

-- Oracle
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    TO_CHAR(DATE_OF_BIRTH,'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE
    TO_CHAR(DATE_OF_BIRTH,'MM') = '03'
AND GENDER = 'W'
AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;

-- Mysql
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM
    MEMBER_PROFILE
WHERE
    MONTH(DATE_OF_BIRTH) ='03'
    AND GENDER = 'W'
    AND TLNO IS NOT NULL;