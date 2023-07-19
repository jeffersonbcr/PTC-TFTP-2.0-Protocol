# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg.proto',
  package='tftp2',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmsg.proto\x12\x05tftp2\"/\n\x03RRQ\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x19\n\x04mode\x18\x02 \x02(\x0e\x32\x0b.tftp2.Mode\"/\n\x03WRQ\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x19\n\x04mode\x18\x02 \x02(\x0e\x32\x0b.tftp2.Mode\"(\n\x04\x44\x41TA\x12\x0f\n\x07message\x18\x01 \x02(\x0c\x12\x0f\n\x07\x62lock_n\x18\x02 \x02(\r\"\x16\n\x03\x41\x43K\x12\x0f\n\x07\x62lock_n\x18\x01 \x02(\r\",\n\x05\x45rror\x12#\n\terrorcode\x18\x01 \x02(\x0e\x32\x10.tftp2.ErrorCode\"\x14\n\x04LIST\x12\x0c\n\x04path\x18\x01 \x02(\t\".\n\x0cListResponse\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.tftp2.ListItem\"L\n\x08ListItem\x12\x1b\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x0b.tftp2.FILEH\x00\x12\x19\n\x03\x64ir\x18\x02 \x01(\x0b\x32\n.tftp2.DIRH\x00\x42\x08\n\x06\x61nswer\"%\n\x04\x46ILE\x12\x0c\n\x04nome\x18\x01 \x02(\t\x12\x0f\n\x07tamanho\x18\x02 \x02(\x05\"\x13\n\x03\x44IR\x12\x0c\n\x04nome\x18\x01 \x02(\t\"\x15\n\x05MKDIR\x12\x0c\n\x04path\x18\x01 \x02(\t\",\n\x04MOVE\x12\x11\n\tnome_orig\x18\x01 \x02(\t\x12\x11\n\tnome_novo\x18\x02 \x01(\t\"\xa1\x02\n\x08Mensagem\x12\x19\n\x03rrq\x18\x01 \x01(\x0b\x32\n.tftp2.RRQH\x00\x12\x19\n\x03wrq\x18\x02 \x01(\x0b\x32\n.tftp2.WRQH\x00\x12\x1b\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0b.tftp2.DATAH\x00\x12\x19\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\n.tftp2.ACKH\x00\x12\x1d\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x0c.tftp2.ErrorH\x00\x12\x1b\n\x04list\x18\x06 \x01(\x0b\x32\x0b.tftp2.LISTH\x00\x12(\n\tlist_resp\x18\x07 \x01(\x0b\x32\x13.tftp2.ListResponseH\x00\x12\x1d\n\x05mkdir\x18\x08 \x01(\x0b\x32\x0c.tftp2.MKDIRH\x00\x12\x1b\n\x04move\x18\t \x01(\x0b\x32\x0b.tftp2.MOVEH\x00\x42\x05\n\x03msg*)\n\x04Mode\x12\x0c\n\x08netascii\x10\x01\x12\t\n\x05octet\x10\x02\x12\x08\n\x04mail\x10\x03*\x99\x01\n\tErrorCode\x12\x10\n\x0c\x46ileNotFound\x10\x01\x12\x13\n\x0f\x41\x63\x63\x65ssViolation\x10\x02\x12\x0c\n\x08\x44iskFull\x10\x03\x12\x14\n\x10IllegalOperation\x10\x04\x12\x0e\n\nUnknownTid\x10\x05\x12\x0e\n\nFileExists\x10\x06\x12\x12\n\x0eUnknownSession\x10\x07\x12\r\n\tUnedfined\x10\x08'
)

_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='tftp2.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='netascii', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='octet', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='mail', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=799,
  serialized_end=840,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='tftp2.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FileNotFound', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AccessViolation', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DiskFull', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IllegalOperation', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UnknownTid', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FileExists', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UnknownSession', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Unedfined', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=843,
  serialized_end=996,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
netascii = 1
octet = 2
mail = 3
FileNotFound = 1
AccessViolation = 2
DiskFull = 3
IllegalOperation = 4
UnknownTid = 5
FileExists = 6
UnknownSession = 7
Unedfined = 8



_RRQ = _descriptor.Descriptor(
  name='RRQ',
  full_name='tftp2.RRQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fname', full_name='tftp2.RRQ.fname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='tftp2.RRQ.mode', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=67,
)


_WRQ = _descriptor.Descriptor(
  name='WRQ',
  full_name='tftp2.WRQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fname', full_name='tftp2.WRQ.fname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='tftp2.WRQ.mode', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=116,
)


_DATA = _descriptor.Descriptor(
  name='DATA',
  full_name='tftp2.DATA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tftp2.DATA.message', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_n', full_name='tftp2.DATA.block_n', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=158,
)


_ACK = _descriptor.Descriptor(
  name='ACK',
  full_name='tftp2.ACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_n', full_name='tftp2.ACK.block_n', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=182,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='tftp2.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorcode', full_name='tftp2.Error.errorcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=228,
)


_LIST = _descriptor.Descriptor(
  name='LIST',
  full_name='tftp2.LIST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='tftp2.LIST.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=250,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='tftp2.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='tftp2.ListResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=298,
)


_LISTITEM = _descriptor.Descriptor(
  name='ListItem',
  full_name='tftp2.ListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='tftp2.ListItem.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dir', full_name='tftp2.ListItem.dir', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='answer', full_name='tftp2.ListItem.answer',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=300,
  serialized_end=376,
)


_FILE = _descriptor.Descriptor(
  name='FILE',
  full_name='tftp2.FILE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='tftp2.FILE.nome', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tamanho', full_name='tftp2.FILE.tamanho', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=415,
)


_DIR = _descriptor.Descriptor(
  name='DIR',
  full_name='tftp2.DIR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='tftp2.DIR.nome', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=436,
)


_MKDIR = _descriptor.Descriptor(
  name='MKDIR',
  full_name='tftp2.MKDIR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='tftp2.MKDIR.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=459,
)


_MOVE = _descriptor.Descriptor(
  name='MOVE',
  full_name='tftp2.MOVE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome_orig', full_name='tftp2.MOVE.nome_orig', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nome_novo', full_name='tftp2.MOVE.nome_novo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=505,
)


_MENSAGEM = _descriptor.Descriptor(
  name='Mensagem',
  full_name='tftp2.Mensagem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rrq', full_name='tftp2.Mensagem.rrq', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wrq', full_name='tftp2.Mensagem.wrq', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='tftp2.Mensagem.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ack', full_name='tftp2.Mensagem.ack', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='tftp2.Mensagem.error', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list', full_name='tftp2.Mensagem.list', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_resp', full_name='tftp2.Mensagem.list_resp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mkdir', full_name='tftp2.Mensagem.mkdir', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='move', full_name='tftp2.Mensagem.move', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='tftp2.Mensagem.msg',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=508,
  serialized_end=797,
)

_RRQ.fields_by_name['mode'].enum_type = _MODE
_WRQ.fields_by_name['mode'].enum_type = _MODE
_ERROR.fields_by_name['errorcode'].enum_type = _ERRORCODE
_LISTRESPONSE.fields_by_name['items'].message_type = _LISTITEM
_LISTITEM.fields_by_name['file'].message_type = _FILE
_LISTITEM.fields_by_name['dir'].message_type = _DIR
_LISTITEM.oneofs_by_name['answer'].fields.append(
  _LISTITEM.fields_by_name['file'])
_LISTITEM.fields_by_name['file'].containing_oneof = _LISTITEM.oneofs_by_name['answer']
_LISTITEM.oneofs_by_name['answer'].fields.append(
  _LISTITEM.fields_by_name['dir'])
_LISTITEM.fields_by_name['dir'].containing_oneof = _LISTITEM.oneofs_by_name['answer']
_MENSAGEM.fields_by_name['rrq'].message_type = _RRQ
_MENSAGEM.fields_by_name['wrq'].message_type = _WRQ
_MENSAGEM.fields_by_name['data'].message_type = _DATA
_MENSAGEM.fields_by_name['ack'].message_type = _ACK
_MENSAGEM.fields_by_name['error'].message_type = _ERROR
_MENSAGEM.fields_by_name['list'].message_type = _LIST
_MENSAGEM.fields_by_name['list_resp'].message_type = _LISTRESPONSE
_MENSAGEM.fields_by_name['mkdir'].message_type = _MKDIR
_MENSAGEM.fields_by_name['move'].message_type = _MOVE
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['rrq'])
_MENSAGEM.fields_by_name['rrq'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['wrq'])
_MENSAGEM.fields_by_name['wrq'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['data'])
_MENSAGEM.fields_by_name['data'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['ack'])
_MENSAGEM.fields_by_name['ack'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['error'])
_MENSAGEM.fields_by_name['error'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['list'])
_MENSAGEM.fields_by_name['list'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['list_resp'])
_MENSAGEM.fields_by_name['list_resp'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['mkdir'])
_MENSAGEM.fields_by_name['mkdir'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['move'])
_MENSAGEM.fields_by_name['move'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['RRQ'] = _RRQ
DESCRIPTOR.message_types_by_name['WRQ'] = _WRQ
DESCRIPTOR.message_types_by_name['DATA'] = _DATA
DESCRIPTOR.message_types_by_name['ACK'] = _ACK
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['LIST'] = _LIST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['ListItem'] = _LISTITEM
DESCRIPTOR.message_types_by_name['FILE'] = _FILE
DESCRIPTOR.message_types_by_name['DIR'] = _DIR
DESCRIPTOR.message_types_by_name['MKDIR'] = _MKDIR
DESCRIPTOR.message_types_by_name['MOVE'] = _MOVE
DESCRIPTOR.message_types_by_name['Mensagem'] = _MENSAGEM
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RRQ = _reflection.GeneratedProtocolMessageType('RRQ', (_message.Message,), {
  'DESCRIPTOR' : _RRQ,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.RRQ)
  })
_sym_db.RegisterMessage(RRQ)

WRQ = _reflection.GeneratedProtocolMessageType('WRQ', (_message.Message,), {
  'DESCRIPTOR' : _WRQ,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.WRQ)
  })
_sym_db.RegisterMessage(WRQ)

DATA = _reflection.GeneratedProtocolMessageType('DATA', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.DATA)
  })
_sym_db.RegisterMessage(DATA)

ACK = _reflection.GeneratedProtocolMessageType('ACK', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.ACK)
  })
_sym_db.RegisterMessage(ACK)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.Error)
  })
_sym_db.RegisterMessage(Error)

LIST = _reflection.GeneratedProtocolMessageType('LIST', (_message.Message,), {
  'DESCRIPTOR' : _LIST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.LIST)
  })
_sym_db.RegisterMessage(LIST)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

ListItem = _reflection.GeneratedProtocolMessageType('ListItem', (_message.Message,), {
  'DESCRIPTOR' : _LISTITEM,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.ListItem)
  })
_sym_db.RegisterMessage(ListItem)

FILE = _reflection.GeneratedProtocolMessageType('FILE', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.FILE)
  })
_sym_db.RegisterMessage(FILE)

DIR = _reflection.GeneratedProtocolMessageType('DIR', (_message.Message,), {
  'DESCRIPTOR' : _DIR,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.DIR)
  })
_sym_db.RegisterMessage(DIR)

MKDIR = _reflection.GeneratedProtocolMessageType('MKDIR', (_message.Message,), {
  'DESCRIPTOR' : _MKDIR,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.MKDIR)
  })
_sym_db.RegisterMessage(MKDIR)

MOVE = _reflection.GeneratedProtocolMessageType('MOVE', (_message.Message,), {
  'DESCRIPTOR' : _MOVE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.MOVE)
  })
_sym_db.RegisterMessage(MOVE)

Mensagem = _reflection.GeneratedProtocolMessageType('Mensagem', (_message.Message,), {
  'DESCRIPTOR' : _MENSAGEM,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:tftp2.Mensagem)
  })
_sym_db.RegisterMessage(Mensagem)


# @@protoc_insertion_point(module_scope)
