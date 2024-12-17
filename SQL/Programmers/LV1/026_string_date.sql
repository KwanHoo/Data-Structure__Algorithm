-- LV1
-- String, Date
-- 한 해에 잡은 물고기 수 구하기

SELECT
    COUNT(ID) AS FISH_COUNT
FROM
    FISH_INFO
WHERE
    SUBSTR(TIME,1,4) = '2021'