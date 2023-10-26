from flask import Flask
import sentry_sdk

sentry_sdk.init(
    dsn="https://6a5b5a1aecb00145519821fcee4e9aac@o4506100000948224.ingest.sentry.io/4506100005470208",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"