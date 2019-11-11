import yaml

__config = None

def config():
  if not __config:
    with open('config.yaml', 'r') as f:
      config = yaml.load(f, Loader=yaml.SafeLoader)

  return config

def news_sites():
  return config()['news_sites']
