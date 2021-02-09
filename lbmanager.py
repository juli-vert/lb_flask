import yaml
# templates
vip_template = '''
@app.route('/{0}', methods=['GET'])
def {0}():
    {1}
    response = requests.get("http://{{0}}".format(server))
    return response.content
    '''
balancers = {"round-robin" : '''
    servers = {1}
    with open("{0}-token.ini", "r") as fd:
        token = int(fd.read())
    server = servers[token]
    with open("{0}-token.ini", "w") as fd:
        token += 1
        if token < len(servers):
            fd.write(str(token))
        else:
            fd.write('0')
    ''', "random": '''
    from random import randint
    servers = {1}
    token = randint(0,len(servers)-1)
    server = servers[token]
    '''}
def LoadConfig():
    with open("config.yaml", "r") as fd:
        config = fd.read()
        return yaml.load(config, Loader=yaml.FullLoader)

def CreateVip(vip, method, realservers):
    
    with open("lb_vips.py", "a+") as fd:
        if method in balancers.keys():
            newvip = vip_template.format(vip, balancers[method].format(vip, realservers))
            fd.write(newvip)
            if method == "round-robin":
                with open("{0}-token.ini".format(vip), "w") as fd:
                    fd.write('0')


config = LoadConfig()
for uri in config['balancers']:
    real_servers = []
    for s in uri['real-servers']:
        real_servers.append(s['name'])  
    CreateVip(uri['uri'].split("/")[1], uri['type'], real_servers)

from loadbalancer import app
for rule in app.url_map.iter_rules():
    print(rule)
app.run(host="0.0.0.0", port=80)