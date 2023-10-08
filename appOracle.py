import oracledb

# Conexión a la base de datos Oracle
connection = oracledb.connect("System/admin@localhost/xepdb1")

#Funcion para agregar departamentos add_deptno
def addDepto(deptno, dname, loc):
    try:
        cursor = connection.cursor()

        cursor.callproc("add_depto", [deptno, dname, loc])

        connection.commit()
        print("Departamento agregado con éxito")

    finally:
        cursor.close()
        connection.close()

#Funcion para actualizar departamento Update_depto()
def updateDepto(deptno, dname, loc):
    try:
        cursor = connection.cursor()

        cursor.callproc("Update_depto", [deptno, dname, loc])

        connection.commit()
        print("Departamento actualizado con éxito")

    finally:
        cursor.close()
        connection.close()

#Funcion para eliminar departamento Delete_depto()
def deleteDepto(deptno):
    try:
        cursor = connection.cursor()

        cursor.callproc("Delete_depto", [deptno])

        connection.commit()
        print("Departamento eliminado con éxito")

    finally:
        cursor.close()
        connection.close()

#Funcion para añadir empleado Add_emp()
def addEmp(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    try:
        cursor = connection.cursor()

        cursor.callproc("Add_emp", [empno, ename, job, mgr, hiredate, sal, comm, deptno])

        connection.commit()
        print("Empleado agregado con éxito")

    finally:
        cursor.close()
        connection.close()

#Funcion para eliminar empleado Delete_emp()
def deleteEmp(empno):
    try:
        # Crear un cursor
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc("Delete_emp", [empno])

        # Confirmar los cambios en la base de datos
        connection.commit()
        print("Empleado eliminado con éxito")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

#Funcion para actualizar empleado Update_emp()
def updateEmp(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    try:
        # Crear un cursor
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc("Update_emp", [empno, ename, job, mgr, hiredate, sal, comm, deptno])

        # Confirmar los cambios en la base de datos
        connection.commit()
        print("Empleado actualizado con éxito")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

#Funcion para obtener el numero de empleados por departamento noEmp_depto()
def noEmpDepto(deptno):
    try:
        # Crear un cursor
        cursor = connection.cursor()

        # Declarar una variable para almacenar el resultado
        num_employees = cursor.var(oracledb.NUMBER)

        # Llamar al procedimiento almacenado
        cursor.callproc("Get_No_Emp_Depto", (deptno, num_employees))

        # Recuperar el resultado del procedimiento
        result = num_employees.getvalue()
        print(f"Número de empleados en el departamento: {result}")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def main():
    print("1.- Añadir el departamento")
    print("2.- Actualizar el departamento")
    print("3.- Eliminar un departamento")
    print("4.- Añadir un empleado")
    print("5.- Eliminar un empleo")
    print("6.- Actualizar un empleado")
    print("7.- Obtener el numero de empleados por departamento")

    opcion = input("Ingrese el numero de opcion que desea hacer: ")

    if (opcion == 1):
        deptno = int(input("Ingrese el numero de departamento: "))
        deptname = input("Ingrese el nombre del departamento: ")
        loc = input("Ingrese la ubicacion del departamento: ")
        addDepto(deptno, deptname, loc)
    elif (opcion == 2):
        deptno = int(input("Ingrese el numero de departamento: "))
        deptname = input("Ingrese el nombre del departamento: ")
        loc = input("Ingrese la ubicacion del departamento: ")
        updateDepto(deptno, deptname, loc)
    elif (opcion == 3):
        deptno = int(input("Ingrese el numero de departamento: "))
        deleteDepto(deptno)
    elif (opcion == 4):
        empno = int(input("Ingrese el numero de empleado"))
        ename = input("Ingrese el nombre: ")
        job = input("Ingrese el trabajo")
        mgr = int(input("Ingese el mgr: "))
        hiredate = input("Ingrese el hire_date: ")
        sal = int(input("Ingrese sal: "))
        comm = int(input("Ingrese el comm: "))
        deptno = int(input("Ingrese el numero de departamento: "))
        addEmp(empno, ename, job, mgr, hiredate, sal, comm, deptno)
    elif (opcion == 5):
        empno = int(input("Ingrese el numero de empleado"))
        deleteEmp(empno)
    elif (opcion == 6):
        empno = int(input("Ingrese el numero de empleado"))
        ename = input("Ingrese el nombre: ")
        job = input("Ingrese el trabajo")
        mgr = int(input("Ingese el mgr: "))
        hiredate = input("Ingrese el hire_date: ")
        sal = int(input("Ingrese sal: "))
        comm = int(input("Ingrese el comm: "))
        deptno = int(input("Ingrese el numero de departamento: "))
        updateEmp(empno, ename, job, mgr, hiredate, sal, comm, deptno)
    elif (opcion == 7):
        deptno = int(input("Ingrese el numero de departamento: "))
        noEmpDepto(deptno)

main()