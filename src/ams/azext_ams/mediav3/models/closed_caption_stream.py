# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .stream_selection import StreamSelection


class ClosedCaptionStream(StreamSelection):
    """Object to represent closed caption stream selection.

    :param file_index: Gets the file index where the stream is present.
    :type file_index: int
    :param stream_index: Gets the stream index.
    :type stream_index: int
    :param is_absolute_stream_index: Gets a value indicating whether the
     stream index is absolute or relative to the stream type.
    :type is_absolute_stream_index: bool
    :param stream_selection_mode: Gets the stream selection mode. Possible
     values include: 'SelectionNotSet', 'SelectHighestBitrateStream',
     'SelectLowestBitrateStream', 'SelectAllStreams'
    :type stream_selection_mode: str or ~accounts.models.StreamSelectionMode
    :param odatatype: Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'file_index': {'required': True},
        'stream_index': {'required': True},
        'odatatype': {'required': True},
    }

    def __init__(self, file_index, stream_index, is_absolute_stream_index=None, stream_selection_mode=None):
        super(ClosedCaptionStream, self).__init__(file_index=file_index, stream_index=stream_index, is_absolute_stream_index=is_absolute_stream_index, stream_selection_mode=stream_selection_mode)
        self.odatatype = '#Microsoft.Media.ClosedCaptionStream'