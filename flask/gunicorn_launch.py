import os

from gunicorn.app.base import Application
import app


class RespucNeam(Application):
    def __init__(self):
        super().__init__()

    def init(self, parser, opts, args):
        self.load_config_from_module_name_or_filename('instance/config_gunicorn.py')

    def load(self):
        config_name = os.getenv('FLASK_CONFIG')
        _app = app.create_app(config_name)
        return _app

 
if __name__ == '__main__':

    _app = RespucNeam()
    _app.run()