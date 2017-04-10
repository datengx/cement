"""Cement core plugins module."""

from abc import abstractmethod
from ..core.handler import Handler
from ..utils.misc import minimal_logger

LOG = minimal_logger(__name__)



class PluginHandlerBase(Handler):

    """
    This class defines the Plugin Handler Interface.  Classes that
    implement this interface must provide the methods and attributes defined
    below.

    Usage:

    .. code-block:: python

        from cement.core.plugin import PluginHandlerBase

        class MyPluginHandler(PluginHandlerBase):
            class Meta:
                label = 'my_plugin_handler'
            ...

    """

    #: String identifier of the interface.
    interface = 'plugin'

    @abstractmethod
    def load_plugin(plugin_name):
        """
        Load a plugin whose name is 'plugin_name'.

        :param plugin_name: The name of the plugin to load.

        """
        pass

    @abstractmethod
    def load_plugins(self, plugin_list):
        """
        Load all plugins from plugin_list.

        :param plugin_list: A list of plugin names to load.

        """
        pass

    @abstractmethod
    def get_loaded_plugins(self):
        """Returns a list of plugins that have been loaded."""
        pass

    @abstractmethod
    def get_enabled_plugins(self):
        """Returns a list of plugins that are enabled in the config."""
        pass

    @abstractmethod
    def get_disabled_plugins(self):
        """Returns a list of plugins that are disabled in the config."""
        pass

class PluginHandler(PluginHandlerBase):

    """
    Plugin handler implementation.

    """

    pass
