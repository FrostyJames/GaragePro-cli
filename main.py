import click
from cli import customer_cli, vehicle_cli, service_cli

@click.group()
def main():
    """GaragePro CLI - Main Menu"""
    pass

main.add_command(customer_cli)
main.add_command(vehicle_cli)
main.add_command(service_cli)

if __name__ == "__main__":
    main()