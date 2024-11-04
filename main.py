from app import App
from dotenv import load_dotenv
from app.plugins.plugin_manager import PluginManager

if __name__ == '__main__':
    app = App().start()