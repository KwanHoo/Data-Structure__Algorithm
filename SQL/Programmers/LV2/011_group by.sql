-- LV2
-- GROUP BY
-- 고양이와 개는 몇 마리 있을까

SELECT
    ANIMAL_TYPE
    ,COUNT(ANIMAL_TYPE) COUNT
FROM
    ANIMAL_INS
GROUP BY
    ANIMAL_TYPE
ORDER BY
    ANIMAL_TYPE ASC