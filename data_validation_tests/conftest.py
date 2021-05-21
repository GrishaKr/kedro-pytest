from data_validation_tests.fixture_starter.app_manager.data_processing_fixture import DataProcessingFixture
from data_validation_tests.fixture_starter.env_starter import EnvStarter
from src.kedro_tutorial.pipelines.data_processing import create_pipeline
import pytest


@pytest.fixture(autouse=True)
def data_processing():
    env = EnvStarter(env="test").env
    env['pipeline'] = create_pipeline
    return DataProcessingFixture(env)
