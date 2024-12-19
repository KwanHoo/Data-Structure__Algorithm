-- LV1
-- SELECT
-- 조건에 맞는 도서 리스트 출력하기

-- oracle
SELECT
    BOOK_ID,
    TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') PUBLISHED_DATE
FROM
    BOOK
WHERE
    TO_CHAR(PUBLISHED_DATE, 'YYYY') IN ('2021')
    AND CATEGORY IN ('인문')
ORDER BY
    PUBLISHED_DATE ASC

-- mysql
SELECT
    BOOK_ID,
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as DATE_FORMAT
FROM
    BOOK
WHERE
    CATEGORY LIKE '인문'
    AND SUBSTR(PUBLISHED_DATE, 1, 4) = '2021'
ORDER BY
    PUBLISHED_DATE;