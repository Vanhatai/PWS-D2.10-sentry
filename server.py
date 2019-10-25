import os
import sentry_sdk
from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

# sentry_sdk.init(
#     dsn="https://a847e1d62c8943018892da06f9ba6a44@sentry.io/1794679",
#     integrations=[BottleIntegration()]
# )

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[BottleIntegration()]
)

@route('/success')
def success():
    # response.status = 200
    return "OK"


@route("/fail")
def fail():
    # response.status = 500
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
