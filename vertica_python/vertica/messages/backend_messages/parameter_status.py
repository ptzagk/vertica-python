# Copyright (c) 2013-2017 Uber Technologies, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division, absolute_import

from struct import unpack

from ..message import BackendMessage


class ParameterStatus(BackendMessage):
    message_id = b'S'

    def __init__(self, data):
        BackendMessage.__init__(self)
        null_byte = data.find(b'\x00')
        unpacked = unpack('{0}sx{1}sx'.format(null_byte - 1, len(data) - null_byte - 1), data)
        self.name = unpacked[0]
        self.value = unpacked[1]


BackendMessage.register(ParameterStatus)
