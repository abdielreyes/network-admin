from flask import Flask, request, render_template, redirect, url_for
from netmiko import ConnectHandler
import routers

def user_config():
	if request.method == 'GET':
		return render_template("confU.html")
	if request.method == 'POST':
		return "Peticion post"

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