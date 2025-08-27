import click
from crud import (
    create_customer, create_vehicle, log_service,
    view_service_history, filter_vehicles,
    update_customer, update_vehicle, update_service,
    delete_customer_by_id, delete_vehicle_by_id, delete_service_by_id
)

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

@cli.command()
@click.option('--make', prompt='Vehicle make')
@click.option('--model', prompt='Vehicle model')
@click.option('--year', prompt='Vehicle year', type=int)
@click.option('--customer-id', prompt='Customer ID', type=int)
def add_vehicle(make, model, year, customer_id):
    vehicle = create_vehicle(make, model, year, customer_id)
    click.secho(f"🚗 Added vehicle: {vehicle.make} {vehicle.model} ({vehicle.year})", fg="green")

@cli.command(name="log-service")
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
@click.option('--service-type', prompt='Service type')
@click.option('--notes', prompt='Service notes')
@click.option('--cost', prompt='Service cost', type=float)
@click.option('--date', default=None, help='Optional service date (YYYY-MM-DD)')
def log_service_cmd(vehicle_id, service_type, notes, cost, date):
    service = log_service(service_type, notes, cost, vehicle_id, date)
    click.secho(f"🛠️ Logged service: {service.service_type} on {service.date}", fg="green")



@cli.command(name="view-history")
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
def view_history(vehicle_id):
    records = view_service_history(vehicle_id)
    if not records:
        click.secho("No service records found.", fg="yellow")
        return
    for r in records:
        click.echo(f"{r.date} - {r.service_type} - KES {r.cost} - {r.notes}")

@cli.command(name="filter-vehicles")
@click.option('--make', default=None, help='Filter by vehicle make')
@click.option('--model', default=None, help='Filter by vehicle model')
@click.option('--year', default=None, type=int, help='Filter by manufacture year')
def filter_vehicles_cmd(make, model, year):
    """Filter vehicles by make, model, or year."""
    results = filter_vehicles(make, model, year)

    if not results:
        click.secho("❌ No matching vehicles found.", fg="yellow")
        return

    click.secho("🔍 Matching Vehicles:", fg="cyan")
    for vehicle, customer in results:
        click.echo(
            f"- ID: {vehicle.id} | {vehicle.make} {vehicle.model} ({vehicle.year}) | Owner: {customer.name}"
        )


@cli.command(name="update-customer")
@click.option('--customer-id', prompt='Customer ID', type=int)
@click.option('--name', default=None)
@click.option('--phone', default=None)
@click.option('--email', default=None)
@click.option('--address', default=None)
def update_customer_cmd(customer_id, name, phone, email, address):
    customer = update_customer(customer_id, name, phone, email, address)
    if customer:
        click.secho("✅ Customer updated.", fg="green")
    else:
        click.secho("❌ Customer not found.", fg="red")

@cli.command(name="update-vehicle")
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
@click.option('--make', default=None)
@click.option('--model', default=None)
@click.option('--year', default=None, type=int)
def update_vehicle_cmd(vehicle_id, make, model, year):
    vehicle = update_vehicle(vehicle_id, make, model, year)
    if vehicle:
        click.secho("✅ Vehicle updated.", fg="green")
    else:
        click.secho("❌ Vehicle not found.", fg="red")

@cli.command(name="update-service")
@click.option('--service-id', prompt='Service ID', type=int)
@click.option('--type', default=None)
@click.option('--notes', default=None)
@click.option('--cost', default=None, type=float)
@click.option('--date', default=None)
def update_service_cmd(service_id, type, notes, cost, date):
    service = update_service(service_id, type, notes, cost, date)
    if service:
        click.secho("✅ Service record updated.", fg="green")
    else:
        click.secho("❌ Service record not found.", fg="red")


@cli.command(name="delete-customer")
@click.option('--customer-id', prompt='Customer ID', type=int)
def delete_customer(customer_id):
    if delete_customer_by_id(customer_id):
        click.secho("🗑️ Customer deleted.", fg="green")
    else:
        click.secho("❌ Customer not found.", fg="red")

@cli.command(name="delete-vehicle")
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
def delete_vehicle(vehicle_id):
    if delete_vehicle_by_id(vehicle_id):
        click.secho("🗑️ Vehicle deleted.", fg="green")
    else:
        click.secho("❌ Vehicle not found.", fg="red")

@cli.command(name="delete-service")
@click.option('--service-id', prompt='Service ID', type=int)
def delete_service(service_id):
    if delete_service_by_id(service_id):
        click.secho("🗑️ Service record deleted.", fg="green")
    else:
        click.secho("❌ Service record not found.", fg="red")