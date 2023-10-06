import cx_Oracle

# Conexión a la base de datos Oracle
connection = cx_Oracle.connect("usuario/password@localhost/orcl")

# Funciones para agregar, actualizar y eliminar departamentos
def add_depto(deptno, dname, loc):
    cursor = connection.cursor()
    try:
        cursor.callproc("Add_depto", [deptno, dname, loc])
        print("Departamento agregado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al agregar el departamento:", e)
    finally:
        cursor.close()

def update_depto(deptno, dname, loc):
    cursor = connection.cursor()
    try:
        cursor.callproc("Update_depto", [deptno, dname, loc])
        print("Departamento actualizado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al actualizar el departamento:", e)
    finally:
        cursor.close()

def delete_depto(deptno):
    cursor = connection.cursor()
    try:
        cursor.callproc("Delete_depto", [deptno])
        print("Departamento eliminado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al eliminar el departamento:", e)
    finally:
        cursor.close()

# Función para obtener el número de empleados en un departamento
def no_emp_depto(deptno):
    cursor = connection.cursor()
    try:
        result = cursor.callfunc("noEmp_depto", cx_Oracle.NUMBER, [deptno])
        print("Número de empleados en el departamento:", result)
    except cx_Oracle.DatabaseError as e:
        print("Error al obtener el número de empleados:", e)
    finally:
        cursor.close()

# Función para agregar un empleado
def add_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    cursor = connection.cursor()
    try:
        cursor.callproc("Add_emp", [empno, ename, job, mgr, hiredate, sal, comm, deptno])
        print("Empleado agregado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al agregar el empleado:", e)
    finally:
        cursor.close()

# Función para eliminar un empleado
def delete_emp(empno):
    cursor = connection.cursor()
    try:
        cursor.callproc("Delete_emp", [empno])
        print("Empleado eliminado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al eliminar el empleado:", e)
    finally:
        cursor.close()

# Función para actualizar un empleado
def update_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno):
    cursor = connection.cursor()
    try:
        cursor.callproc("Update_emp", [empno, ename, job, mgr, hiredate, sal, comm, deptno])
        print("Empleado actualizado con éxito")
    except cx_Oracle.DatabaseError as e:
        print("Error al actualizar el empleado:", e)
    finally:
        cursor.close()

# Ejemplo de uso
if __name__ == "__main__":
    add_depto(50, 'Ventas', 'Nueva York')
    update_depto(50, 'Ventas Internacionales', 'Los Ángeles')
    delete_depto(50)
    no_emp_depto(10)

# Cerrar la conexión a la base de datos
connection.close()