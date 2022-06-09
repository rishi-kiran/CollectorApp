from flask import Flask, render_template, request, flash
import sqlite3
from sqlite3 import Error
import logging

def dbconnect():
    try:
       cnx = sqlite3.connect('db/collector.db')
    except Error as e:
       print(e)
       logging.error("Database connection error")
       return 'error'
    return cnx


def select():
    cnx = dbconnect()

    cursor = cnx.cursor()

    query = ("SELECT Id, Name, Type, Value, Term, AcademicYear from CampusInformation")

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()
    return data

def selectid(id):
    cnx = dbconnect()
    cursor = cnx.cursor()

    query = ("SELECT Name, Type, Value, Term, AcademicYear from CampusInformation where Id=?")

    cursor.execute(query,id)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()
    return data
   

def insert(values):
   try:
      cnx = dbconnect()
      cnx.text_factory = sqlite3.OptimizedUnicode
      cursor = cnx.cursor()

      campus_info = ("INSERT INTO CampusInformation"
                  "(Name, AcademicYear, Term, Type, Value) "
                  "VALUES (?, ?, ?, ?, ?)")

      entities = (values[0], values[1], values[2], values[3], values[4])

      # Insert campus info
      cursor.execute(campus_info, entities)

      # Make sure data is committed to the database
      cnx.commit()

      cursor.close()
      cnx.close()
      return 'Added Successfully'
   except Error as e:
      cnx.close()
      return(e)

def update(values):
   try:
      cnx = dbconnect()
      cnx.text_factory = sqlite3.OptimizedUnicode
      cursor = cnx.cursor()

      campus_info = ("UPDATE CampusInformation SET Name=?, AcademicYear=?,Term=?,Type=?,Value=? where Id=?")

      entities = (values[0], values[1], values[2], values[3], values[4], values[5])

      # Insert campus info
      cursor.execute(campus_info, entities)

      # Make sure data is committed to the database
      cnx.commit()

      cursor.close()
      cnx.close()
      return 'Updated Successfully'
   except Error as e:
      cnx.close()
      return(e)


