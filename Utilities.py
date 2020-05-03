import xmltodict
import json


def import_file(file, file_type="json", xml_prefix=""):
    if file_type == "json":
        with open(file) as f:
            return json.load(f)
    elif file_type == "xml":
        with open(file) as f:
            return xmltodict.parse(f.read())[xml_prefix]
