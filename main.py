from sanic import Sanic
from sanic.response import json,file

app = Sanic("Crack_detection_system")


@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.route("/file")
async def query_string(request):
    # return json({"parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string})
    return await file('./static/'+str(request.args["file"][0]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
