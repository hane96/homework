SELECT E.FNAME, E.LNAME, E.SSN
FROM EMPLOYEE E 
JOIN DEPARTMENT D ON E.DNO=D.DNUMBER
JOIN PROJECT P ON D.DNUMBER=P.DNUM
WHERE P.PNAME='ProductX'

UNION

SELECT E.FNAME, E.LNAME, E.SSN
FROM EMPLOYEE E 
JOIN DEPARTMENT D ON D.MGR_SSN=E.SSN
JOIN PROJECT P ON P.DNUM=D.DNUMBER
WHERE PNAME='ProductX'
