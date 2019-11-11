import yaml

__config = None

def config():
  if not __config:
    with open('config.yaml', 'r') as f:
      config = yaml.load(f, Loader=yaml.SafeLoader)

  return config

def get_news_sites():
  return config()['news_sites']

def get_news_site(uid):
  return config()['news_sites'][uid]
