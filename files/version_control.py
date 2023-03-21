#!/usr/bin/env python
# *-* coding: utf-8 *-*
from git import Repo

repo_dir = 'version_control_test/files'
repo = Repo(repo_dir, search_parent_directories=True)
file_list = ['files/text.txx']
commit_message = 'Add simple text file'

def git_push():
    try:
        # repo = Repo(repo_dir)
        # repo.git.add(update=True)
        repo.git.add(file_list)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
