import socket

def send_datagram(message, host='127.0.0.1', port=553):
    try:
        # Create a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Send data
            sock.sendto(message.encode(), (host, port))
        print(f"Datagram sent to {host}:{port}: {message}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    message = "Hello, UDP1!"
    send_datagram(message)
