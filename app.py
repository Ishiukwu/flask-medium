from flask import Flask, render_template, jsonify

app = Flask(__name__)


jobs = [
    {
    "id": 1,
    "title": "Software Engineer",
    "location": "Remote",
    "wage": "$100k - $120k",
    },
    {
        "id": 2,
        "title": "Backend Engineer",
        "location": "Hong Kong",
        "wage": "$130k - $150k",
        },
    {
        "id": 3,
        "title": "Data Analyst",
        "location": "San Francisco",
        "wage": "$100k - $120k",
        },
    {
        "id": 4,
        "title": "Product Designer",
        "location": "Lagos",
        "wage": "$100k - $120k",
        },
]

@app.route("/")
def index():
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def api_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)