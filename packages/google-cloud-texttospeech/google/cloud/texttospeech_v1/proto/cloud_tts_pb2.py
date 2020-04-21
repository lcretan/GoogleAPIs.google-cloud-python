# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/texttospeech_v1/proto/cloud_tts.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/texttospeech_v1/proto/cloud_tts.proto",
    package="google.cloud.texttospeech.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n com.google.cloud.texttospeech.v1B\021TextToSpeechProtoP\001ZHgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1;texttospeech\370\001\001\252\002\034Google.Cloud.TextToSpeech.V1\312\002\034Google\\Cloud\\TextToSpeech\\V1\352\002\037Google::Cloud::TextToSpeech::V1"
    ),
    serialized_pb=_b(
        '\n2google/cloud/texttospeech_v1/proto/cloud_tts.proto\x12\x1cgoogle.cloud.texttospeech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"/\n\x11ListVoicesRequest\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0\x41\x01"I\n\x12ListVoicesResponse\x12\x33\n\x06voices\x18\x01 \x03(\x0b\x32#.google.cloud.texttospeech.v1.Voice"\x94\x01\n\x05Voice\x12\x16\n\x0elanguage_codes\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x42\n\x0bssml_gender\x18\x03 \x01(\x0e\x32-.google.cloud.texttospeech.v1.SsmlVoiceGender\x12!\n\x19natural_sample_rate_hertz\x18\x04 \x01(\x05"\xe9\x01\n\x17SynthesizeSpeechRequest\x12@\n\x05input\x18\x01 \x01(\x0b\x32,.google.cloud.texttospeech.v1.SynthesisInputB\x03\xe0\x41\x02\x12\x46\n\x05voice\x18\x02 \x01(\x0b\x32\x32.google.cloud.texttospeech.v1.VoiceSelectionParamsB\x03\xe0\x41\x02\x12\x44\n\x0c\x61udio_config\x18\x03 \x01(\x0b\x32).google.cloud.texttospeech.v1.AudioConfigB\x03\xe0\x41\x02"@\n\x0eSynthesisInput\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x0e\n\x04ssml\x18\x02 \x01(\tH\x00\x42\x0e\n\x0cinput_source"\x84\x01\n\x14VoiceSelectionParams\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x42\n\x0bssml_gender\x18\x03 \x01(\x0e\x32-.google.cloud.texttospeech.v1.SsmlVoiceGender"\xf1\x01\n\x0b\x41udioConfig\x12H\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32+.google.cloud.texttospeech.v1.AudioEncodingB\x03\xe0\x41\x02\x12\x1d\n\rspeaking_rate\x18\x02 \x01(\x01\x42\x06\xe0\x41\x04\xe0\x41\x01\x12\x15\n\x05pitch\x18\x03 \x01(\x01\x42\x06\xe0\x41\x04\xe0\x41\x01\x12\x1e\n\x0evolume_gain_db\x18\x04 \x01(\x01\x42\x06\xe0\x41\x04\xe0\x41\x01\x12\x1e\n\x11sample_rate_hertz\x18\x05 \x01(\x05\x42\x03\xe0\x41\x01\x12"\n\x12\x65\x66\x66\x65\x63ts_profile_id\x18\x06 \x03(\tB\x06\xe0\x41\x04\xe0\x41\x01"1\n\x18SynthesizeSpeechResponse\x12\x15\n\raudio_content\x18\x01 \x01(\x0c*W\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03*T\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0c\n\x08OGG_OPUS\x10\x03\x32\xb4\x03\n\x0cTextToSpeech\x12\x93\x01\n\nListVoices\x12/.google.cloud.texttospeech.v1.ListVoicesRequest\x1a\x30.google.cloud.texttospeech.v1.ListVoicesResponse""\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/voices\xda\x41\rlanguage_code\x12\xbc\x01\n\x10SynthesizeSpeech\x12\x35.google.cloud.texttospeech.v1.SynthesizeSpeechRequest\x1a\x36.google.cloud.texttospeech.v1.SynthesizeSpeechResponse"9\x82\xd3\xe4\x93\x02\x18"\x13/v1/text:synthesize:\x01*\xda\x41\x18input,voice,audio_config\x1aO\xca\x41\x1btexttospeech.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xe4\x01\n com.google.cloud.texttospeech.v1B\x11TextToSpeechProtoP\x01ZHgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1;texttospeech\xf8\x01\x01\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
    ],
)

_SSMLVOICEGENDER = _descriptor.EnumDescriptor(
    name="SsmlVoiceGender",
    full_name="google.cloud.texttospeech.v1.SsmlVoiceGender",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SSML_VOICE_GENDER_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MALE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FEMALE", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="NEUTRAL", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1179,
    serialized_end=1266,
)
_sym_db.RegisterEnumDescriptor(_SSMLVOICEGENDER)

SsmlVoiceGender = enum_type_wrapper.EnumTypeWrapper(_SSMLVOICEGENDER)
_AUDIOENCODING = _descriptor.EnumDescriptor(
    name="AudioEncoding",
    full_name="google.cloud.texttospeech.v1.AudioEncoding",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="AUDIO_ENCODING_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="LINEAR16", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MP3", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OGG_OPUS", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1268,
    serialized_end=1352,
)
_sym_db.RegisterEnumDescriptor(_AUDIOENCODING)

AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
SSML_VOICE_GENDER_UNSPECIFIED = 0
MALE = 1
FEMALE = 2
NEUTRAL = 3
AUDIO_ENCODING_UNSPECIFIED = 0
LINEAR16 = 1
MP3 = 2
OGG_OPUS = 3


_LISTVOICESREQUEST = _descriptor.Descriptor(
    name="ListVoicesRequest",
    full_name="google.cloud.texttospeech.v1.ListVoicesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="language_code",
            full_name="google.cloud.texttospeech.v1.ListVoicesRequest.language_code",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=172,
    serialized_end=219,
)


_LISTVOICESRESPONSE = _descriptor.Descriptor(
    name="ListVoicesResponse",
    full_name="google.cloud.texttospeech.v1.ListVoicesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="voices",
            full_name="google.cloud.texttospeech.v1.ListVoicesResponse.voices",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=221,
    serialized_end=294,
)


_VOICE = _descriptor.Descriptor(
    name="Voice",
    full_name="google.cloud.texttospeech.v1.Voice",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="language_codes",
            full_name="google.cloud.texttospeech.v1.Voice.language_codes",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.texttospeech.v1.Voice.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ssml_gender",
            full_name="google.cloud.texttospeech.v1.Voice.ssml_gender",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="natural_sample_rate_hertz",
            full_name="google.cloud.texttospeech.v1.Voice.natural_sample_rate_hertz",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=297,
    serialized_end=445,
)


_SYNTHESIZESPEECHREQUEST = _descriptor.Descriptor(
    name="SynthesizeSpeechRequest",
    full_name="google.cloud.texttospeech.v1.SynthesizeSpeechRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="google.cloud.texttospeech.v1.SynthesizeSpeechRequest.input",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="voice",
            full_name="google.cloud.texttospeech.v1.SynthesizeSpeechRequest.voice",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="audio_config",
            full_name="google.cloud.texttospeech.v1.SynthesizeSpeechRequest.audio_config",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=448,
    serialized_end=681,
)


_SYNTHESISINPUT = _descriptor.Descriptor(
    name="SynthesisInput",
    full_name="google.cloud.texttospeech.v1.SynthesisInput",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="text",
            full_name="google.cloud.texttospeech.v1.SynthesisInput.text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ssml",
            full_name="google.cloud.texttospeech.v1.SynthesisInput.ssml",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="input_source",
            full_name="google.cloud.texttospeech.v1.SynthesisInput.input_source",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=683,
    serialized_end=747,
)


_VOICESELECTIONPARAMS = _descriptor.Descriptor(
    name="VoiceSelectionParams",
    full_name="google.cloud.texttospeech.v1.VoiceSelectionParams",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="language_code",
            full_name="google.cloud.texttospeech.v1.VoiceSelectionParams.language_code",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.texttospeech.v1.VoiceSelectionParams.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ssml_gender",
            full_name="google.cloud.texttospeech.v1.VoiceSelectionParams.ssml_gender",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=750,
    serialized_end=882,
)


_AUDIOCONFIG = _descriptor.Descriptor(
    name="AudioConfig",
    full_name="google.cloud.texttospeech.v1.AudioConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="audio_encoding",
            full_name="google.cloud.texttospeech.v1.AudioConfig.audio_encoding",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="speaking_rate",
            full_name="google.cloud.texttospeech.v1.AudioConfig.speaking_rate",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\004\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pitch",
            full_name="google.cloud.texttospeech.v1.AudioConfig.pitch",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\004\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="volume_gain_db",
            full_name="google.cloud.texttospeech.v1.AudioConfig.volume_gain_db",
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\004\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sample_rate_hertz",
            full_name="google.cloud.texttospeech.v1.AudioConfig.sample_rate_hertz",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="effects_profile_id",
            full_name="google.cloud.texttospeech.v1.AudioConfig.effects_profile_id",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\004\340A\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=885,
    serialized_end=1126,
)


_SYNTHESIZESPEECHRESPONSE = _descriptor.Descriptor(
    name="SynthesizeSpeechResponse",
    full_name="google.cloud.texttospeech.v1.SynthesizeSpeechResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="audio_content",
            full_name="google.cloud.texttospeech.v1.SynthesizeSpeechResponse.audio_content",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1128,
    serialized_end=1177,
)

_LISTVOICESRESPONSE.fields_by_name["voices"].message_type = _VOICE
_VOICE.fields_by_name["ssml_gender"].enum_type = _SSMLVOICEGENDER
_SYNTHESIZESPEECHREQUEST.fields_by_name["input"].message_type = _SYNTHESISINPUT
_SYNTHESIZESPEECHREQUEST.fields_by_name["voice"].message_type = _VOICESELECTIONPARAMS
_SYNTHESIZESPEECHREQUEST.fields_by_name["audio_config"].message_type = _AUDIOCONFIG
_SYNTHESISINPUT.oneofs_by_name["input_source"].fields.append(
    _SYNTHESISINPUT.fields_by_name["text"]
)
_SYNTHESISINPUT.fields_by_name[
    "text"
].containing_oneof = _SYNTHESISINPUT.oneofs_by_name["input_source"]
_SYNTHESISINPUT.oneofs_by_name["input_source"].fields.append(
    _SYNTHESISINPUT.fields_by_name["ssml"]
)
_SYNTHESISINPUT.fields_by_name[
    "ssml"
].containing_oneof = _SYNTHESISINPUT.oneofs_by_name["input_source"]
_VOICESELECTIONPARAMS.fields_by_name["ssml_gender"].enum_type = _SSMLVOICEGENDER
_AUDIOCONFIG.fields_by_name["audio_encoding"].enum_type = _AUDIOENCODING
DESCRIPTOR.message_types_by_name["ListVoicesRequest"] = _LISTVOICESREQUEST
DESCRIPTOR.message_types_by_name["ListVoicesResponse"] = _LISTVOICESRESPONSE
DESCRIPTOR.message_types_by_name["Voice"] = _VOICE
DESCRIPTOR.message_types_by_name["SynthesizeSpeechRequest"] = _SYNTHESIZESPEECHREQUEST
DESCRIPTOR.message_types_by_name["SynthesisInput"] = _SYNTHESISINPUT
DESCRIPTOR.message_types_by_name["VoiceSelectionParams"] = _VOICESELECTIONPARAMS
DESCRIPTOR.message_types_by_name["AudioConfig"] = _AUDIOCONFIG
DESCRIPTOR.message_types_by_name["SynthesizeSpeechResponse"] = _SYNTHESIZESPEECHRESPONSE
DESCRIPTOR.enum_types_by_name["SsmlVoiceGender"] = _SSMLVOICEGENDER
DESCRIPTOR.enum_types_by_name["AudioEncoding"] = _AUDIOENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListVoicesRequest = _reflection.GeneratedProtocolMessageType(
    "ListVoicesRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTVOICESREQUEST,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""The top-level message sent by the client for the ``ListVoices``
  method.
  Attributes:
      language_code:
          Optional. Recommended. `BCP-47 <https://www.rfc-
          editor.org/rfc/bcp/bcp47.txt>`__ language tag. If specified,
          the ListVoices call will only return voices that can be used
          to synthesize this language\_code. E.g. when specifying "en-
          NZ", you will get supported "en-*" voices; when specifying
          "no", you will get supported "no-*" (Norwegian) and "nb-*"
          (Norwegian Bokmal) voices; specifying "zh" will also get
          supported "cmn-*" voices; specifying "zh-hk" will also get
          supported "yue-\*" voices.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.ListVoicesRequest)
    ),
)
_sym_db.RegisterMessage(ListVoicesRequest)

ListVoicesResponse = _reflection.GeneratedProtocolMessageType(
    "ListVoicesResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTVOICESRESPONSE,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""The message returned to the client by the ``ListVoices`` method.
  Attributes:
      voices:
          The list of voices.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.ListVoicesResponse)
    ),
)
_sym_db.RegisterMessage(ListVoicesResponse)

Voice = _reflection.GeneratedProtocolMessageType(
    "Voice",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VOICE,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""Description of a voice supported by the TTS service.
  Attributes:
      language_codes:
          The languages that this voice supports, expressed as `BCP-47
          <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__ language
          tags (e.g. "en-US", "es-419", "cmn-tw").
      name:
          The name of this voice. Each distinct voice has a unique name.
      ssml_gender:
          The gender of this voice.
      natural_sample_rate_hertz:
          The natural sample rate (in hertz) for this voice.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.Voice)
    ),
)
_sym_db.RegisterMessage(Voice)

SynthesizeSpeechRequest = _reflection.GeneratedProtocolMessageType(
    "SynthesizeSpeechRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SYNTHESIZESPEECHREQUEST,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""The top-level message sent by the client for the ``SynthesizeSpeech``
  method.
  Attributes:
      input:
          Required. The Synthesizer requires either plain text or SSML
          as input.
      voice:
          Required. The desired voice of the synthesized audio.
      audio_config:
          Required. The configuration of the synthesized audio.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesizeSpeechRequest)
    ),
)
_sym_db.RegisterMessage(SynthesizeSpeechRequest)

SynthesisInput = _reflection.GeneratedProtocolMessageType(
    "SynthesisInput",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SYNTHESISINPUT,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""Contains text input to be synthesized. Either ``text`` or ``ssml``
  must be supplied. Supplying both or neither returns
  [google.rpc.Code.INVALID\_ARGUMENT][]. The input size is limited to
  5000 characters.
  Attributes:
      input_source:
          The input source, which is either plain text or SSML.
      text:
          The raw text to be synthesized.
      ssml:
          The SSML document to be synthesized. The SSML document must be
          valid and well-formed. Otherwise the RPC will fail and return
          [google.rpc.Code.INVALID\_ARGUMENT][]. For more information,
          see `SSML </speech/text-to-speech/docs/ssml>`__.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesisInput)
    ),
)
_sym_db.RegisterMessage(SynthesisInput)

VoiceSelectionParams = _reflection.GeneratedProtocolMessageType(
    "VoiceSelectionParams",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VOICESELECTIONPARAMS,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""Description of which voice to use for a synthesis request.
  Attributes:
      language_code:
          Required. The language (and potentially also the region) of
          the voice expressed as a `BCP-47 <https://www.rfc-
          editor.org/rfc/bcp/bcp47.txt>`__ language tag, e.g. "en-US".
          This should not include a script tag (e.g. use "cmn-cn" rather
          than "cmn-Hant-cn"), because the script will be inferred from
          the input provided in the SynthesisInput. The TTS service will
          use this parameter to help choose an appropriate voice. Note
          that the TTS service may choose a voice with a slightly
          different language code than the one selected; it may
          substitute a different region (e.g. using en-US rather than
          en-CA if there isn't a Canadian voice available), or even a
          different language, e.g. using "nb" (Norwegian Bokmal) instead
          of "no" (Norwegian)".
      name:
          The name of the voice. If not set, the service will choose a
          voice based on the other parameters such as language\_code and
          gender.
      ssml_gender:
          The preferred gender of the voice. If not set, the service
          will choose a voice based on the other parameters such as
          language\_code and name. Note that this is only a preference,
          not requirement; if a voice of the appropriate gender is not
          available, the synthesizer should substitute a voice with a
          different gender rather than failing the request.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.VoiceSelectionParams)
    ),
)
_sym_db.RegisterMessage(VoiceSelectionParams)

AudioConfig = _reflection.GeneratedProtocolMessageType(
    "AudioConfig",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AUDIOCONFIG,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""Description of audio data to be synthesized.
  Attributes:
      audio_encoding:
          Required. The format of the audio byte stream.
      speaking_rate:
          Optional. Input only. Speaking rate/speed, in the range [0.25,
          4.0]. 1.0 is the normal native speed supported by the specific
          voice. 2.0 is twice as fast, and 0.5 is half as fast. If
          unset(0.0), defaults to the native 1.0 speed. Any other values
          < 0.25 or > 4.0 will return an error.
      pitch:
          Optional. Input only. Speaking pitch, in the range [-20.0,
          20.0]. 20 means increase 20 semitones from the original pitch.
          -20 means decrease 20 semitones from the original pitch.
      volume_gain_db:
          Optional. Input only. Volume gain (in dB) of the normal native
          volume supported by the specific voice, in the range [-96.0,
          16.0]. If unset, or set to a value of 0.0 (dB), will play at
          normal native signal amplitude. A value of -6.0 (dB) will play
          at approximately half the amplitude of the normal native
          signal amplitude. A value of +6.0 (dB) will play at
          approximately twice the amplitude of the normal native signal
          amplitude. Strongly recommend not to exceed +10 (dB) as
          there's usually no effective increase in loudness for any
          value greater than that.
      sample_rate_hertz:
          Optional. The synthesis sample rate (in hertz) for this audio.
          When this is specified in SynthesizeSpeechRequest, if this is
          different from the voice's natural sample rate, then the
          synthesizer will honor this request by converting to the
          desired sample rate (which might result in worse audio
          quality), unless the specified sample rate is not supported
          for the encoding chosen, in which case it will fail the
          request and return [google.rpc.Code.INVALID\_ARGUMENT][].
      effects_profile_id:
          Optional. Input only. An identifier which selects 'audio
          effects' profiles that are applied on (post synthesized) text
          to speech. Effects are applied on top of each other in the
          order they are given. See `audio profiles
          <https://cloud.google.com/text-to-speech/docs/audio-
          profiles>`__ for current supported profile ids.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.AudioConfig)
    ),
)
_sym_db.RegisterMessage(AudioConfig)

SynthesizeSpeechResponse = _reflection.GeneratedProtocolMessageType(
    "SynthesizeSpeechResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SYNTHESIZESPEECHRESPONSE,
        __module__="google.cloud.texttospeech_v1.proto.cloud_tts_pb2",
        __doc__="""The message returned to the client by the ``SynthesizeSpeech`` method.
  Attributes:
      audio_content:
          The audio data bytes encoded as specified in the request,
          including the header for encodings that are wrapped in
          containers (e.g. MP3, OGG\_OPUS). For LINEAR16 audio, we
          include the WAV header. Note: as with all bytes fields,
          protobuffers use a pure binary representation, whereas JSON
          representations use base64.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1.SynthesizeSpeechResponse)
    ),
)
_sym_db.RegisterMessage(SynthesizeSpeechResponse)


DESCRIPTOR._options = None
_LISTVOICESREQUEST.fields_by_name["language_code"]._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name["input"]._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name["voice"]._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name["audio_config"]._options = None
_VOICESELECTIONPARAMS.fields_by_name["language_code"]._options = None
_AUDIOCONFIG.fields_by_name["audio_encoding"]._options = None
_AUDIOCONFIG.fields_by_name["speaking_rate"]._options = None
_AUDIOCONFIG.fields_by_name["pitch"]._options = None
_AUDIOCONFIG.fields_by_name["volume_gain_db"]._options = None
_AUDIOCONFIG.fields_by_name["sample_rate_hertz"]._options = None
_AUDIOCONFIG.fields_by_name["effects_profile_id"]._options = None

_TEXTTOSPEECH = _descriptor.ServiceDescriptor(
    name="TextToSpeech",
    full_name="google.cloud.texttospeech.v1.TextToSpeech",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\033texttospeech.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform"
    ),
    serialized_start=1355,
    serialized_end=1791,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListVoices",
            full_name="google.cloud.texttospeech.v1.TextToSpeech.ListVoices",
            index=0,
            containing_service=None,
            input_type=_LISTVOICESREQUEST,
            output_type=_LISTVOICESRESPONSE,
            serialized_options=_b(
                "\202\323\344\223\002\014\022\n/v1/voices\332A\rlanguage_code"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="SynthesizeSpeech",
            full_name="google.cloud.texttospeech.v1.TextToSpeech.SynthesizeSpeech",
            index=1,
            containing_service=None,
            input_type=_SYNTHESIZESPEECHREQUEST,
            output_type=_SYNTHESIZESPEECHRESPONSE,
            serialized_options=_b(
                '\202\323\344\223\002\030"\023/v1/text:synthesize:\001*\332A\030input,voice,audio_config'
            ),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_TEXTTOSPEECH)

DESCRIPTOR.services_by_name["TextToSpeech"] = _TEXTTOSPEECH

# @@protoc_insertion_point(module_scope)
