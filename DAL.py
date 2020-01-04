import mysql.connector
import ToDo2 as GUI
import re

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "11551155", database = "todo")

mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)

mycursor.execute("select * from tasks")


def create_task(name,parent):

	mycursor.execute("INSERT INTO tasks (name, parent) VALUES (%s, %s)", (name, parent))
	mydb.commit()

	mycursor.execute("select * from tasks")

	for i in mycursor:
		print(i)

def display_tasks(self):
	self.listWidget.clear()
	mycursor.execute("select name from tasks")
	self.listWidget.addItems([str (i) for i in mycursor])

def display_parent_tasks(name1):
	mySql_insert_query = "SELECT parent FROM tasks WHERE name = %s"
	values = (name1)
	parent = cursor.execute(mySql_insert_query, values) #not done

def display_sub_tasks(name1):
	mySql_insert_query = "SELECT * FROM %s"
	values = (name1)
	parent = cursor.execute(mySql_insert_query, values)
	
def display_tables(self):
	self.listWidget.clear()
	mycursor.execute("select name from tasks")
	result = mycursor.fetchall()
	self.listWidget.addItems(result)

def delete_table(name1):
	#sql_Delete_query = "DROP TABLE %s"%(name1)
	
	mycursor.execute("DROP TABLE %s"%name1)
	mydb.commit()

def delete_task(name1):
	mySql_insert_query = "DELETE FROM tasks WHERE name = %s"
	values = (name1)
	mycursor.execute(mySql_insert_query, values)
	mydb.commit()

def create_table(name1, parent):
	name = (re.findall(r"'(.*?)'", name1))
	#create table
	mycursor.execute("CREATE TABLE %s (name VARCHAR(255), parent VARCHAR(255))"%name)
	#table_name = (name)
	#mycursor.execute("CREATE TABLE task (name varchar(255) PRIMARY KEY, parent varchar(255)")
	#mycursor.execute(sql_CreateTable_query, table_name)
	mydb.commit()

	#fill table
	mySql_insert_query = "INSERT INTO %s (name, parent) VALUES (%s, %s)"
	values = (name1, name1, parent)
	mycursor.execute(mySql_insert_query, values)
	mydb.commit()


def fill_table(name1, parent):
	mySql_insert_query = "INSERT INTO tasks (name, parent) VALUES (%s, %s)"
	values = (name1, parent)
	mycursor.execute(mySql_insert_query, values)
	mydb.commit()


	


