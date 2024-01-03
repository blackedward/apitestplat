import multiprocessing
import subprocess
import os

from common.GenerateProto import download_and_compile_protos

user_home = os.path.expanduser("~")
rep_url = "http://git.kkpoker.co/server/doc.git"
temp_repo = user_home + "/tempcode"
merge_dir = user_home + "/merge"
branches = ["master"]
destination_directory = user_home + '/tempcopile'


def download_and_compile(branch):
    try:
        subprocess.run(download_and_compile_protos(branch), capture_output=True, check=True)
    except Exception as e:
        print(f"Error in branch {branch}: {e}")


if __name__ == "__main__":
    user_provided_branches = ["master", "20231130-fix-master", "20231219-opt-enterroom"]

    processes = []
    for branch in user_provided_branches:
        process = multiprocessing.Process(target=download_and_compile, args=branch)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All branches processed.")
