from awscrt import http
from awsiot import mqtt_connection_builder

# Certificate path
cert_file = 'j-connect-thingy.cert.pem'
key_file = 'j-connect-thingy.private.key'

"""
Add your AWS resource information
"""

end="$aws/things/j-connect-thingy/shadow/get/accepted"
client_id = 'j-connect-thingy'
server = 'a2r4euk7l75oz1-ats.iot.eu-north-1.amazonaws.com'


# Callback when connection is accidentally lost.
def on_connection_interrupted(connection, error):
    print(f"Connection interrupted. error: {error}")

# Callback when an interrupted connection is re-established.
def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print("Connection resumed. return_code: {} session_present: {}".format(return_code, session_present))


if __name__ == '__main__':
    # Create the proxy options if the data is present in cmdData
    proxy_options = None
    # Create a MQTT connection from the command line data
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=client_id,
        port=8883,
        cert_filepath='/home/jang/Desktop/J_connect_backend/src/j-connect-thingy.cert.pem',
        pri_key_filepath='/home/jang/Desktop/J_connect_backend/src/j-connect-thingy.private.key',
        ca_filepath=None,
        on_connection_interrupted=on_connection_interrupted,
        on_connection_resumed=on_connection_resumed,
        client_id=client_id,
        clean_session=False,
        keep_alive_secs=30,
        http_proxy_options=proxy_options
        )

    if not client_id:
        print(f"Connecting to {end} with client ID '{client_id}'...")
    else:
        print("Connecting to endpoint with client ID")

    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")

    # Disconnect
    print("Disconnecting...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected!")