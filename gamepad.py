import socket
import time

class HKProtocol(object):
    def __init__(self):
        self.headerData = [85, 0, 11, 0]
        self.header = ''.join([chr(x) for x in self.headerData])
        self.posData = [0, 0, 0, 0, 0, 0]

    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('192.168.1.113', 5500))

    def test_channels(self):
        for i in range(50):
            self.posData = [60, 60, 60, 60, 0, 0]
            self.send()
            time.sleep(0.01)

    def send(self):
        pos = ''.join([chr(x) for x in self.posData])
        checksum = (sum(self.posData) + sum(self.headerData)) % 256
        data = self.header + pos + chr(checksum)
        self.s.send(data)

    def stop(self):
        self.posData = [0, 0, 0, 0, 0, 0]
        self.send()
        self.s.close()
        del(self.s)

if __name__ == "__main__":
    import pygame
    pygame.init()
    j = pygame.joystick.Joystick(0)
    j.init()
    hk = HKProtocol()
    running = False
    while True:
        pygame.event.pump()
        ch1 = int(50 - (j.get_axis(1) * 50))
        ch2, ch3, ch4 = 0, 0, 0

        # Start engine (square button)
        if j.get_button(3):
            if not running:
                running = True
                hk.start()

        # Stop engine (circle button)
        if j.get_button(1):
            if running:
                hk.stop()
            break

        if running:
            hk.posData = [ch1, ch2, ch3, ch4, 0, 0]
            hk.send()
        time.sleep(0.01)