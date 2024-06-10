-- 프로그래머스
-- SQL 고득점 Kit : SELECT
-- 흉부외과 또는 일반외과 의사 목록 출력하기

-- 의사이름, 의사IOD, 면허번호, 고용일자, 진료과코드. 전화번호
-- SELECT * FROM DOCTOR;
-- 흉부 CS, 일반, GS인

-- Oracle
select
dr_name as DR_NAME,
dr_id,
mcdp_cd,
to_char(hire_ymd ,'yyyy-mm-dd')
from DOCTOR
where mcdp_cd in('CS','GS')
order by
    hire_ymd desc, dr_name asc

-- MYSQL
SELECT
    DR_NAME AS DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM
    DOCTOR
WHERE
    MCDP_CD LIKE 'CS' OR MCDP_CD LIKE 'GS'
ORDER BY
    HIRE_YMD DESC, DR_NAME ASC;