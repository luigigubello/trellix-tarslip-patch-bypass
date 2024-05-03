import os
import tarfile

# CVE-2007-4559 Trellix Patch
# https://www.trellix.com/blogs/research/trellix-advanced-research-center-patches-vulnerable-open-source-projects/
# Sample: https://github.com/operator-framework/operator-courier/pull/210


def is_within_directory(directory, target):
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])

    return prefix == abs_directory


def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise Exception("Attempted Path Traversal in Tar File")

    tar.extractall(path, members, numeric_owner=numeric_owner)


def extract_tar_gz(archive_file, extract_path):
    with tarfile.open(archive_file, "r:gz") as tar:
        safe_extract(tar, path=extract_path)


# Usage
archive_file = "/tmp/bypass.tar.gz"
extract_path = "/tmp/result"

extract_tar_gz(archive_file, extract_path)
