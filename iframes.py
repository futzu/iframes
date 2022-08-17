import sys
from functools import partial


MAJOR = "0"
MINOR = "0"
MAINTAINENCE = "1"


def version():
    """
    version prints version as a string

    Odd number versions are releases.
    Even number versions are testing builds between releases.

    Used to set version in setup.py
    and as an easy way to check which
    version you have installed.

    """
    return f"{MAJOR}.{MINOR}.{MAINTAINENCE}"


class IFramer:

    @staticmethod
    def _abc_flags(pkt):
        """
        0x80, 0x20, 0x8
        """
        return pkt[5] & 0xA8

    @staticmethod
    def _afc_flag(pkt):
        return pkt[3] & 0x20

    @staticmethod
    def _nal(pkt):
        return b"\x00\x00\x01\x65" in pkt

    @staticmethod
    def _pcr_flag(pkt):
        return pkt[5] & 0x10

    @staticmethod
    def _pts_flag(pay):
        # uses pay not pkt
        return pay[7] & 0x80

    @staticmethod
    def _pusi_flag(pkt):
        return pkt[1] & 0x40

    @staticmethod
    def _rai_flag(pkt):
        return pkt[5] & 0x40

    def _parse_payload(self, pkt):
        head_size = 4
        if self._afc_flag(pkt):
            afl = pkt[4]
            head_size += afl + 1  # +1 for afl byte
        return pkt[head_size:]

    def _parse_pts(self, pkt):
        """
        parse pts from pkt and store it
        in the dict Stream._pid_pts.
        """
        payload = self._parse_payload(pkt)
        if len(payload) < 14:
            return
        if self._pts_flag(payload):
            pts = ((payload[9] >> 1) & 7) << 30
            pts |= payload[10] << 22
            pts |= (payload[11] >> 1) << 15
            pts |= payload[12] << 7
            pts |= payload[13] >> 1
            return pts

    def _is_key(self, pkt):
        """
        _is_key is key frame detection.
        """
        if self._nal(pkt):
            return True
        if not self._afc_flag(pkt):
            return False
        if self._pcr_flag(pkt):
            if self. _rai_flag(pkt):
                return True
        if self._abc_flags(pkt):
            return True
        return False

    def parse(self,pkt):
        if self._pusi_flag(pkt):
            if self._is_key(pkt):
                pts = self._parse_pts(pkt)
                return round(pts/90000.0,6)
        return None

    def do(self,vid):
        packet_size = 188
        with open(vid,'rb') as video:
            iframes = [self.parse(pkt) for pkt in iter(partial(video.read, packet_size), b"")]
            iframes = list(filter(None,iframes))
            print(iframes)
            return iframes


def cli():
    iframer =IFramer()
    iframer.do(sys.argv[1])


if __name__  == ' __main__':
    cli()
