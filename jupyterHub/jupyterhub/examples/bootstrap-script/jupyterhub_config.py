# Example for a Spawner.pre_spawn_hook
# create a directory for the user before the spawner starts

import os
import shutil
def create_dir_hook(spawner):
    username = spawner.user.name # get the username
    volume_path = os.path.join('/volumes/jupyterhub', username)
    if not os.path.exists(volume_path):
        os.mkdir(volume_path, 0o755)
        # now do whatever you think your user needs
        # ...

def clean_dir_hook(spawner):
    username = spawner.user.name # get the username
    temp_path = os.path.join('/volumes/jupyterhub', username, 'temp')
    if os.path.exists(temp_path) and os.path.isdir(temp_path):
        shutil.rmtree(temp_path)

# attach the hook functions to the spawner
c.Spawner.pre_spawn_hook = create_dir_hook
c.Spawner.post_stop_hook = clean_dir_hook

# Use the DockerSpawner to serve your users' notebooks
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.DockerSpawner.hub_ip_connect = public_ips()[0]
c.DockerSpawner.container_ip = "0.0.0.0"

# You can now mount the volume to the docker container as we've
# made sure the directory exists
c.DockerSpawner.volumes = { '/volumes/jupyterhub/{username}/': '/home/jovyan/work' }

