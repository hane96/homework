SELECT DISTINCT FNAME,LNAME,DNAME,ADDRESS
FROM employee join department on employee.dno=department.dnumber
WHERE Sex='M'