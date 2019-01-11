import click
import shutil


@click.option('-n', '--name', help='Unit name')
def delete_unit(name: str):
    # Define vars
    unit_path = f'./src/units/{name}'

    # Remove unit
    shutil.rmtree(unit_path)

    # Remove record
    content = open('./src/plugins/restplus.py').read()
    content = content.replace(restplus_record.format(name, name.lower()), '')
    open('./src/plugins/restplus.py', 'w').write(content)


restplus_record = \
'''from src.units.{0}.namespace import {1}
restplus.add_namespace({1})
'''
