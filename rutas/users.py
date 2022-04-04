from flask import Flask, request, render_template, redirect, url_for
from netmiko import ConnectHandler
from rutas.routers import connect_ssh

def user_config():
	if request.method == 'GET':
		return render_template("confU.html")

def user_add():
	if request.method == 'GET':
		return render_template("newUser.html")
	if request.method =='POST':
		usr = request.form['nameUser']
		con = request.form['passUser']
		comandos = ["username "+usr+" privilege 15 password "+con]
		resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
		print(resultado)
	return "Usuario registrado exitosamente"

def user_edit():
	if request.method == 'GET':
		return render_template("editUser.html")
	if request.method =='POST':
		usr = request.form['nameUser']
		con = request.form['passUser']

		newUsr = request.form['newNameUser']
		newCon = request.form['newPassUser']

		comandos = ["no username "+usr+" privilege 15 password "+con]
		resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
		print(resultado)

		comandos2 = ["username "+newUsr+" privilege 15 password "+newCon]
		resultado2 = connect_ssh("10.0.1.254","cisco","cisco",comandos2)
		print(resultado2)
	return "Cambios exitosos"

def user_remove():
	if request.method == 'GET':
		return render_template("removeUser.html")
	if request.method =='POST':
		usr = request.form['nameUser']
		con = request.form['passUser']
		comandos = ["no username "+usr+" privilege 15 password "+con]
		resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
		print(resultado)
	return "Usuario registrado exitosamente"