""" Preprocess data to prepare it for model training. """

import logging
from pathlib import Path
from typing import Union

from dotenv import find_dotenv, load_dotenv


def main(input_filepath: Union[str, Path], output_filepath: Union[str, Path]) -> None:
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    print(input_filepath)
    print(output_filepath)


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main('data/raw', 'data/processed')
