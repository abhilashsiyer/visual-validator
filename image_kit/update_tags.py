from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
import json


def add_tag(file_ids, tags):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )
    result = imagekit.add_tags(file_ids=file_ids, tags=tags)

    # Final Result
    print(result)

    # Raw Response
    print(result.response_metadata.raw)

    # list successfully updated file ids
    print(result.successfully_updated_file_ids)

    # print the first file's id
    print(result.successfully_updated_file_ids[0])


def remove_tag(file_ids, tags):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )
    result = imagekit.remove_tags(file_ids=file_ids, tags=tags)

    # Final Result
    print(result)

    # Raw Response
    print(result.response_metadata.raw)

    # list successfully updated file ids
    print(result.successfully_updated_file_ids)

    # print the first file's id
    print(result.successfully_updated_file_ids[0])
