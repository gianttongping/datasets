# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python2, python3
"""irc_disentanglement dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import irc_disentanglement


class IrcDisentanglementTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = irc_disentanglement.IrcDisentanglement
  SPLITS = {
      "train": 5,  # Number of fake train example
      "validation": 6,  # Number of fake validation example
      "test": 5,  # Number of fake test example
  }


if __name__ == "__main__":
  tfds.testing.test_main()

