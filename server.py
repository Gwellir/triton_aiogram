import asyncio

from flask import Flask, request, Response

import config
from main import bot, dp


app = Flask(__name__)


@app.route(config.WEBHOOK_PATH)
def process_webhook():
    print(request)
    if request.method == "POST":
        data = request.get_json(force=True)
        dp.feed_raw_update(bot, data)

    return Response(status=200)


@app.route("/drop_webhook")
def drop_webhook():
    asyncio.run(bot.delete_webhook())