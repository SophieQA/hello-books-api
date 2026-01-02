from flask import Blueprint

hello_world_bp = Blueprint("hello_world_bp", __name__)


@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, World!"


@hello_world_bp.get("/hello/JSON")
def say_hello_json():
    return {
        "name": "Sophie Qiusi",
        "message": "Hello!",
        "hobbies": ["Art", "Golf", "Reading"]
    }


@hello_world_bp.get("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Sophie Qiusi",
        "message": "Hello!",
        "hobbies": ["Art", "Golf", "Reading"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body