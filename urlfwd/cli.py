import click 
import yaml
import subprocess

from .genpage import files_from_dict
from .manage_links import add_link,find_duplicate_keys


@click.command
@click.option('-s','--source-yaml',default='links.yml',
              help='file name if not links.yml')
@click.option('-r','--retain',is_flag=True,
              help='retain existing (do not overwrite)')
@click.option('-p','--out-path',default='docs',
              help='path to write files to default docs')
@click.option('-v','--verbose',is_flag=True,
              help='verbose mode, print details')


def generate_links(source_yaml,retain,out_path,verbose):
    '''
    from a yaml source file create a set of toy files with file names as the keys
    and the values as the content of each file

    '''
    # TODO: check file type and use different readers to accepts files other than yaml?

    duplicated_keys = find_duplicate_keys(source_yaml)
    # empty list wil read as false
    if duplicated_keys:
        click.echo('Warning: the following keys are duplicated, only last one will be used:\n   ' +
                    '\n  '.join(duplicated_keys))
    else:
        if verbose:
            click.echo('no duplicate keys')

    # read file 
    with open(source_yaml,'r') as f:
        files_to_create = yaml.safe_load(f)

    overwrite = not(retain)
    # call creator
    log = files_from_dict(files_to_create,overwrite,out_path,logging=verbose)
    if verbose and log:
        click.echo(log)


@click.command
@click.option('-u','--url',prompt='URL to forward to',
              help='url to forward to')
@click.option('-l','--short-link',prompt= 'short name to create',
              help='short name to create')
@click.option('-y','--yaml-file',default='links.yml',
              help='file name if not links.yml')
@click.option('-f','--force',is_flag=True,
              help = 'force to overwrite an existing key')
@click.option('-b','--build',is_flag=True,
              help = 'also rebuild')
@click.option('-c','--commit',is_flag=True,
              help = 'commit and push the links file')


def add_short_link(url,short_link,yaml_file,force,build, commit):
    '''
    add a new link with options or prompting
    '''
    if build:
        message,files_to_create = add_link(url,short_link,yaml_file, force,
                                           return_dict=build)
        files_from_dict(files_to_create)
    else:
        message = add_link(url,short_link,yaml_file, force)
    
    # will return nothing if succeeds with no overwriteing, otherwise print
    if message:
        click.echo(message)

    if commit:
        commit_msg = '"add ' + short_link +'"'
        subprocess.run(['git','add','links.yml'])
        subprocess.run(['git','commit','-m',commit_msg])
        subprocess.run(['git','push'])
