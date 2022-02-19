import requests


class Oauth:
  client_id = "90614*CENSORED*8811977"
  client_secret = "LKKzqxt2B*CENSORED*QHt4YaVFFg"
  redirect_uri = "https://spirit-box.ursulpolar03.repl.co/acasa"
  scope = "identify%20email%20guilds"
  discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=906142997538811977&redirect_uri=https%3A%2F%2Fspirit-box.ursulpolar03.repl.co%2Facasa&response_type=code&scope=identify%20email%20guilds"
  discord_token_url = "https://discord.com/api/oauth2/token"
  discord_api_url = "https://discord.com/api"

  @staticmethod
  def get_access_token(code):
    payload = {
      "client_id": Oauth.client_id,
      "client_secret" : Oauth.client_secret,
      "grant_type" : "authorization_code",
      "code" : code,
      "redirect_uri" : Oauth.redirect_uri,
      "scope" : Oauth.scope
    }

    access_token = requests.post(url = Oauth.discord_token_url, data = payload).json()

    return access_token.get("access_token")
  
  @staticmethod
  def get_user_json(access_token):
    url = f"{Oauth.discord_api_url}/users/@me"
    headers = {"Authorization": f"Bearer {access_token}"}

    user_object = requests.get(url = url, headers = headers).json()
    return user_object