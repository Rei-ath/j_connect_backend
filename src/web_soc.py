import asyncio
import websockets

connected_clients = {}  # Dictionary to store connected client WebSocket connections by IP address

async def handler(websocket, path):
    client_ip = websocket.remote_address[0]  # Get the client's IP address

    # Add the client WebSocket connection to the dictionary
    connected_clients[client_ip] = websocket

    try:
        async for message in websocket:
            # Process and respond to client messages as needed
            print(f"Received message from client {client_ip}: {message}")
            await websocket.send(message)  # Send a response back to the client
    except websockets.exceptions.ConnectionClosedError:
        pass  # Handle the case when the client disconnects

    # Remove the client from the dictionary when the connection is closed
    del connected_clients[client_ip]

async def main(address='192.168.0.114', port=42069):
    server = await websockets.serve(handler, address, port)
    print(f'Server started at ws://{address}:{port}')

    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
