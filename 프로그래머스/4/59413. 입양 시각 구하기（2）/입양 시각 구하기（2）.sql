-- 코드를 입력하세요
WITH RECURSIVE HOUR_COUNT
AS(
    SELECT 0 AS H
    UNION ALL
    SELECT H+1
    FROM HOUR_COUNT
    WHERE H < 23
)

SELECT H HOUR, IFNULL(COUNT(AO.ANIMAL_ID), 0) COUNT
FROM HOUR_COUNT HC
LEFT JOIN ANIMAL_OUTS AO ON HC.H = HOUR(AO.DATETIME) 
GROUP BY HC.H
ORDER BY 1
;