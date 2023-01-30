from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions


def upload_image(image, file_tag, project, branch_name, test_case_name, test_matrix_id="default"):
    imagekit = ImageKit(
        private_key='private_Gufvw5TqIpJXCHLXsflAmIhjsJU=',
        public_key='public_T79KXeQeARDMxvGEm70zJ2Zk6FY=',
        url_endpoint='https://ik.imagekit.io/it41uxh5d'
    )

    options = UploadFileRequestOptions(
        response_fields=["is_private_file", "tags"],
        tags=[file_tag, project, branch_name, test_matrix_id, test_case_name]
    )

    upload = imagekit.upload_file(
        file=image,
        file_name=file_tag+project+branch_name+test_case_name+test_matrix_id,
        options=options
    )

    raw_response = upload.response_metadata.raw

    print("Upload response", upload.response_metadata.raw)

    download_url = raw_response['url']

    return download_url
