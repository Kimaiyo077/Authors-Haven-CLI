import requests
import json
import click
from .write import writeToJsonFile

url = 'https://ah-premier-staging.herokuapp.com/api/articles/'

@click.group()
def ah():
    '''
    A console application that consumes Author's Haven API and 
    returns an article or a list of articles.

    '''
    pass


@ah.command()
@click.option('--save', default=False, is_flag=True,
                help='save article in a JSON file')
@click.argument('slug', default='slug')
def view(slug, save):
    '''
    Command that allows a user to view a single article and
    have the option to save it to a JSON file.

    '''
    if slug == 'slug':
        click.echo('Please pass article slug as argument to view it.')
    else:
        try: 
            data = requests.get(url + slug)
            if data.status_code != 200:
                data.raise_for_status()
            else:
                article = data.json()
                click.echo(json.dumps(article, indent=4))
                if save:
                    name = slug 
                    writeToJsonFile(name=name, data=article)
        except requests.exceptions.HTTPError as e:
            click.echo("Something went wrong. Please try again ")


@ah.command()
@click.option('--limit', default=2, type=int,
                help='Limit how many articles are displayed')
@click.option('--search', type=str,
                help='Enter name to filter the articles by author')
def list(limit, search):
    '''
    Command that allows users to view all the articles in the database
    and have the option to limit how many they view

    '''
    try: 
        if limit and not search:
            data = requests.get(url + '?page_size=' + str(limit))
        elif search and not limit:
            data = requests.get(url + '?author=' + str(search))
        elif search and limit:
            data = requests.get(url + '?page_size={}&author={}'.format(limit, search) )
        else:
            data = requests.get(url)

        if data.status_code != 200:
            data.raise_for_status()
        else:
            article = data.json()
            click.echo(json.dumps(article, indent=4))
    except requests.exceptions.HTTPError as e:
        click.echo("Something went wrong. Please try again ")
