## config.ini

Create a file called config.ini with the folowing content

```bash
[mysql]
#
# DEV
#
host = database.ip.address
database = database.password
```

## Virtual Environment

1. easy_install pip
2. pip install virtualenv

3. virtualenv --python=python3 venv // python3 -m venv venv/
4. source venv/bin/activate
5. deactivate

6. pip freeze --local > requirements.txt
7. pip install -r requirements.txt


#### Docker

```bash
docker-compose up --force-recreate --build  && docker-compose down  --remove-orphans

```

#### Docker Dev

```bash
docker-compose -f docker-compose-dev.yaml up --force-recreate --build && docker-compose -f docker-compose-dev.yaml   down --remove-orphans
```

#### Docker Prod

```bash
docker-compose -f docker-compose-prod.yaml up && docker-compose -f docker-compose-prod.yaml down --remove-orphans
```


### From Master to Main

```bash
# Step 1 
# create main branch locally, taking the history from master
git branch -m master main

# Step 2 
# push the new local main branch to the remote repo (GitHub) 
git push -u origin main

# Step 3
# switch the current HEAD to the main branch
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main

git branch -a

# Step 4
# change the default branch on GitHub to main
# https://docs.github.com/en/github/administering-a-repository/setting-the-default-branch

# Step 5
# delete the master branch on the remote
git push origin --delete master

git branch -a
```

ref.: https://stevenmortimer.com/5-steps-to-change-github-default-branch-from-master-to-main/