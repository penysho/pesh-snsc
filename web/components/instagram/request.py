from web import models


def create_ig_get_user_url(site: models.Site):
    return f"https://graph.facebook.com/{site.version}/{site.account_id}?fields=business_discovery.username({site.username}){{{"biography,id,followers_count,follows_count,media_count,name,profile_picture_url,username,website"}}}&access_token={site.token}"
