SELECT E1.FNAME, E1.LNAME
FROM EMPLOYEE E1
JOIN DEPENDENT D ON E1.SSN = D.ESSN
JOIN EMPLOYEE E2 ON D.DEPENDENT_NAME = E2.FNAME AND E1.SEX = E2.SEX
