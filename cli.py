import click
from crud import create_customer

@click.group()
def cli():
    """GaragePro CLI - Manage customers, vehicles, and service records."""
    pass

@cli.command()
@click.option('--name', prompt='Customer name')
@click.option('--phone', prompt='Phone number')
@click.option('--email', prompt='Email')
@click.option('--address', prompt='Address')
def add_customer(name, phone, email, address):
    customer = create_customer(name, phone, email, address)
    click.secho(f"✅ Added customer: {customer.name}", fg="green")