-- LV1
-- SELECT
-- 어린 동물 찾기

SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE
    INTAKE_CONDITION NOT IN ('Aged')
ORDER BY
    ANIMAL_ID