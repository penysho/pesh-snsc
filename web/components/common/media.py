def get_media_extension_by_url(url: str):
    return url.split("?")[0].split("/")[-1].split(".")[-1]
