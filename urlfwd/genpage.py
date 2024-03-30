import os





pg_html = '''
<!DOCTYPE html>
<html lang="en-US">
<head>
    <title>redirecting to {url}</title>
    <meta http-equiv="refresh" content="0; URL={url}" />
    <meta name="author" content="Sarah Brown" />
    <meta property="og:title" content="{name}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta name="description" content="forwarding to {url}"/>
    <link rel="canonical" href="{url}"/>
</head>
<body>
This page should forward to <a href="{url}">{url}</a>
</body>
</html>
'''


def files_from_dict(pages_to_create,overwrite=True,base_path='docs',logging=False):
    '''
    given a dictionary, create html files
    
    Parameters
    ----------
    pages_to_create : dictionary
        keys are names of pages, values are urls to redirect to
    
    '''
    if logging:
        log = []
    for path, url in pages_to_create.items():
        # handle case of numbers in key
        if not(type(path) == str):
            path = str(path)

        contents = pg_html.format(url=url,name=path)
        out_dir = os.path.join(base_path,path)
        out_file = os.path.join(out_dir,'index.html')
        # do not create if overwriting and already exists, otherwise create 
        #        (will error if exists and not overwriting)
        if not(os.path.exists(out_dir)):
            os.mkdir(out_dir)
            if logging:
                log.append('creating ' + out_dir)

        if logging and os.path.exists(out_file):
            log.append(path + ' exists')

        # write the file out
        if overwrite or not(os.path.exists(out_file)):
            with open(out_file,'w') as f:
                f.write(contents)
            if logging:
                log.append('writing' + out_file)

    # do at end
    if logging:
        # with open(os.path.join(out_dir,'log.txt'),'w') as f:
        #     f.write('\n'.join(log))
        return '\n'.join(log)
    else:
        return ''