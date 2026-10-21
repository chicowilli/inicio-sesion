import mysql.connector

from flask_app.config.mysqlconnection import get_db_connection


def get_user_by_email(email):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, nombre, apellido, email, password "
            "FROM usuarios WHERE email = %s",
            (email,),
        )
        return cursor.fetchone()
    finally:
        connection.close()


def create_user(nombre, apellido, email, password_hash):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, email, password) "
            "VALUES (%s, %s, %s, %s)",
            (nombre, apellido, email, password_hash),
        )
        connection.commit()
    except mysql.connector.Error:
        connection.rollback()
        raise
    finally:
        connection.close()
