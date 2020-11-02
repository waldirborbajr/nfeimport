## NFeImport 4.0.1

#### Docker

#### Docker Dev

```bash
docker-compose up --force-recreate --build && docker-compose down --remove-orphans
```

```bash
docker run -it nfeimport:latest /bin/bash
```

#### Docker Prod

```bash
docker-compose -f docker-compose.prod.yaml up && docker-compose -f docker-compose.prod.yaml down --remove-orphans
```

```bash
docker-compose -f docker-compose.prod.yaml up --force-recreate --build && docker-compose -f docker-compose.prod.yaml down --remove-orphans
```

## WARNING 

#### BEWARE

```bash
docker container prune
docker network prune
docker image prune

docker system prune -a
docker image rm $(docker images --format "{{.ID}}" --filter "dangling=true")

Images
docker rmi $(docker images -a -q)
docker images -f dangling=true
docker images purge

Volumes
docker volume ls -f dangling=true
docker volume prune
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