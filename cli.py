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

from crud import create_vehicle

@cli.command()
@click.option('--make', prompt='Vehicle make')
@click.option('--model', prompt='Vehicle model')
@click.option('--year', prompt='Vehicle year', type=int)
@click.option('--customer-id', prompt='Customer ID', type=int)
def add_vehicle(make, model, year, customer_id):
    vehicle = create_vehicle(make, model, year, customer_id)
    click.secho(f"🚗 Added vehicle: {vehicle.make} {vehicle.model} ({vehicle.year})", fg="green")