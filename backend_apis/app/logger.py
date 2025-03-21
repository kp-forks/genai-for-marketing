# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Logging functions """

import os
import logging 
from enum import IntEnum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%H:%M:%S'
)

__gaim_logger = logging.getLogger('GAIM')
__gaim_logger.setLevel(logging.INFO)

class TraceLevel(IntEnum):
    """Trace levels Definition """
    OFF = 0
    ON = 1
    VERBOSE = 2 

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'  

def log(msg: str, level: int = TraceLevel.ON):
    if level > 0:
        __gaim_logger.log(logging.INFO, msg)