from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions


def get_file_url(file_tag, project, branch_name, test_matrix_id="default"):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    print(file_tag, project, branch_name, test_matrix_id)

    options = ListAndSearchFileRequestOptions(
        tags=[file_tag, project, branch_name, test_matrix_id]
    )

    list_files = imagekit.list_files(options=options)
    raw_response = list_files.response_metadata.raw
    if raw_response:
        return raw_response[0]['url']
    else:
        return False


def delete_compare_file_if_existing(file_tag, project, branch_name, test_matrix_id):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    options = ListAndSearchFileRequestOptions(
        tags=[file_tag, project, branch_name, test_matrix_id]
    )

    list_files = imagekit.list_files(options=options)

    raw_response = list_files.response_metadata.raw

    if raw_response:
        file_id = raw_response[0]['fileId']
        result = imagekit.delete_file(file_id=file_id)
        return result
    else:
        return {'message': 'No such file'}
