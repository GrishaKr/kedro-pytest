from data_validation_tests.helpers.data_catalog import DataCatalogHelper


class DataProcessingFixture:

    def __init__(self, env):
        self.catalog = DataCatalogHelper(env['catalog']['data_processing']).catalog
        self.pipeline = env['pipeline']
