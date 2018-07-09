from flask import Blueprint, render_template

from .docker_wrap import client


Containers = Blueprint('containers', __name__, url_prefix='/containers')


@Containers.route('/')
def container_list():
    containers = client.containers
    return render_template(
        'containers/list.html', containers=containers,
        docker_command='docker ps')


@Containers.route('/<string:short_id>')
def container_detail(short_id):
    container = client.get_container(short_id)
    return render_template(
        'containers/detail.html', container=container,
        docker_command='docker inspect {}'.format(short_id))
