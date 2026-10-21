from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from flask_app.models.usuario import create_user, get_user_by_email


usuarios = Blueprint("usuarios", __name__)


@usuarios.get("/")
def inicio():
    if session.get("usuario_id"):
        return redirect(url_for("usuarios.bienvenida"))
    return render_template("index.html")


@usuarios.post("/registro")
def registro():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    confirmacion = request.form.get("confirmacion", "")

    if not all((nombre, apellido, email, password, confirmacion)):
        flash("Completa todos los campos del registro.", "error")
    elif password != confirmacion:
        flash("Las contraseñas no coinciden.", "error")
    elif len(password) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.", "error")
    elif get_user_by_email(email):
        flash("Ya existe una cuenta con ese e-mail.", "error")
    else:
        create_user(
            nombre,
            apellido,
            email,
            generate_password_hash(password),
        )
        flash("Registro exitoso. Ya puedes iniciar sesión.", "success")

    return redirect(url_for("usuarios.inicio"))


@usuarios.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = get_user_by_email(email) if email and password else None

    if not usuario or not check_password_hash(usuario["password"], password):
        flash("E-mail o contraseña incorrectos.", "error")
        return redirect(url_for("usuarios.inicio"))

    session.clear()
    session["usuario_id"] = usuario["id"]
    session["nombre"] = usuario["nombre"]
    return redirect(url_for("usuarios.bienvenida"))


@usuarios.get("/bienvenida")
def bienvenida():
    if not session.get("usuario_id"):
        return redirect(url_for("usuarios.inicio"))
    return render_template("bienvenida.html", nombre=session["nombre"])


@usuarios.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("usuarios.inicio"))
