import socket
import threading
from pathlib import Path
from urllib.parse import urlparse
import logging

codes = {
    200: "OK",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal server Error",
}

CR_LF = "\r\n"
CR_LF_BYTES = b"\r\n"


def prepare_response(
    http_code: int, content: bytes, is_head_request: bool = False
) -> bytes:
    headers = [
        f"HTTP/1.1 {http_code} {codes.get(http_code, 'Unknown')}",
        "Server: python",
        f"Content-Length: {len(content)}",
        "Content-Type: text/html",
    ]

    return (
        CR_LF.join(headers).encode("utf-8")
        + CR_LF_BYTES
        + CR_LF_BYTES
        + (content if not is_head_request else b"")
        + CR_LF_BYTES
    )


def make_response(
    method: str, path: str, client_socket: socket.socket, document_root: Path
):
    if not method or method.upper() not in ["GET", "HEAD"]:
        prepare_response(405, b"Method Not Allowed")
        return

    x = urlparse(path)
    requested_path = "index.html" if x.path == "/" else x.path.strip("/\\")
    file_path = document_root.joinpath(requested_path)

    is_head_response = method.upper() == "HEAD"
    if not file_path.exists():
        client_socket.send(prepare_response(404, b"Not Found", is_head_response))
        return

    client_socket.send(prepare_response(200, file_path.read_bytes(), is_head_response))


def handle_request(client_socket: socket.socket, document_root: Path):
    try:
        # 1. get request
        data = client_socket.recv(1024)
        if not data:
            return
        # 2. get headers
        headers = data.decode(encoding="utf-8").split(CR_LF)
        # 3. split headers to methods
        method, path, _ = headers.pop(0).split(" ")
        # 4. give back response
        make_response(method, path, client_socket, document_root)
    finally:
        client_socket.close()


def start_server(host: str, port: int, document_root: Path):
    # 1. create socket
    # 2. bind socket to address and port
    # 3. in while loop create threads with function for handle_request
    logging.info(f"Start server: host={host}, port={port}")

    if not document_root.exists():
        logging.error(
            f"Document root path {document_root} does not exists! Stop action"
        )
        exit(1)
    logging.info(f"Document root configured: {document_root}")

    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_tcp.bind((host, port))
    s_tcp.listen(5)
    while True:
        client_socket, _ = s_tcp.accept()
        client_handler = threading.Thread(
            target=handle_request, args=(client_socket, document_root)
        )
        client_handler.start()
