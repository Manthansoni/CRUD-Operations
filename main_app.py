'''
    Python with SQL
'''
# Importing module
import mysql.connector
import streamlit as st
import pandas as pd

# Decorator function


def connection_db(func):

    def inner(*args, **kwargs):
        # Creating connection object
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bacancytask"
        )

        mycursor = mydb.cursor()

        val = func(*args, **kwargs, mycursor=mycursor, mydb=mydb)

        mycursor.close()
        mydb.close()
        return val

    return inner

# Other functions


@connection_db
def insert_data(name, field, pnum, mycursor, mydb):
    '''
        Insert Data into Table
    '''
    qry1 = "INSERT INTO task1 VALUES (' ',%s, %s,%s)"
    val = (name, field, pnum)

    exec = mycursor.execute(qry1, val)

    mydb.commit()

    return (f'{mycursor.rowcount} detail inserted')


@connection_db
def update_data(name, field, pnum, mycursor, mydb):
    '''
        Update Data into Table
    '''
    qry2 = "UPDATE task1 SET field = (%s), pNum = (%s)  WHERE name =(%s)"
    val = (field, pnum, name)
    mycursor.execute(qry2, val)
    mydb.commit()

    return "details updated"


@connection_db
def delete_data(id, mycursor, mydb):
    '''
        Delete User Details
    '''
    qry3 = "DELETE FROM task1 WHERE id = (%s)"
    val = [id]
    mycursor.execute(qry3, val)
    mydb.commit()

    return "details deleted"


@connection_db
def view_data(mycursor, mydb):
    '''
        View Table Data
    '''
    mycursor.execute("Select * from task1")
    myresult = mycursor.fetchall()

    # for i in myresult:
    #     st.write(i)
    if len(myresult) > 0:
        table_data = [[myresult[i][x]
                       for x in range(len(myresult[0]))] for i in range(len(myresult))]
        dataframe = pd.DataFrame(table_data, columns=(
            "id", "Name", "Field", "Contact Number"))
        st.table(dataframe)
    else:
        st.write("No data available table")


@connection_db
def search_data(name, mycursor, mydb):
    '''
        Search Table Data
    '''
    mycursor.execute(
        "Select * from task1 Where id = (%s) OR name = (%s) OR field = (%s) OR pNum = (%s);", [name, name, name, name])
    myresult = mycursor.fetchall()

    # for i in myresult:
    #     st.write(i)
    if len(myresult) > 0:
        table_data = [[myresult[i][x]
                       for x in range(len(myresult[0]))] for i in range(len(myresult))]
        dataframe = pd.DataFrame(table_data, columns=(
            "id", "Name", "Field", "Contact Number"))
        st.table(dataframe)
    else:
        st.write("Data not found")


# Streamlit Code Starts here
# Insert Details
st.header("Insert Details")
name1 = st.text_input("Your name", key="name1")
field1 = st.text_input("Your field", key="field1")
number1 = st.number_input("Your number", key="number1")

if st.button("Insert Details"):
    st.write(insert_data(name1, field1, number1))


# Update Data
st.header("Update Details")
name2 = st.text_input("Your name", key="name2")
field2 = st.text_input("Your field", key="field2")
number2 = st.number_input("Your number", key="number2")

if st.button("Update Details"):
    st.write(update_data(name2, field2, number2))

st.header("Delete Details")
id1 = st.text_input("Id to delete", key="id1")

if st.button("Delete Details"):
    st.write(delete_data(id1))

st.header("Search Details")
name3 = st.text_input("Enter any details to search", key="name3")
if name3:
    search_data(name3)

st.header("View Details")
if st.button("View Data"):
    view_data()


if st.button("Clear"):
    st.empty()
