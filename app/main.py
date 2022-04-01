from flask import Flask, request
import management

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    homepage_content = """homePAGE for Vagrant Docker version
    
    
1-  method: GET, route: / This is the landing page (Home page). 
    It should return a welcome message along with a simple tutorial clarifying how APIs can be used

2-  method: POST, route: /spartan/add 
    This API should allow the user to add new spartan to the system by passing a JSON object.

3-  method: GET, route: /spartan/<spartan_id> 
    Get certain employee using the spartan_id. 
    An error message should be returned if the spartan_id doesn't exist in the system. 
    The data should be returned as string

4-  method: POST, route: /spartan/remove?id=sparta_id 
    This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string

5- method: GET, route: /spartan 
This API should return the spartan list as one JSON object."""
    return homepage_content


@app.route("/spartan/add", methods=["POST"])
def spartan_add():
    result = management.add_to_db()
    return f"{result}"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def spartan_getter(spartan_id):
    data = management.spartan_info(spartan_id)
    return data


@app.route("/spartan/remove", methods=["POST"])
def remove_spartan():
    id_var = int(request.args.get("id"))
    result = management.delete_from_db(id_var)
    return f"{result}"


@app.route("/spartan", methods=["GET"])
def list_spartans():
    spartans_db = management.display_db()
    return f"{spartans_db}"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
    # app.run(debug=True)
