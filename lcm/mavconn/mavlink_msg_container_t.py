"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import mavconn.mavlink_message_t

class mavlink_msg_container_t(object):
    __slots__ = ["link_network_source", "link_component_id", "msg", "extended_payload_len", "extended_payload"]

    def __init__(self):
        self.link_network_source = 0
        self.link_component_id = 0
        self.msg = None
        self.extended_payload_len = 0
        self.extended_payload = []

    def encode(self):
        buf = BytesIO()
        buf.write(mavlink_msg_container_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">bb", self.link_network_source, self.link_component_id))
        assert self.msg._get_packed_fingerprint() == mavconn.mavlink_message_t._get_packed_fingerprint()
        self.msg._encode_one(buf)
        buf.write(struct.pack(">i", self.extended_payload_len))
        buf.write(struct.pack('>%db' % self.extended_payload_len, *self.extended_payload[:self.extended_payload_len]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mavlink_msg_container_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mavlink_msg_container_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mavlink_msg_container_t()
        self.link_network_source, self.link_component_id = struct.unpack(">bb", buf.read(2))
        self.msg = mavconn.mavlink_message_t._decode_one(buf)
        self.extended_payload_len = struct.unpack(">i", buf.read(4))[0]
        self.extended_payload = struct.unpack('>%db' % self.extended_payload_len, buf.read(self.extended_payload_len))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if mavlink_msg_container_t in parents: return 0
        newparents = parents + [mavlink_msg_container_t]
        tmphash = (0x893144dfcd4de92f+ mavconn.mavlink_message_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mavlink_msg_container_t._packed_fingerprint is None:
            mavlink_msg_container_t._packed_fingerprint = struct.pack(">Q", mavlink_msg_container_t._get_hash_recursive([]))
        return mavlink_msg_container_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
