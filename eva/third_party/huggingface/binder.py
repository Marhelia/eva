# coding=utf-8
# Copyright 2018-2022 EVA
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
from eva.catalog.models.udf_catalog import UdfCatalogEntry
from eva.third_party.huggingface.create import MODEL_FOR_TASK
from eva.third_party.huggingface.utils import get_metadata_entry


def assign_hf_udf(udf_obj: UdfCatalogEntry):
    """
    Assigns the correct HF Model to the UDF. The model assigned depends on
    the task type for the UDF. This is done so that we can
    process the input correctly before passing it to the HF model.
    """
    inputs = udf_obj.args

    # NOTE: Currently, we only support models that require a single input.
    assert len(inputs) == 1, "Only single input models are supported."

    task = get_metadata_entry(udf_obj, "task")[1]
    model_class = MODEL_FOR_TASK[task]

    return lambda: model_class(udf_obj)
