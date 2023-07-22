#!/usr/bin/env python3

import sys
from functools import partial
from new_reader import reader

MAJOR = "0"
MINOR = "0"
MAINTAINENCE = "7"

PKT_SIZE = 188

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
    def __init__(self,shush=False):
        self.shush =shush

    @staticmethod
    def _to90k(pts):
        return round(pts/90000.0,6)

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
        pts=None
        if self._pusi_flag(pkt):
            if self._is_key(pkt):
                pts = self._parse_pts(pkt)
                if pts:
                    pts= self._to90k(pts)
                    if not self.shush:
                        print(pts)
        return pts

    def iter_pkts(self, video,num_pkts=1):
        """
        iter_pkts iterates a mpegts stream into packets
        """
        return iter(partial(video.read, PKT_SIZE * num_pkts), b"")

    def do(self,vid):
        """
        do returns a list of PTS for the iframes.
        """
        with reader(vid) as video:
            iframes = [self.parse(pkt) for pkt in self.iter_pkts(video)]
            iframes = list(filter(None,iframes))
            return iframes

    def  first(self,vid):
        """
        first returns the PTS of the first iframe.
        """
        with reader(vid) as video:
             for pkt in self.iter_pkts(video):
                pts = self.parse(pkt)
                if pts is not None:
                    return pts


def cli():
    iframer =IFramer()
    iframer.do(sys.argv[1])

def firstcli():
    iframer =IFramer()
    pts = iframer.first(sys.argv[1])


if __name__ == "__main__":

   cli()
