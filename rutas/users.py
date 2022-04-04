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

#def user_edit():

#def user_remove():