import os
import sqlite3

DB_PATH = 'database.db'
db_conn = 0


def createTables():
    global db_conn
    db_conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
                     (ID INT PRIMARY KEY NOT NULL,
                     NAME TEXT,
                     SALARY INT,
                     DEPT_ID INT,
                     FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(ID));''')

    db_conn.execute('''CREATE TABLE IF NOT EXISTS DEPARTMENT
                     (ID INT PRIMARY KEY NOT NULL,
                     NAME TEXT,
                     LOCATION  TEXT);''')


def insertIntoETable(newID, newName, newSalary, newDeptId):
    global db_conn
    db_conn.execute("INSERT INTO EMPLOYEE (ID,NAME ,SALARY,DEPT_ID)\
                    VALUES( \"" + str(newID) + "\",\"" + newName + "\", \"" + str(newSalary) + "\", \"" \
                    + str(newDeptId) + "\");")


def insertIntoDTable(newID, newName, newLocation):
    global db_conn
    db_conn.execute("INSERT INTO DEPARTMENT (ID,NAME ,LOCATION)\
                        VALUES( \"" + str(newID) + "\",\"" + newName + "\", \"" + newLocation + "\");")


def createTest():
    global db_conn
    db_conn = sqlite3.connect(DB_PATH)
    createTables()

    insertIntoETable(1, "Candice", 4685, 1)
    insertIntoETable(2, "Julia", 2559, 2)
    insertIntoETable(3, "Bob", 4405, 4)
    insertIntoETable(4, "Scarlet", 2350, 1)
    insertIntoETable(5, "Ileana", 1151, 4)

    insertIntoDTable(1, "Executive", "Sydney")
    insertIntoDTable(2, "Production", "Sydney")
    insertIntoDTable(3, "Resources", "Cape Town")
    insertIntoDTable(4, "Technical", "Texas")
    insertIntoDTable(5, "Management", "Paris")

    db_conn.commit()
    db_conn.close()


def printResult(result):
    print("Department name | Employee count ")
    for row in result:
        print(str(row[0]) + ' \t ' * 2 + str(row[1]))


def findEmployeeCount():
    global db_conn
    db_conn = sqlite3.connect(DB_PATH)
    cursor = db_conn.cursor()
    cursor.execute('''SELECT DEPARTMENT.NAME, COUNT(EMPLOYEE.DEPT_ID) 
                    FROM DEPARTMENT
                    LEFT JOIN EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID
                    GROUP BY DEPARTMENT.ID
                    ORDER BY COUNT(EMPLOYEE.DEPT_ID) DESC; ''')
    result = cursor.fetchall()
    db_conn.commit()
    db_conn.close()

    return result


if __name__ == '__main__':
    if not os.path.isfile(DB_PATH):
        createTest()
    emp_count = findEmployeeCount()
    printResult(emp_count)
