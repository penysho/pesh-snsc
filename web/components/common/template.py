from web.apps import WebConfig


def get_template_name(file_name: str) -> str:
    return f"{WebConfig.name}/{file_name}"
