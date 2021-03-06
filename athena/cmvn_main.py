# coding=utf-8
# Copyright (C) ATHENA AUTHORS
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# Only support tensorflow 2.0
# pylint: disable=invalid-name, no-member
r""" a sample implementation of LAS for HKUST """
import sys
import json
import tensorflow as tf
from absl import logging
from athena.main import parse_config, SUPPORTED_DATASET_BUILDER

if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    tf.random.set_seed(1)

    jsonfile = sys.argv[1]
    with open(jsonfile) as file:
        config = json.load(file)
    p = parse_config(config)
    p.dataset_config['speed_permutation'] = [1.0] # cause no redundent computation
    csv_file = sys.argv[2]
    dataset_builder = SUPPORTED_DATASET_BUILDER[p.dataset_builder](p.dataset_config)
    dataset_builder.load_csv(csv_file).compute_cmvn_if_necessary(True)
