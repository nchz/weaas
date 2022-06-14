import os

import flask
import gensim


if (LANG := os.getenv("LANG")) is None:
    raise RuntimeError("Env var LANG must be defined.")

app = flask.Flask(f"weaas_{LANG}")
model = gensim.models.fasttext.load_facebook_vectors(
    f"/weaas/models/{LANG}.bin",
    encoding="latin-1",
)


@app.post("/find_similar")
def find_similar():
    body = flask.request.get_json(True)
    word = body["word"]
    topn = body.get("topn", 10)
    r = model.similar_by_word(word, topn=topn)
    result = [{"word": w, "sim": float(s)} for w, s in r]
    return {"result": result}


@app.post("/compare")
def compare():
    body = flask.request.get_json(True)
    w1, w2 = body["words"]
    s = model.similarity(w1, w2)
    return {"result": {"sim": float(s)}}


@app.post("/_model/<func_name>")
def _model(func_name):
    if (f := getattr(model, func_name, None)) is None:
        return ("Error in func_name", 490)

    body = flask.request.get_json(True)
    try:
        result = [f(**kw) for kw in body["kwargs"]]
    except Exception:
        return ("Error in result", 491)

    result = [_try_float(r) for r in result]
    return {"result": result}


@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    return ("salve!", 476)


def _try_float(x):
    if type(x) is dict:
        return {k: _try_float(v) for k, v in x.items()}
    elif hasattr(x, "__iter__") and type(x) is not str:
        return [_try_float(i) for i in x]
    else:
        try:
            return float(x)
        except ValueError:
            return x
