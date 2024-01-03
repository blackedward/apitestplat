import re
from datetime import datetime, timedelta
import os
import shutil
import traceback
from collections import Counter
from git import Repo
import git
from common.log import logger
from diskcache import Cache

user_home = os.path.expanduser("~")
rep_url = "http://git.kkpoker.co/server/doc.git"
temp_repo = user_home + "/tempcode"
merge_dir = user_home + "/merge"
branches = ["master"]
destination_directory = user_home + '/tempcopile'
cache_file = user_home + "/cachefile"
global_cache = Cache(cache_file, expire=24 * 60 * 60)


def download_and_compile_protos(branch=None):
    code_destination = os.path.dirname(os.path.dirname(__file__)) + "/proto/" + branch

    if os.path.exists(merge_dir):
        shutil.rmtree(merge_dir)
    os.makedirs(merge_dir)
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
    os.makedirs(destination_directory)
    if not os.path.exists(temp_repo):
        try:
            os.makedirs(temp_repo)
            repo = Repo.clone_from(rep_url, temp_repo)
        except Exception as e:
            logger.error(traceback.format_exc())
        repo.git.checkout(branch)
        logger.info('代码不存在，执行克隆，checkout的分支名称是： ' + branch)
        move_files(temp_repo + "/proto/inner", merge_dir)
        move_files(temp_repo + "/proto/trunk", merge_dir)
    else:
        try:
            repo = Repo(temp_repo)
            repo.git.reset("--hard")
            repo.git.checkout(branch)
            repo.git.pull("origin", branch)
            logger.info('代码已经存在，执行更新，pull的分支名称是： ' + branch)
        except Exception as e:
            logger.error(traceback.format_exc())

        move_files(temp_repo + "/proto/inner", merge_dir)
        move_files(temp_repo + "/proto/trunk", merge_dir)
    compile_proto_files(merge_dir, destination_directory)
    move_compiled_files(destination_directory, code_destination)


def update_proto_file(proto_file_path, new_prefix):
    # 读取原始.proto文件内容
    with open(proto_file_path, 'r') as file:
        content = file.read()

    # 修改 import 语句的路径
    import_pattern = re.compile(r'^\s*import\s+"([^"]+)"\s*;', re.MULTILINE)
    content = import_pattern.sub(lambda match: f'import "{new_prefix}_{match.group(1)}";', content)

    # 写回.proto文件
    with open(proto_file_path, 'w') as file:
        file.write(content)


def compile_proto_files(source_directory, destination_directory):
    os.chdir(source_directory)
    replace_deprecated(source_directory)

    proto_files = [f for f in os.listdir(source_directory) if f.endswith(".proto")]
    logger.info(f"proto_files: {proto_files}")
    for proto_file in proto_files:
        protoc_command = f"/usr/local/bin/protoc -I={source_directory} --python_out={destination_directory} {proto_file}"
        os.system(protoc_command)


def move_compiled_files(source_directory, destination_directory):
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
    os.makedirs(destination_directory)

    for file_name in os.listdir(source_directory):
        src_file = os.path.join(source_directory, file_name)
        dest_file = os.path.join(destination_directory, file_name)
        shutil.move(src_file, dest_file)


def move_files(source_folder, destination_folder):
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取源文件夹下的所有文件
    files = os.listdir(source_folder)

    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # 移动文件
        shutil.move(source_path, destination_path)


def replace_deprecated(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".proto"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace('[deprecated=true]', '')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)


def get_remote_active_branches(repo_url):
    days = 10
    # 克隆远程仓库到临时目录
    temp_repo_path = user_home + '/tempcodeforbranch'
    if os.path.exists(temp_repo_path):
        # 如果目录存在，执行更新
        repo = git.Repo(temp_repo_path)
        repo.remotes.origin.pull()
    else:
        # 如果目录不存在，执行克隆
        repo = git.Repo.clone_from(repo_url, temp_repo_path)

    repo.remotes.origin.fetch()
    current_date = datetime.now()
    # 获取所有分支
    branches = [str(remote_branch).split('/')[-1] for remote_branch in repo.remotes.origin.refs]
    # 初始化一个字典用于存储每个分支的提交数量
    commit_counts = {branch: 0 for branch in branches}

    # 遍历每个分支，获取提交数量
    for branch in branches:
        try:
            if branch == 'HEAD':
                continue
            # 获取分支的提交数量
            recent_commits = list(repo.iter_commits(f"origin/{branch}", since=f"{days} days ago"))
            # 计算最近10天的提交数量
            commit_counts[branch] = len(recent_commits)
        except git.GitCommandError:
            # 处理无效分支等错误
            pass

    # 找到最活跃的分支
    most_active_branches = Counter(commit_counts).most_common(10)
    logger.info(f"since {current_date} 10 days most_active_branches: {most_active_branches}")
    return most_active_branches


def get_recently_active_branches_cached(repo_url):
    cache_key = "most_active_branches"

    # 检查全局缓存中是否存在键
    if cache_key in global_cache:
        # 从缓存中获取活跃分支数据
        cached_result = global_cache[cache_key]
        logger.info(f"Cache hit! 缓存数据是： {cached_result}")
        return cached_result
    else:
        logger.info("Cache miss!")

    # 如果全局缓存中不存在，进行计算
    result = get_remote_active_branches(repo_url)

    # 将计算结果存入全局缓存
    global_cache[cache_key] = result

    return result
