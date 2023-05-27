import subprocess
from colorama import init, Fore, Back, Style

def execute_commands(final_name):
    project_env = "devel.yaml"
    base_de_datos = input(f"{Fore.YELLOW}Data Base:{Style.RESET_ALL} ")
    filestore_db = input(f"{Fore.YELLOW}Filestore Data Base:{Style.RESET_ALL} ")
    backup_file = final_name
    container = subprocess.check_output("docker-compose ps -q odoo", shell=True, text=True).strip()

    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo mkdir -p /var/lib/odoo/filestore', shell=True)
    subprocess.run(f'docker cp ../backups/{backup_file}.sql {container}:/var/lib/odoo/filestore/', shell=True)
    subprocess.run(f'docker cp ../backups/filestore_{backup_file}.tar.gz {container}:/var/lib/odoo/filestore/', shell=True)

    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo rm -rf /var/lib/odoo/filestore/{filestore_db}', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo tar zxvf /var/lib/odoo/filestore/filestore_{backup_file}.tar.gz --directory=/var/lib/odoo/filestore/', shell=True)

    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo mv /var/lib/odoo/filestore/var/lib/odoo/filestore/{filestore_db} /var/lib/odoo/filestore/{base_de_datos}', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo rm -rf /var/lib/odoo/filestore/var', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} stop odoo', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo dropdb {base_de_datos}', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo psql -l', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo createdb {base_de_datos}', shell=True)

    subprocess.run(f'docker-compose -f ../{project_env} run --rm odoo psql -d {base_de_datos} -f /var/lib/odoo/filestore/{backup_file}.sql', shell=True)
    subprocess.run(f'docker-compose -f ../{project_env} start odoo', shell=True)
