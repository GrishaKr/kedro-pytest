from kedro.runner import SequentialRunner
import pytest
import os


class TestCheckPrice:
    @pytest.fixture(autouse=True)
    def __get_fixture(self, data_processing):
        self.catalog = data_processing.catalog
        self.pipeline = data_processing.pipeline
        self.path_to_test_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../test_data")

    def test_data_processing_pipeline_max_price(self):
        runner = SequentialRunner()
        pipeline_output = runner.run(self.pipeline(), self.catalog)
        max_values = pipeline_output['master_table'].max()
        assert max_values['price'] == 86150

    def test_data_processing_pipeline_min_price(self):
        runner = SequentialRunner()
        pipeline_output = runner.run(self.pipeline(), self.catalog)
        max_values = pipeline_output['master_table'].min()
        assert max_values['price'] == 86150


@pytest.fixture(autouse=False)
def test_fixture():
    """additional fixture
    for ex.: to change the input data for the pipeline in the csv file"""
    pass
