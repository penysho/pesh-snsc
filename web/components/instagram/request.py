

from web.models import Sns


def create_ig_get_user_url(sns: Sns):
    return f"https://graph.facebook.com/{sns.version}/{sns.account_id}?fields=business_discovery.username({sns.username}){{{"biography,id,followers_count,follows_count,media_count,name,profile_picture_url,username,website"}}}&access_token={sns.token}"
