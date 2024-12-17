-- LV1
-- SUM, MAX, MIN
-- 잡은 물고기 중 가장 큰 물고기의 길이 구하기

SELECT
    CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM
    FISH_INFO

-- CONCAT() : 괄호 안의 내용을 이어줌
-- CONCAT_WS('S', ...) 괄호 안의 내용을 S로 이어줌
-- CONCAT_WS('-', 'H', 'W') -> H-W

-- FORMAT(~~, 숫자) : ~~을 소수점 (숫자)자리에서 반올림
-- FORMAT(3.141592, 2) -> 3.14