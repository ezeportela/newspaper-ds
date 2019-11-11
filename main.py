import argparse
from common import config, news_sites

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  news_site_choices = list(news_sites().keys())

  parser.add_argument(
    'news_site',
    help='The news site that you want to scrape',
    type=str,
    choices=news_site_choices,
  )

  args = parser.parse_args()
  print('scrape the news site {}'.format(args.news_site))