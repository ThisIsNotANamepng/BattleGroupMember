from flask import Flask, request

app = Flask(__name__)

def getData():
    # Returns a dictionary with the data for the ship (id, name, type)

    f = open('roster.txt', 'r')
    roster = f.readlines()
    f.close()

    # If the file ends without a newline then roster[2] doesn't need to be cut
    return {'id': roster[0][0:-1], 'name': roster[1][0:-1], 'type': roster[2]}

global registeredIDs
global registeredTypes

registeredIDs = []
registeredTypes = []
registeredIPs = []


@app.route('/exists', methods=['GET', 'POST'])
def hello():
    # Endpoint for checking if the ip belongs to something

    return 'Exists'

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registers a ship with its provided information if its not registers. Returns its own roster to the registering ship
    
    global registeredIDs
    global registeredTypes

    if request.method == 'POST':
        id = request.values.get('id')
        type = request.values.get('type')
        print(id, type)

        if id == None:
            return "Missing id"
        elif type == None:
            return "Missing type"
        
        if id not in registeredIDs:
            registeredIDs.append(id)
            registeredTypes.append(type)
            registeredIPs.append(request.remote_addr)

        print(registeredIDs)
    
    else:
        print(request.values)
        return 'Invalid request method'
    
    return getData()


app.run(host='0.0.0.0', port=5000)