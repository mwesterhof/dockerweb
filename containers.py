from flask import Blueprint, render_template

from docker_wrap import client


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


@Containers.route('/<string:short_id>/kill')
def container_kill(short_id):
    container = client.get_container(short_id)
    return render_template(
        'containers/kill.html', container=container,
        docker_command='docker kill {}'.format(short_id))


@Containers.route('/<string:short_id>/kill/confirm')
def container_kill_confirm(short_id):
    container = client.get_container(short_id)
    container.kill()
    containers = client.containers
    return render_template(
        'containers/list.html', containers=containers,
        docker_command='docker ps', messages=['container killed'])
