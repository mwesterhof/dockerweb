import docker


class Image:
    def __init__(self, base_image, client):
        if base_image.tags and base_image.tags[0]:
            self.name = base_image.tags[0]
        else:
            self.name = '<image>'

        self.base_image = base_image
        self.short_id = base_image.short_id
        self.attrs = base_image.attrs
        self.client = client

    @property
    def containers(self):
        return [
            cont
            for cont in self.client.containers
            if cont.image.short_id == self.short_id
        ]

    def __str__(self):
        return self.name


class Container:
    def __init__(self, base_container, client):
        self.base_container = base_container
        self.name = base_container.attrs['Name']
        self.short_id = base_container.short_id
        image_id = base_container.attrs['Image']
        self.image_id = image_id[:image_id.find(':') + 11]
        self.client = client
        self.attrs = base_container.attrs

    @property
    def image(self):
        return self.client.get_image(self.image_id)

    def kill(self):
        self.base_container.kill()

    def __str__(self):
        return self.name


class Client:
    def __init__(self):
        self._wrapped = docker.from_env()
        self.info = self._wrapped.info()
        self.version = self._wrapped.version()

    @property
    def images(self):
        base_images = self._wrapped.images.list()
        return (Image(base_image, self) for base_image in base_images)

    def get_image(self, short_id):
        return Image(self._wrapped.images.get(short_id), self)

    @property
    def containers(self):
        base_containers = self._wrapped.containers.list()
        return (
            Container(base_container, self)
            for base_container in base_containers
        )

    def get_container(self, short_id):
        return Container(self._wrapped.containers.get(short_id), self)


client = Client()
