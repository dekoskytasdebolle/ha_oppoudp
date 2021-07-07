""" Home Assistant derived exceptions"""

from homeassistant import exceptions as ha_exc

class HaCannotConnect(ha_exc.HomeAssistantError):
    """Error to indicate we cannot connect."""
