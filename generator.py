from dataclasses import dataclass
import json
import os
import re
from typing import Optional


@dataclass
class OperationParam:
    name: str
    type: str
    desc: str


class Endpoint:
    summary: Optional[str]
    operation_id: str
    tags: list[str]
    parameters: list[dict]
    responses: dict

    def __init__(self, data: dict) -> None:
        self.summary = data.get("summary")
        self.operation_id = data["operationId"]
        self.tags = data.get("tags", [])
        self.parameters = data.get("parameters", [])
        self.responses = data["responses"]


@dataclass
class Path:
    delete: Optional[Endpoint] = None
    get: Optional[Endpoint] = None
    post: Optional[Endpoint] = None
    put: Optional[Endpoint] = None


class Spec:
    info: dict
    servers: list
    paths: dict[str, Path]
    tags: list
    x_tag_groups: list
    components: dict

    def __init__(self, data: dict) -> None:
        self.info = data["info"]
        self.servers = data["servers"]
        self.paths = self.__parse_paths(data["paths"])
        self.tags = data["tags"]
        self.x_tag_groups = data["x-tagGroups"]
        self.components = data["components"]

    def __parse_paths(self, paths: dict[str, dict]) -> dict[str, Path]:
        result = dict()

        for path, data in paths.items():
            result[path] = Path()

            delete = data.get("delete")
            if delete:
                result[path].delete = Endpoint(delete)

            get = data.get("get")
            if get:
                result[path].get = Endpoint(get)

            post = data.get("post")
            if post:
                result[path].post = Endpoint(post)

            put = data.get("put")
            if put:
                result[path].put = Endpoint(put)

        return result


def to_pascal_case(s):
    return "".join(word.capitalize() for word in s.split("_"))


def to_camel_case(s):
    words = re.split(r"[_\s]+", s)
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name.replace("-", "_")).lower()


def to_type(name: str) -> str:
    match name:
        case "integer":
            return "int"
        case "number":
            return "float"
        case "boolean":
            return "bool"
        case "string":
            return "str"
        case "array":
            return "list"
        case "object":
            return "dict"
        case _:
            raise ValueError(f"Unknown type: {name}")


def load_spec(path: str) -> Spec:
    with open(path) as f:
        return Spec(json.load(f))


def generate_operation_params(operation: Endpoint) -> list[OperationParam]:
    params = []

    for param in operation.parameters:
        if "in" not in param:
            continue

        if param["in"] != "path":
            continue

        param_name: str = to_snake_case(param["name"])
        param_type: str = to_type(param["schema"]["type"])
        param_desc: str = param["description"]

        params.append(OperationParam(param_name, param_type, param_desc))

    return params


def generate_operation(
    service_name: str, operation_name: str, operation: Endpoint
) -> str:
    operation_params = generate_operation_params(operation)

    docstring_params = ""
    for param in operation_params:
        if param.name == "self":
            continue

        docstring_params += f"            {param.name} ({param.type}): {param.desc}\n"

    docstring = f'''"""
        {operation.summary}
        
        Args:
{docstring_params}
        """'''

    operation_params_str = str(
        "self, "
        + ", ".join(f"{param.name}: {param.type}" for param in operation_params)
    )

    return f"""
    def {operation_name}({operation_params_str}) -> None:
        {docstring}
    
        print("Calling operation '{operation_name}' of service '{to_pascal_case(service_name)}' ...")
"""


SERVICES: dict[str, dict] = dict()


def generate_service(service_name: str) -> str:
    if service_name not in SERVICES:
        return ""

    operations = ""
    for operation_name in SERVICES[service_name].keys():
        operations += generate_operation(
            service_name,
            operation_name,
            SERVICES[service_name][operation_name],
        )

    return f"""
class {to_pascal_case(service_name)}:
    {operations}
    """


def generate_services(spec: Spec) -> None:
    os.makedirs("dist/services", exist_ok=True)

    for path, endpoint in spec.paths.items():
        service_name = to_snake_case(path.split("/")[1])

        if service_name not in SERVICES:
            SERVICES[service_name] = dict()

        # if service_name != "virtual_hosts":
        #     continue

        for operation_name in endpoint.__annotations__.keys():
            operation = getattr(endpoint, operation_name)
            if operation is None:
                continue

            print(
                f"Generating service '{path}' ... '{service_name}' for operation '{operation_name}'..."
            )

            operation_id = to_snake_case(operation.operation_id)
            SERVICES[service_name][operation_id] = operation

        with open(f"dist/services/{service_name}.py", "w") as f:
            f.write(generate_service(service_name))


def generate_client(spec: Spec) -> None:
    os.makedirs("dist", exist_ok=True)

    generate_services(spec)


## ---- ## ---- ## ---- ##

spec = load_spec("spec.json")
generate_client(spec)
