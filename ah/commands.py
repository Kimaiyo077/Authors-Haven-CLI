import requests
import click

url = 'https://ah-premier-staging.herokuapp.com/api/articles/'
@click.group()
def ah():
    pass


@click.command()
@click.argument('slug', default='slug')
@click.argument('write', type=click.File('w'), required= False)
def view(slug, write):
    if slug == 'slug':
        click.echo('Please enter an articles slug to view it.')
    else:
        data = requests.get(url + slug)
        if data.status_code != 200:
            click.echo('There was an error when getting the article. Please try again')
        else:
            click.echo(data.article, file=write)


@click.command()
def list():
    pass