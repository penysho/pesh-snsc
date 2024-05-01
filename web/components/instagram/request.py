from web.models import SnsApiAccount


def create_ig_get_user_url(sns_api_account: SnsApiAccount):
    return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"biography,followers_count,follows_count,media_count,name,profile_picture_url,website"}}}&access_token={sns_api_account.token}"


def create_ig_get_media_url(sns_api_account: SnsApiAccount):
    return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"media{comments_count,like_count}"}}}&access_token={sns_api_account.token}"
