from flask import Flask, request, render_template, redirect, url_for
from netmiko import ConnectHandler

def connect_router(routername):
	if request.method == 'GET':
		return render_template("router.html",value=routername)
	if request.method == 'POST':
		metod = request.form['metod']
		usr = request.form['user']
		psw = request.form['password']
		hostname = request.form['hostname']

		if metod == "ssh":
			connect_ssh(hostname,usr,psw,"")
			return redirect(url_for('router_config'))
		elif metod == "telnet":
			print("el metodo es telnet")
			return redirect(url_for('router_config'))
	return redirect(url_for('home'))

def connect_ssh(hostname,user,password,comando):
	router = {
	"device_type": "cisco_ios",
	"host": hostname,
	"username": user,
	"password": password
	}
	net_connect = ConnectHandler(**router)
	output = net_connect.send_config_set(comando)
	return output

def router_config():
	if request.method == 'GET':
		return render_template("routerSuccess.html")

def routing_config():
	if request.method == 'GET':
		return render_template("confR.html")
	if request.method == 'POST':
		return "Peticion post"

def routing_add():
	if request.method == 'GET':
		return render_template("newRouting.html")
	if request.method =='POST':
		if request.form['routing-config'] == 'Configurar RIP':
			num = request.form['number']
			numInt = int(num)
			#commandos = ["router rip", "version 2"]
			for x in range(numInt):
				comandos = ["router rip", "version 2",'net '+request.form['dir'+f'{x}'],"no auto-summary","exit"]
				resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
				print(resultado)
			return "Configuracion exitosa de RIP"
		if request.form['routing-config'] == 'Configurar OSPF':
			num = request.form['number2']
			numInt = int(num)
			for x in range(numInt):
				comandos = ["router ospf 1", "network "+request.form['dir2'+f'{x}']+" "+
				request.form['mask'+f'{x}']+" area "+request.form['area'+f'{x}'], "exit"] 
				resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
				print(resultado)
			return "Configuracion exitosa de OSPF"

def routing_edit():
	if request.method == 'GET':
		comandos = ["exit", "show ip protocol"]
		resultado = connect_ssh("10.0.1.254","cisco","cisco",comandos)
		if "Routing Protocol" in resultado:
			noti = "Se han encontrado protocolos de enrutamiento"
			protocol_info = resultado.split("\n")
			routing_protocols_data = [x for x in protocol_info if x.startswith("Routing Protocol")]
			protocols_in_router = []
			for prot in routing_protocols_data:
				temp_p = prot.split(" ")[3]
				temp_p = temp_p.replace("\r", "")
				temp_p = temp_p.replace("\"", "")
				protocols_in_router.append(temp_p)
			protocolos = f"Protocolos encontrados: {', '.join(protocols_in_router)}"
			print(f"Protocolos encontrados: {', '.join(protocols_in_router)}")
		else:
			noti = "NO se han encontrado protocolos de enrutamiento"
		return render_template("editRouting.html", value = noti, protocolos = protocolos)
	elif request.method == 'POST':
		print("-----------------")
		num0 = request.form['number0'] #numero de las interfaces rip
		num1 = request.form['number1'] #numero de las interfaces ospf
		print("INterfaces rip: "+num0+"  INterfaces ospf = "+num1)
	return "Modificacion exitosa"	

	