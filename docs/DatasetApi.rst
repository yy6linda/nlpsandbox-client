
datanode.DatasetApi
===================

All URIs are relative to *http://example.com/api/v1*

.. list-table::
   :header-rows: 1

   * - Method
     - HTTP request
     - Description
   * - `\ **create_dataset** <DatasetApi.md#create_dataset>`_
     - **POST** /datasets
     - Create a dataset
   * - `\ **delete_dataset** <DatasetApi.md#delete_dataset>`_
     - **DELETE** /datasets/{datasetId}
     - Delete a dataset by ID
   * - `\ **get_dataset** <DatasetApi.md#get_dataset>`_
     - **GET** /datasets/{datasetId}
     - Get a dataset by ID
   * - `\ **list_datasets** <DatasetApi.md#list_datasets>`_
     - **GET** /datasets
     - Get all datasets


**create_dataset**
======================

..

   Dataset create_dataset(dataset_id, dataset=dataset)


Create a dataset

Create a dataset with the name specified

Example
^^^^^^^

.. code-block:: python

   from __future__ import print_function
   import time
   import datanode
   from datanode.rest import ApiException
   from pprint import pprint
   # Defining the host is optional and defaults to http://example.com/api/v1
   # See configuration.py for a list of all supported configuration parameters.
   configuration = datanode.Configuration(
       host = "http://example.com/api/v1"
   )


   # Enter a context with an instance of the API client
   with datanode.ApiClient() as api_client:
       # Create an instance of the API class
       api_instance = datanode.DatasetApi(api_client)
       dataset_id = 'awesome-dataset' # str | The ID of the dataset that is being created.
   dataset = datanode.Dataset() # Dataset |  (optional)

       try:
           # Create a dataset
           api_response = api_instance.create_dataset(dataset_id, dataset=dataset)
           pprint(api_response)
       except ApiException as e:
           print("Exception when calling DatasetApi->create_dataset: %s\n" % e)

Parameters
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Notes
   * -  **dataset_id**
     - **str**
     - The ID of the dataset that is being created.
     - 
   * -  **dataset**
     - `\ **Dataset** <Dataset.md>`_
     - 
     - [optional] 


Return type
^^^^^^^^^^^

`\ **Dataset** <Dataset.md>`_

Authorization
^^^^^^^^^^^^^

No authorization required

HTTP request headers
^^^^^^^^^^^^^^^^^^^^


* **Content-Type**\ : application/json
* **Accept**\ : application/json

HTTP response details
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Status code
     - Description
     - Response headers
   * - 


**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |
**409** | The request conflicts with current state of the target resource |  -  |

`[Back to top] <#>`_ `[Back to API list] <../README.md#documentation-for-api-endpoints>`_ `[Back to Model list] <../README.md#documentation-for-models>`_ `[Back to README] <../README.md>`_

**delete_dataset**
======================

..

   Dataset delete_dataset(dataset_id)


Delete a dataset by ID

Deletes the dataset for a given ID

Example
^^^^^^^

.. code-block:: python

   from __future__ import print_function
   import time
   import datanode
   from datanode.rest import ApiException
   from pprint import pprint
   # Defining the host is optional and defaults to http://example.com/api/v1
   # See configuration.py for a list of all supported configuration parameters.
   configuration = datanode.Configuration(
       host = "http://example.com/api/v1"
   )


   # Enter a context with an instance of the API client
   with datanode.ApiClient() as api_client:
       # Create an instance of the API class
       api_instance = datanode.DatasetApi(api_client)
       dataset_id = 'dataset_id_example' # str | The ID of the dataset

       try:
           # Delete a dataset by ID
           api_response = api_instance.delete_dataset(dataset_id)
           pprint(api_response)
       except ApiException as e:
           print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)

Parameters
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Notes
   * -  **dataset_id**
     - **str**
     - The ID of the dataset
     - 


Return type
^^^^^^^^^^^

`\ **Dataset** <Dataset.md>`_

Authorization
^^^^^^^^^^^^^

No authorization required

HTTP request headers
^^^^^^^^^^^^^^^^^^^^


* **Content-Type**\ : Not defined
* **Accept**\ : application/json

HTTP response details
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Status code
     - Description
     - Response headers
   * - 


**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

`[Back to top] <#>`_ `[Back to API list] <../README.md#documentation-for-api-endpoints>`_ `[Back to Model list] <../README.md#documentation-for-models>`_ `[Back to README] <../README.md>`_

**get_dataset**
===================

..

   Dataset get_dataset(dataset_id)


Get a dataset by ID

Returns the dataset for a given ID

Example
^^^^^^^

.. code-block:: python

   from __future__ import print_function
   import time
   import datanode
   from datanode.rest import ApiException
   from pprint import pprint
   # Defining the host is optional and defaults to http://example.com/api/v1
   # See configuration.py for a list of all supported configuration parameters.
   configuration = datanode.Configuration(
       host = "http://example.com/api/v1"
   )


   # Enter a context with an instance of the API client
   with datanode.ApiClient() as api_client:
       # Create an instance of the API class
       api_instance = datanode.DatasetApi(api_client)
       dataset_id = 'dataset_id_example' # str | The ID of the dataset

       try:
           # Get a dataset by ID
           api_response = api_instance.get_dataset(dataset_id)
           pprint(api_response)
       except ApiException as e:
           print("Exception when calling DatasetApi->get_dataset: %s\n" % e)

Parameters
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Notes
   * -  **dataset_id**
     - **str**
     - The ID of the dataset
     - 


Return type
^^^^^^^^^^^

`\ **Dataset** <Dataset.md>`_

Authorization
^^^^^^^^^^^^^

No authorization required

HTTP request headers
^^^^^^^^^^^^^^^^^^^^


* **Content-Type**\ : Not defined
* **Accept**\ : application/json

HTTP response details
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Status code
     - Description
     - Response headers
   * - 


**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

`[Back to top] <#>`_ `[Back to API list] <../README.md#documentation-for-api-endpoints>`_ `[Back to Model list] <../README.md#documentation-for-models>`_ `[Back to README] <../README.md>`_

**list_datasets**
=====================

..

   PageOfDatasets list_datasets(limit=limit, offset=offset)


Get all datasets

Returns the datasets

Example
^^^^^^^

.. code-block:: python

   from __future__ import print_function
   import time
   import datanode
   from datanode.rest import ApiException
   from pprint import pprint
   # Defining the host is optional and defaults to http://example.com/api/v1
   # See configuration.py for a list of all supported configuration parameters.
   configuration = datanode.Configuration(
       host = "http://example.com/api/v1"
   )


   # Enter a context with an instance of the API client
   with datanode.ApiClient() as api_client:
       # Create an instance of the API class
       api_instance = datanode.DatasetApi(api_client)
       limit = 10 # int | Maximum number of results returned (optional) (default to 10)
   offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)

       try:
           # Get all datasets
           api_response = api_instance.list_datasets(limit=limit, offset=offset)
           pprint(api_response)
       except ApiException as e:
           print("Exception when calling DatasetApi->list_datasets: %s\n" % e)

Parameters
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Notes
   * -  **limit**
     - **int**
     - Maximum number of results returned
     - [optional] [default to 10]
   * -  **offset**
     - **int**
     - Index of the first result that must be returned
     - [optional] [default to 0]


Return type
^^^^^^^^^^^

`\ **PageOfDatasets** <PageOfDatasets.md>`_

Authorization
^^^^^^^^^^^^^

No authorization required

HTTP request headers
^^^^^^^^^^^^^^^^^^^^


* **Content-Type**\ : Not defined
* **Accept**\ : application/json

HTTP response details
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Status code
     - Description
     - Response headers
   * - 


**200** | Success |  -  |
**403** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

`[Back to top] <#>`_ `[Back to API list] <../README.md#documentation-for-api-endpoints>`_ `[Back to Model list] <../README.md#documentation-for-models>`_ `[Back to README] <../README.md>`_
