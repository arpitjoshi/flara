from typing import Any, Dict

import flask
import os

# from dotenv import load_dotenv

# if file exists, variables from it will be added as env vars
# load_dotenv('.local_env')
from app import create_app
from simple_settings import settings

config: Dict[str, Any] = settings.as_dict()

app: flask.Flask = create_app(config)


@app.cli.command()
def test():
    """
    $ flask run # runs unit tests
    """
    import logging
    logger = logging.getLogger('lara.testcases')
    logger.info(f"Starting the TestCases")

    import unittest
    tests = unittest.TestLoader().discover('tests')
    logger.info(f"Variable tests {tests}")
    unittest.TextTestRunner(verbosity=2).run(tests)
