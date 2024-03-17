import click 
import yaml
import os


@click.command
@click.option('-s','--source-yaml',default='links.yml',
              help='file name if not links.yml')


def generate_links(source_yaml):
    '''
    from a yaml source file create a set of toy files with file names as the keys
    and the values as the content of each file

    '''
    # TODO: check file type and use different readers to accepts files other than yaml
    # read file 
    with open(source_yaml,'r') as f:
        files_to_create = yaml.safe_load(f)

    # call creator
    files_from_dict(files_to_create)



def validate():
    '''
    check that what's asked for is not
    '''



pg_html = '''
<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta http-equiv="refresh" content="0; URL={url}" />
    <meta name="author" content="Sarah Brown" />
    <meta property="og:title" content="{name}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta name="description" content="forwarding to {url}"/>
</head>
<body>
This page should forward to <a href="{url}">{url}</a>
</body>
</html>
'''


def files_from_dict(pages_to_create,overwrite=True):
    '''
    given a dictionary, create html files
    
    Parameters
    ----------
    pages_to_create : dictionary
        keys are names of pages, values are urls to redirect to
    
    '''
    for path, url in pages_to_create.items():
        if not(type(path) == str):
            path = str(path)
            
        contents = pg_html.format(url=url,name=path)
        out_path = os.path.join('docs',path)
        # do not create if overwriting and already exists, otherwise create
        if not(overwrite and os.path.exists(out_path)):
            os.mkdir(out_path)

        # write the file out
        with open(os.path.join('docs',path,'index.html'),'w') as f:
            f.write(contents)