from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


def _jupyter_nbextension_paths():  # pragma: no cover
    return [{
        'section': 'notebook',
        # the path is relative to the `jupyter_spark` directory
        'src': 'static',
        # directory in the `nbextension/` namespace
        'dest': 'jupyter_spark_ui',
        # _also_ in the `nbextension/` namespace
        'require': 'jupyter_spark_ui/extension',
    }]

def _jupyter_server_extension_paths():  # pragma: no cover
    return [{
        'module': 'jupyter_spark_ui',
    }]


def load_jupyter_server_extension(nbapp):  # pragma: no cover
    from .spark import Spark
    from .handlers import SparkHandler

    spark = Spark(
        # add access to NotebookApp config, too
        parent=nbapp,
        base_url=nbapp.web_app.settings['base_url'],
    )

    nbapp.web_app.add_handlers(
        r'.*',  # match any host
        [(spark.proxy_url + '.*', SparkHandler, {'spark': spark})]
    )
    nbapp.log.info("Spark-UI enabled!")
