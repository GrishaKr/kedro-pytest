from src.tests.helpers.data_catalog import DataCatalogHelper
from typing import Dict


class DataProcessingFixture:

    def __init__(self, env):
        self.catalog = DataCatalogHelper(env['catalog']['data_processing']).catalog
        self.pipeline = env['pipeline']
