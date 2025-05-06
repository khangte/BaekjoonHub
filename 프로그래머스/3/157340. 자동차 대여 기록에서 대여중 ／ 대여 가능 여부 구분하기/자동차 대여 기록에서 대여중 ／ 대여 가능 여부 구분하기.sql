-- 코드를 입력하세요
SELECT CRH.CAR_ID
    , CASE
        WHEN CA2.AVAILABILITY = '대여중' THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CRH
LEFT JOIN (
    SELECT *
    FROM (
        SELECT CAR_ID
            , CASE
                WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
                ELSE '대여 가능'
            END AS AVAILABILITY
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) CA
    WHERE AVAILABILITY = '대여중'
) CA2
    ON CRH.CAR_ID = CA2.CAR_ID
GROUP BY CRH.CAR_ID
ORDER BY 1 DESC;
-- -------------------------------------------------

SELECT CAR_ID,
    CASE
        WHEN SUM(CASE
                    WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1
                    ELSE 0
                END) > 0
            THEN '대여중'
        ELSE '대여 가능'
    END AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;