def get_property_string(file_name):
    props = {}
    with open(file_name, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=')
                props[key.strip()] = value.strip()
    return props
