import os
import click
import json



def writeToJsonFile(name, data):
    # Create docs directory if it does not exist
    if not os.path.isdir('./docs'):
        os.mkdir('./docs')

    # check if file already exists
    directory = os.getcwd() + '/docs/'+ name + '.json'

    if not os.path.isfile(directory):
        # write new file
        with open(directory, 'w') as savefile:
            json.dump(data, savefile, indent=4)

    else:
        click.echo('File with that name already exists')
    