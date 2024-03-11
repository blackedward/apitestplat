import re
import subprocess
from datetime import datetime, timedelta
import os
import shutil
import traceback
from collections import Counter, defaultdict
from git import Repo
import git
from common.log import logger
from diskcache import Cache

user_home = os.path.expanduser("~")
rep_url = "http://git.kkpoker.co/server/doc.git"
svn_url = "svn://devsvn.pppoker.net/PPPoker/proto/"
temp_repo = user_home + "/tempcode"
merge_dir = user_home + "/merge"
branches = ["master"]
destination_directory = user_home + '/tempcopile'
cache_file = user_home + "/cachefile"
temp_repo_pp = user_home + "/ppproto/proto"
merge_dir_pp = user_home + "/ppmerge"
destination_directory_pp = user_home + '/ppcopile'


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


def download_and_compile_protos_pp(branch=None):
    ppproto_destination = os.path.dirname(os.path.dirname(__file__)) + "/proto/pp/" + branch

    if os.path.exists(merge_dir_pp):
        shutil.rmtree(merge_dir_pp)
    os.makedirs(merge_dir_pp)
    if os.path.exists(destination_directory_pp):
        shutil.rmtree(destination_directory_pp)
    os.makedirs(destination_directory_pp)
    if not os.path.exists(temp_repo_pp):
        try:
            os.makedirs(temp_repo_pp)
            subprocess.run(["svn", "checkout", svn_url, temp_repo_pp], check=True)
        except Exception as e:
            logger.error(traceback.format_exc())
        logger.info('svn代码不存在，checkout,{}', svn_url)
        if branch == 'trunk':
            move_files(temp_repo_pp + "/trunk", merge_dir_pp)
        else:
            move_files(temp_repo_pp + "/branch/" + branch, merge_dir_pp)
    else:
        try:
            subprocess.run(["svn", "update", temp_repo_pp], check=True)
            logger.info('svn代码已经存在，执行更新')
        except Exception as e:
            logger.error(traceback.format_exc())

        if branch == 'trunk':
            move_files(temp_repo_pp + "/trunk", merge_dir_pp)
        else:
            move_files(temp_repo_pp + "/branch/" + branch, merge_dir_pp)
    compile_proto_files(merge_dir_pp, destination_directory_pp)
    move_compiled_files(destination_directory_pp, ppproto_destination)


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
        shutil.rmtree(temp_repo_path)

    repo = git.Repo.clone_from(repo_url, temp_repo_path)

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


def get_recently_active_branches_pp():
    local_path = user_home + "/ppproto/"
    folder_path = "proto/branch"
    # 构建SVN命令
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # 格式化日期字符串
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    svn_update_command = f"svn update {local_path}/{folder_path}"
    # 构建SVN命令
    svn_command = f"svn log -r{{{start_date_str}}}:{{{end_date_str}}} -v {local_path}/{folder_path}"

    try:
        # 执行SVN命令
        subprocess.run(svn_update_command, shell=True, check=True)

        result = subprocess.run(svn_command, shell=True, capture_output=True, text=True, check=True)
        log_output = result.stdout.splitlines()

        # 解析SVN日志
        folder_activity = defaultdict(int)

        for line in log_output:
            if line.startswith("   A") or line.startswith("   M") or line.startswith("   D"):
                folder = line.split('/')[3].split(' ')[0]  # 提取文件夹名
                folder_activity[folder] += 1
        # 获取最活跃的10个子文件夹
        top_folders = sorted(folder_activity.items(), key=lambda x: x[1], reverse=True)[:9]
        top_folders.append(('trunk', 0))
        logger.info(f"top_folders: {top_folders}")
        return top_folders

    except subprocess.CalledProcessError as e:
        print(f"Error executing SVN command: {e}")
        return None


def get_recently_active_branches_cached(repo_url):
    cache_key = "most_active_branches"
    global_cache = Cache(directory=cache_file)

    logger.info(f"global_cache: {global_cache.get(cache_key, None)}")

    # 检查全局缓存中是否存在键
    if cache_key in global_cache:
        # 从缓存中获取活跃分支数据
        result = global_cache[cache_key]
        logger.info(f"Cache hit! 缓存数据是： {result}")
        return result
    else:
        logger.info("Cache miss!")
        # 从远程仓库获取活跃分支数据
        result = get_remote_active_branches(repo_url)
        global_cache.set(cache_key, result, expire=60 * 60 * 24)

    return result
