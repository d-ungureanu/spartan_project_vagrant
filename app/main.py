from flask import Flask, request
import management
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@app.route("/", methods=["GET"])
def homepage():
    homepage_content = f"Homepage for AWS + Docker version from server ID:{management.server_id}"
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
@by_path_counter
def remove_spartan():
    id_var = int(request.args.get("id"))
    result = management.delete_from_db(id_var)
    return f"{result}"


@app.route("/spartan", methods=["GET"])
@by_path_counter
def list_spartans():
    spartans_db = management.display_db()
    return f"{spartans_db}"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
    # app.run(debug=True)
