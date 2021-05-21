from kedro.io import DataCatalog
from kedro.config import ConfigLoader


class DataCatalogHelper(object):
    def __init__(self, env_data_catalog):
        self.env_data_catalog = env_data_catalog
        self.catalog = self.get_data_catalog(env_data_catalog)

    @staticmethod
    def get_data_catalog(env_data_catalog) -> DataCatalog:
        conf_loader = ConfigLoader(env_data_catalog['path'])
        conf_catalog = conf_loader.get(*env_data_catalog['patterns'])
        catalog = DataCatalog.from_config(conf_catalog)
        return catalog
