-- 프로그래머스
-- SQL 고득점 Kit : SELECT
-- 조건에 맞는 도서 리스트 출력하기

select
    book_id,
    to_char(published_date, 'yyyy-mm-dd') as published_date
from book
where
    substr(to_char(published_date, 'yyyymmdd'),1,4) ='2021'
    and category ='인문'
order by published_date asc
;