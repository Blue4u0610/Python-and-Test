"""
Author:Jinfeng Lan
Time:2026/2/16 01:17
Class:SSW 567
Project name:HW 03a
"""
import requests


def get_github_repo(user_id):
    repo_url = f"https://api.github.com/users/{user_id}/repos"

    response = requests.get(repo_url)
    #test if requests works
    if response.status_code != 200:
        return f"Error: Unable to fetch repositories for user {user_id}"


    repos = response.json()
    #get repo form GitHub
    results = []

    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        #fill url

        commit_response = requests.get(commits_url)
        if commit_response.status_code == 200:
            commits = commit_response.json()
            commit_count = len(commits)
            results.append(f"Repo: {repo_name} Number of commits: {commit_count}")

        else:
            results.append(f"Repo: {repo_name} Number of commits: Error")
            #status != 200

    return results


if __name__ == "__main__":
    #print and test
    print("Enter the user's ID:")
    user_id = input()
    user_id = user_id.strip()

    results = get_github_repo(user_id)
    for repo in results:
        print(repo)