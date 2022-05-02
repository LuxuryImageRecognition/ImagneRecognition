from image_fetcher import ImageFetcher
import json

with open("bags.json") as bag_conf_file:
    bags_conf = json.loads(bag_conf_file.read())

fetcher = ImageFetcher()

fetcher.make_url("louis vuitton", "alma bag")

fetcher.get_images_links()

fetcher.download_images("images")
