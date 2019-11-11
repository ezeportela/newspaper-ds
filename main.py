import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument(
    'news_site',
    help='The news site that you want to scrape',
    type=str,
  )

  args = parser.parse_args()
  print('scrape the news site {}'.format(args.news_site))