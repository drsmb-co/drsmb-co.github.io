import yaml

def find_duplicate_keys(source_yaml):
    '''
    find any duplicated keys in the source yaml

    Parameters
    ----------
    source_yaml : string or file buffer
        file to parse

    Returns
    -------
    duplicates: list
        list of repeated keys; empty if none
    '''
    #yaml reading drops duplicates, keeps only the last one. 
    with open(source_yaml,'r') as f:
        yaml_dict = yaml.safe_load(f)

    with open(source_yaml,'r') as f:
        yaml_list = f.readlines()

    # lengths will match if well formated and no repeats
    if len(yaml_dict) ==len(yaml_list):
        return []
    else:
        key_list = [key_val.split(':')[0] for key_val in yaml_list]
        # cast to set removes duplicates
        duplicates = set([key for key in key_list if key_list.count(key) >1])
        return list(duplicates)
    



def add_link(new_url,new_name,yaml_file, force=False,return_dict =False):
    '''
    add a new key to the yaml file

    Parameters:
    -----------
    new_url : string
        URL to forward to, value in yaml file
    new_name: string
        short url to create, key in yaml file
    yaml_file : string or file buffer
        file to add to
    force: boolean
        if true change a value for an existing key
    '''


    with open(yaml_file,'r') as f:
        link_dict = yaml.safe_load(f)

    if  new_name in link_dict.keys():
        if not(force):
            message = new_name + ' exists, not creating'
            write = False
        else:
            message = new_name + ' exists, overwriting'
            write = True
    else:
        write = True
        message = ''

    if write: 
        link_dict[new_name] = new_url

        text_out = yaml.dump(link_dict)
        with open(yaml_file,'w') as f:
             f.write(text_out)

    if return_dict:
        return message, link_dict
    else:
        return message