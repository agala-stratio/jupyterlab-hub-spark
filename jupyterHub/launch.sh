docker run --rm --net host -v \
/home/agala/IdeaProjects/jupyterlab-hub-spark/jupyterHub/jupyterhub/jupyterhub_config_alvaro.py:/jupyterhub_config_alvaro.py -v /var/run/docker.sock:/var/run/docker.sock jupyterhub/jupyterhub:alvaro

#docker run -p 8000:8000 -d --name jupyterhub jupyterhub/jupyterhub:alvaro
