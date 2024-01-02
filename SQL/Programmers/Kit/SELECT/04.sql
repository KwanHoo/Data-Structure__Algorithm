-- 프로그래머스
-- SQL 고득점 Kit : SELECT
-- 서울에 위치한 식당 목록 출력하기


-- MySql
SELECT
    rr.rest_id,
    rr.rest_name,
    rr.food_type,
    rr.favorites,
    rr.address,
    round(sum(ri.review_score) / count(rr.rest_id),2) as score
from
    rest_info rr
join rest_review ri
    on rr.rest_id = ri.rest_id
group by rr.rest_id
having rr.address like '서울%'
order by score desc , favorites desc