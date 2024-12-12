import urllib.parse as urlparse
from urllib.parse import parse_qs

import queryparams


def get_query_params(url):
    return queryparams.parse(parse_qs(urlparse.urlparse(url).query))


def pydantic_errors_to_request_error(pydantic_errors):
    if isinstance(pydantic_errors, list):
        return {
            "id": "validation_failed",
            "message": "Validation error",
            "meta": {
                "errors": {error["loc"][0]: error["msg"] for error in pydantic_errors}
            },
        }
    return pydantic_errors
