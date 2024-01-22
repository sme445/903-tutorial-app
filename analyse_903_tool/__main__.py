import pandas as pd 
import click

from analyse_903_tool.utils import read_data, ingress, gender_count, child_count

@click.command()
@click.argument("filepath", required=True)
def run_app(filepath):
    # TODO write docstring
    #filepath = "https://raw.githubusercontent.com/data-to-insight/csc-validator-be-903/main/tests/fake_data/header.csv"
    df = read_data(filepath)
    df_ingress = ingress(df)

    male, female = gender_count(df_ingress)
    counts = child_count(df_ingress)

    click.echo(f'Total Unique Children: {counts}')
    click.echo(f'Total Male: {male}')
    click.echo(f'Total Female: {female}')
if __name__=='__main__':
    run_app()