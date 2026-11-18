"""Look up IPv4 addresses and registered services."""

import socket
from ipaddress import IPv4Address


def resolve_hostname(hostname):
    hostname = hostname.strip()
    if not hostname or any(character.isspace() for character in hostname):
        raise ValueError("Enter one hostname without spaces.")
    if "\x00" in hostname:
        raise ValueError("The hostname contains an invalid character.")
    try:
        return socket.gethostbyname(hostname)
    except OSError as error:
        raise ValueError(f"Could not resolve {hostname}: {error}") from error


def lookup_service(port_text):
    try:
        port = int(port_text)
    except ValueError as error:
        raise ValueError("Enter a whole-number port from 1 to 65535.") from error
    if not 1 <= port <= 65535:
        raise ValueError("Enter a port from 1 to 65535.")
    try:
        return socket.getservbyport(port)
    except OSError as error:
        raise ValueError(f"No registered service found for port {port}.") from error


def pack_ipv4(address):
    try:
        return socket.inet_aton(str(IPv4Address(address)))
    except (ValueError, OSError) as error:
        raise ValueError(f"Invalid IPv4 address: {address}") from error
