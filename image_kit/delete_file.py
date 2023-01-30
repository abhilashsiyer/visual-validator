from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
import json


def delete_file(file_id):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )
    result = imagekit.delete_file(file_id=file_id)

    # Final Result
    print(result)

    # Raw Response
    print(result.response_metadata.raw)
