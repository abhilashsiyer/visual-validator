from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
import json


def get_file_url(file_tag, project, branch_name, test_case_name):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    print(file_tag, project, branch_name, test_case_name)

    options = ListAndSearchFileRequestOptions(
        tags=[file_tag, project, branch_name, test_case_name]
    )

    list_files = imagekit.list_files(options=options)
    raw_response = list_files.response_metadata.raw
    print("raw_response", raw_response)

    json_array = json.dumps(raw_response)
    a_list = json.loads(json_array)
    filtered_list = []
    for dictionary in a_list:
        if branch_name in dictionary['tags'] and project in dictionary['tags'] and file_tag in dictionary['tags'] \
                and test_case_name in dictionary['tags']:
            filtered_list.append(dictionary)

    print('filtered_list', filtered_list)

    if filtered_list:
        return filtered_list[0]['url']
    else:
        return "False"


def get_file_id(file_tag, project, branch_name, test_case_name):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    print(file_tag, project, branch_name, test_case_name)

    options = ListAndSearchFileRequestOptions(
        tags=[file_tag, project, branch_name, test_case_name]
    )

    list_files = imagekit.list_files(options=options)
    raw_response = list_files.response_metadata.raw
    print("raw_response", raw_response)

    json_array = json.dumps(raw_response)
    a_list = json.loads(json_array)
    filtered_list = []
    for dictionary in a_list:
        if branch_name in dictionary['tags'] and project in dictionary['tags'] and file_tag in dictionary['tags'] \
                and test_case_name in dictionary['tags']:
            filtered_list.append(dictionary)

    print('filtered_list', filtered_list)

    if filtered_list:
        return filtered_list[0]['fileId']
    else:
        return "False"


def delete_compare_file_if_existing(file_tag, project, branch_name, test_case_name, test_matrix_id):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    options = ListAndSearchFileRequestOptions(
        tags=[file_tag, project, branch_name, test_case_name, test_matrix_id]
    )

    list_files = imagekit.list_files(options=options)

    raw_response = list_files.response_metadata.raw

    if raw_response:
        file_id = raw_response[0]['fileId']
        result = imagekit.delete_file(file_id=file_id)
        print("result", result)
        return {'message': 'Delete success'}
    else:
        return {'message': 'No such file'}
