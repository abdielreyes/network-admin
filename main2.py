from flask import Flask, request, render_template, redirect, url_for
from rutas.routers import connect_router, router_config, routing_config, routing_add, routing_edit
from rutas.users import user_config, user_add

app = Flask(__name__)

app.add_url_rule('/routers/<routername>', "connect_router", connect_router, methods=["GET","POST"])
app.add_url_rule('/routers/config', "router_config", router_config, methods=["GET"])
app.add_url_rule('/routers/confRouting', "routing_config", routing_config, methods=["GET"])
app.add_url_rule('/routers/confRoutingAdd', "routing_add", routing_add, methods=["GET", "POST"])
app.add_url_rule('/routers/confRoutingEdit', "routing_edit", routing_edit, methods=["GET", "POST"])
app.add_url_rule('/users/confUser', "user_config", user_config, methods=["GET"])
app.add_url_rule('/users/confUserAdd', "user_add", user_add, methods=["GET", "POST"])


@app.route("/")
def home():
    return render_template("/index.html")


"""commands = ['ip route 10.0.5.0 255.255.255.0 10.0.2.253', 'router rip', 'version 2','net 10.0.3.0', 
            'no auto-summary','router ospf 1', 'net 10.0.4.0 0.0.0.255 area 0', 'exit',
            "router rip", "ver 2", "redistribute static","redistribute connected", "redistribute ospf 1 metric 1", 
            "router ospf 1", 
            "redistribute static subnets", "redistribute rip subnets", "end"
            ]

def index():
    if request.method == 'POST':
        usr = request.form['user']
        psw = request.form['password']
        hostname = request.form['hostname']
        return redirect(url_for('exito', usr = usr, psw = psw, hostname = hostname))
    return render_template("/index.html")

@app.route("/exito")
def exito():
    usr = request.args.get('usr',None)
    psw = request.args.get('psw',None)
    hostname = request.args.get('hostname',None)

    router= {
    'device_type': 'cisco_ios',
    'host': hostname,
    'username': usr,
    'password': psw,
    }
    net_connect = ConnectHandler(**router)
    output = net_connect.send_config_set(commands)
    print(output)
    return render_template("exito.html",usr = usr, psw = psw, hostname = hostname)"""

if __name__ == "__main__":
    app.run(debug=True)
