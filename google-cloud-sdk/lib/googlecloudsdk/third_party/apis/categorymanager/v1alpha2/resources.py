# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://categorymanager.googleapis.com/v1alpha2/'
DOCS_URL = 'https://cloud.google.com/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  ASSETS = (
      'assets',
      'assets/{assetId}',
      {},
      [u'assetId']
  )
  ASSETS_TAG = (
      'assets.tag',
      'assets/{assetId}/annotationTag',
      {},
      [u'assetId']
  )
  OPERATIONS = (
      'operations',
      '{+name}',
      {
          '':
              'operations/{operationsId}',
      },
      [u'name']
  )
  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      [u'projectsId']
  )
  PROJECTS_TAXONOMIES = (
      'projects.taxonomies',
      '{+name}',
      {
          '':
              'projects/{projectsId}/taxonomies/{taxonomiesId}',
      },
      [u'name']
  )
  PROJECTS_TAXONOMIES_ANNOTATIONS = (
      'projects.taxonomies.annotations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/taxonomies/{taxonomiesId}/annotations/'
              '{annotationsId}',
      },
      [u'name']
  )
  TAXONOMYSTORES = (
      'taxonomyStores',
      'taxonomyStores/{taxonomyStoresId}',
      {},
      [u'taxonomyStoresId']
  )
  TAXONOMYSTORES_TAXONOMIES = (
      'taxonomyStores.taxonomies',
      '{+name}',
      {
          '':
              'taxonomyStores/{taxonomyStoresId}/taxonomies/{taxonomiesId}',
      },
      [u'name']
  )
  TAXONOMYSTORES_TAXONOMIES_ANNOTATIONS = (
      'taxonomyStores.taxonomies.annotations',
      '{+name}',
      {
          '':
              'taxonomyStores/{taxonomyStoresId}/taxonomies/{taxonomiesId}/'
              'annotations/{annotationsId}',
      },
      [u'name']
  )

  def __init__(self, collection_name, path, flat_paths, params):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
