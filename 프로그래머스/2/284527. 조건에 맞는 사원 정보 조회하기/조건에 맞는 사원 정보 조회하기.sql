-- 코드를 작성해주세요
SELECT HG.SCORE, HE.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_EMPLOYEES HE
LEFT JOIN (
    SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
) HG
ON HE.EMP_NO = HG.EMP_NO
ORDER BY 1 DESC LIMIT 1
;