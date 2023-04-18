import docker
import click

client = docker.from_env()

def create_container():
    container_name = input("Digite o nome do container: ")
    image_name = input("Digite o nome da imagem: ")
    command = input("Digite o comando a ser executado: ")
    container = client.containers.create(image_name, command=command, name=container_name)
    click.echo(f"Container {container_name} criado com sucesso!")

def start_container():
    container_name = input("Digite o nome do container: ")
    container = client.containers.get(container_name)
    container.start()
    click.echo(f"Container {container_name} iniciado com sucesso!")

def list_containers():
    containers = client.containers.list()
    click.echo("Lista de containers:")
    for container in containers:
        click.echo(container.name)

def stop_container():
    container_name = input("Digite o nome do container: ")
    container = client.containers.get(container_name)
    container.stop()
    click.echo(f"Container {container_name} parado com sucesso!")

def restart_container():
    container_name = input("Digite o nome do container: ")
    container = client.containers.get(container_name)
    container.restart()
    click.echo(f"Container {container_name} reiniciado com sucesso!")

def remove_container():
    container_name = input("Digite o nome do container: ")
    container = client.containers.get(container_name)
    container.remove()
    click.echo(f"Container {container_name} removido com sucesso!")

def list_images():
    images = client.images.list()
    click.echo("Lista de imagens:")
    for image in images:
        click.echo(image.tags)

def remove_image():
    image_name = input("Digite o nome da imagem: ")
    client.images.remove(image_name)
    click.echo(f"Imagem {image_name} removida com sucesso!")

@click.command()
@click.option('--create', is_flag=True, help='Criar um novo container')
@click.option('--start', is_flag=True, help='Iniciar um container')
@click.option('--list', is_flag=True, help='Listar todos os containers')
@click.option('--stop', is_flag=True, help='Parar um container')
@click.option('--restart', is_flag=True, help='Reiniciar um container')
@click.option('--remove', is_flag=True, help='Remover um container')
@click.option('--list-images', is_flag=True, help='Listar todas as imagens')
@click.option('--remove-image', is_flag=True, help='Remover uma imagem')
def main(create, start, list, stop, restart, remove, list_images, remove_image):
    if create:
        create_container()
    elif start:
        start_container()
    elif list:
        list_containers()
    elif stop:
        stop_container()
    elif restart:
        restart_container()
    elif remove:
        remove_container()
    elif list_images:
        list_images()
    elif remove_image:
        remove_image()

if __name__ == '__main__':
    main()
