class Codec:
    def __init__(self):
        self.url_mapping = {}
        self.counter = 0
        self.domain = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        self.url_mapping[str(self.counter)] = longUrl
        return self.domain + str(self.counter)

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split('/')[-1]
        return self.url_mapping.get(key, "")