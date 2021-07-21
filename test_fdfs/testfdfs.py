from fdfs_client.client import get_tracker_conf, Fdfs_client


def main():
    tracker_conf = get_tracker_conf('res/fastfdfs_client.conf')
    client = Fdfs_client(tracker_conf)

    """
    文件上传返回格式
    {
        'Group name': b 'group1',
        'Remote file_id': b 'group1/M00/AD/BA/rBAEUmD3whGACkiyAAAAA7KUrj0796.txt',
        'Status': 'Upload successed.',
        'Local file name': 'res/upload.txt',
        'Uploaded size': '3B',
        'Storage IP': b '172.16.4.82'
    }
    """
    up_result = client.upload_by_filename('res/upload.txt')
    print(f'upload file result = {up_result}')

    """
    文件下载返回格式
    {
        'Remote file_id': b 'group1/M00/AD/BA/rBAEUmD3whGACkiyAAAAA7KUrj0796.txt',
        'Content': 'res/down.txt',
        'Download size': '3B',
        'Storage IP': b '172.16.4.82'
    }
    """
    down_result = client.download_to_file('res/down.txt', up_result['Remote file_id'])
    print(f'down file result = {down_result}')

    """
    文件删除返回
    ('Delete file successed.', b'group1/M00/AD/BA/rBAEUmD3whGACkiyAAAAA7KUrj0796.txt', b'172.16.4.82')
    """
    del_result = client.delete_file(up_result['Remote file_id'])
    print(f'del file result = {del_result}')

    """
    列出所有的group信息
    {'Groups count': 1.0, 'Groups': [ < fdfs_client.tracker_client.Group_info object at 0x0000011541508A30 >]}
    """
    group_result = client.list_all_groups()
    print(f'group info = {group_result}')

    """
    列出同一组内的storage servers信息
    {'Group name': b'group1', 'Servers': [<fdfs_client.tracker_client.Storage_info object at 0x00000115415348B0>]}
    """
    result = client.list_servers(b'group1', up_result['Storage IP'])
    print(f'storage servers info = {result}')


if __name__ == '__main__':
    main()
