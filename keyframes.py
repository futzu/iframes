#!/usr/bin/env python3

"""
keyframes.py
"""

import sys
from functools import partial
from threefive import Stream

class KeyFramer(Stream):
    """
    KeyFramer class
    """

    def __init__(self, tsdata, show_null=False):
        """
        tsdata is an file or http/https url or multicast url
        """
        super().__init__(tsdata, show_null)


    @staticmethod
    def _rai_flag(pkt):
        return pkt[5] & 0x40

    @staticmethod
    def _ABC_flags(pkt):
        """
        0x80, 0x20, 0x8
        """
        return pkt[5] & 0xA8   


    def _is_key(self, pkt):
        """
        _is_key is key frame detection.

        """
        if b"\x00\x00\x01\x65" in pkt:
            return True
        if not self._afc_flag(pkt):
            return False
        if self._pcr_flag(pkt):
            if self._rai_flag(pkt):
                return True
        if self._ABC_flags(pkt):
            return True
        return False

 
    def _parse(self, pkt):
        """
        _parse parses mpegts packets
        """
        pid = self._parse_info(pkt)
        if self._pusi_flag(pkt):
            self._parse_pts(pkt, pid)
            if self._is_key(pkt):
                print(f"{self.pid2pts(pid):.6f}")


if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        print("src:",arg)
        keyframer = KeyFramer(arg)
        keyframer.decode()
