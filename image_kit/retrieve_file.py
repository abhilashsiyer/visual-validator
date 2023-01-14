from imagekitio import ImageKit
import asyncio
import time

def get_file_url(tag_name):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )
    # imagekit.list_files({"tags": ["sale", "summer"]})
    list_files = imagekit.list_files({"tags": ["tag-" + tag_name]})
    response = list_files['response']
    print('response')
    print(response)
    if len(response) == 0:
        return False
    if len(response) != 0:
        print("List files-", "\n", list_files['response'][0]['url'])
        url = list_files['response'][0]['url']
        return url


async def delete_existing_file(tag_name):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )
    list_files = imagekit.list_files({"tags": ["tag-" + tag_name]})
    response = list_files['response']

    if len(response) != 0:
        file_id = list_files['response'][0]['fileId']
        result = imagekit.delete_file(file_id=file_id)
        return result
        # handle if length is more than 1
