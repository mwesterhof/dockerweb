from flask import Blueprint, render_template

from docker_wrap import client

Images = Blueprint('images', __name__, url_prefix='/images')


@Images.route('/')
def image_list():
    images = client.images
    return render_template(
        'images/list.html', images=images, docker_command='docker images')


@Images.route('/<string:short_id>')
def image_detail(short_id):
    image = client.get_image(short_id)
    return render_template(
        'images/detail.html', image=image,
        docker_command='docker inspect {}'.format(short_id))
