class WebSocket:
    def __init__(self, address, environ, handler):
        self.address = address
        self.environ = environ

        self.handler = handler
        self.read = handler.rfile.read
        self.write = handler.socket.sendall

        self.awaiting_pong = False
        self.last_ping_time = None

    def pong(self):
        if self.awaiting_pong:
            self.awaiting_pong = False
        else:
            print("Pong was not expected")

    def ping(self):
        

    def read_headers(self):
        first_byte = self.read()

        fin = first_byte & 0x80 == 0x80
        opcode = first_byte & 0xf

        if opcode == 0xa:
            return {
                "fin": fin,
                "opcode": opcode
            }

        second_byte = self.read()

        payload_length = second_byte & 0x7F

        if payload_length == 126:
            data = self.read(2)
            payload_length = int.from_bytes(data, byteorder='big')
        elif payload_length > 126:
            data = self.read(8)
            payload_length = int.from_bytes(data, byteorder='big')
        else:
            return {}
        
        return {
            "fin": fin,
            "opcode": opcode,
            "length": payload_length
        }

    def receive(self):
        headers = self.read_headers()

        if headers["opcode"] == 0xa:
            self.pong()
            return

        payload = self.read(headers.length)

        if len(payload) != headers.length:
            return None
        
        return {
            **headers,
            "payload": payload
        }