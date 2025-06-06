-- 코드를 입력하세요
SELECT YEAR(OS.SALES_DATE) YEAR, 
    MONTH(OS.SALES_DATE) MONTH,
    UI.GENDER GENDER,
    COUNT(DISTINCT UI.USER_ID) USERS -- 중복된 회원 제거
FROM ONLINE_SALE OS
JOIN USER_INFO UI
ON OS.USER_ID = UI.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY YEAR(OS.SALES_DATE), MONTH(OS.SALES_DATE), UI.GENDER
ORDER BY 1,2,3
;
