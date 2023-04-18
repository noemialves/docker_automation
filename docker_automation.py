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

@click.command()
@click.option('--create', is_flag=True, help='Criar um novo container')
@click.option('--start', is_flag=True, help='Iniciar um container')
@click.option('--list', is_flag=True, help='Listar todos os containers')
def main(create, start, list):
    if create:
        create_container()
    elif start:
        start_container()
    elif list:
        list_containers()

if __name__ == '__main__':
    main()
