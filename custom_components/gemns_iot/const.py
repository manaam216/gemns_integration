"""Constants for the Gemns™ IoT integration."""
from typing import Final

DOMAIN: Final = "gemns_iot"

# Configuration keys
CONF_MQTT_BROKER: Final = "mqtt_broker"
CONF_MQTT_USERNAME: Final = "mqtt_username"
CONF_MQTT_PASSWORD: Final = "mqtt_password"
CONF_ENABLE_ZIGBEE: Final = "enable_zigbee"
CONF_SCAN_INTERVAL: Final = "scan_interval"
CONF_HEARTBEAT_INTERVAL: Final = "heartbeat_interval"

# Default values
DEFAULT_MQTT_BROKER: Final = "mqtt://homeassistant:1883"
DEFAULT_SCAN_INTERVAL: Final = 0.02
DEFAULT_HEARTBEAT_INTERVAL: Final = 10.0
DEFAULT_ENABLE_ZIGBEE: Final = True

# MQTT Topics
MQTT_TOPIC_STATUS: Final = "gemns_iot/status"
MQTT_TOPIC_CONTROL: Final = "gemns_iot/control"
MQTT_TOPIC_DEVICE: Final = "gemns_iot/device"

# Device types
DEVICE_TYPE_BLE: Final = "ble"
DEVICE_TYPE_ZIGBEE: Final = "zigbee"
DEVICE_TYPE_ZWAVE: Final = "zwave"
DEVICE_TYPE_MATTER: Final = "matter"
DEVICE_TYPE_GENERIC: Final = "generic"

# Device categories
DEVICE_CATEGORY_SENSOR: Final = "sensor"
DEVICE_CATEGORY_SWITCH: Final = "switch"
DEVICE_CATEGORY_LIGHT: Final = "light"
DEVICE_CATEGORY_DOOR: Final = "door"
DEVICE_CATEGORY_TOGGLE: Final = "toggle"

# Device statuses
DEVICE_STATUS_DISCONNECTED: Final = "disconnected"
DEVICE_STATUS_CONNECTING: Final = "connecting"
DEVICE_STATUS_CONNECTED: Final = "connected"
DEVICE_STATUS_IDENTIFIED: Final = "identified"
DEVICE_STATUS_PAIRED: Final = "paired"
DEVICE_STATUS_OFFLINE: Final = "offline"
DEVICE_STATUS_ERROR: Final = "error"

# BLE discovery modes
BLE_DISCOVERY_MODE_V0_MANUAL: Final = "v0_manual"
BLE_DISCOVERY_MODE_V1_AUTO: Final = "v1_auto"

# Integration name and version
INTEGRATION_NAME: Final = "Gemns™ IoT"
INTEGRATION_VERSION: Final = "1.0.101"

# BLE Packet Format Constants
BLE_COMPANY_ID: Final = 0x5750  # Gemns™ company ID
BLE_PACKET_LENGTH: Final = 20
BLE_ENCRYPTED_DATA_SIZE: Final = 16

# BLE Configuration
CONF_ADDRESS: Final = "address"
CONF_NAME: Final = "name"
CONF_DECRYPTION_KEY: Final = "decryption_key"
CONF_DEVICE_NAME: Final = "device_name"
CONF_SENSOR_TYPE: Final = "sensor_type"

# Sensor Types
SENSOR_TYPE_LEAK: Final = 4
SENSOR_TYPE_TEMPERATURE: Final = 1
SENSOR_TYPE_HUMIDITY: Final = 2
SENSOR_TYPE_PRESSURE: Final = 3
SENSOR_TYPE_VIBRATION: Final = 5

# Switch Types
SWITCH_TYPE_ON_OFF: Final = 6
SWITCH_TYPE_LIGHT: Final = 7
SWITCH_TYPE_DOOR: Final = 8
SWITCH_TYPE_TOGGLE: Final = 9

# Signals
SIGNAL_DEVICE_UPDATED: Final = f"{DOMAIN}_device_updated"
SIGNAL_DEVICE_ADDED: Final = f"{DOMAIN}_device_added"


