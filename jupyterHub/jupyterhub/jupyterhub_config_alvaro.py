# spawn with Docker

c = get_config()

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.ssl_key = '/etc/ssl/private/alvaro-selfsigned.key'
c.JupyterHub.ssl_cert = '/etc/ssl/private/alvaro-selfsigned.crt'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_connect_ip = '10.100.0.86'
c.JupyterHub.port = 443
c.JupyterHub.extra_host_config = { 'network_mode': 'host' }
c.JupyterHub.hub_prefix = '/hub/'


c.DockerSpawner.image = 'mikebirdgeneau/jupyterlab:alvaro'
c.DockerSpawner.remove_containers = True
c.DockerSpawner.hub_ip_connect = '10.100.0.86'


c.Authenticator.whitelist = {'alvaro'}
c.Spawner.default_url = '/lab'
#c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--no-include-prefix']
