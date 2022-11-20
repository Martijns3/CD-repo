# README.md
[![Deploy](https://github.com/Martijns3/CD-repo/actions/workflows/deploy.yml/badge.svg)](https://github.com/Martijns3/CD-repo/actions/workflows/deploy.yml)


# 3 components of my solution
- [ ] The YAML file in the .github/workflows folder uses Appleboy ssh- action to login on my VPS, using github secrets and then runs the update.sh file on the VPS. 
- [ ] I wrote a small script in the update.sh file, that gives the “git pull” command in the repository folder and after that, gives a service restart command.
- [ ] Because I decided to run the pipeline on a user account on my VPS, I have used visudo to edit the “sudoers” file and authorize  user to give the “systemctl restart service” command without asking for a superuser password. 

# 3 Issues that I encountered 
- [ ] Because my deployment pipeline runs on a user account and not on root, the Gunicorn app didn’t have automatic access to the files in my user folder because of the set permissions. I tried to fix that by creating a group with user and root in it and then set the permissions recursively from the user account point. Immediately I got authentication errors, because with my action I also changed the permissions in the .ssh folder. I was able to solve this by rebuilding the .ssh folder and regenerating the key.
- [ ] Because of the same permissions change mentioned above, Git considered the files in the repository folder as “changed” so I got Git errors because the destination folder was different from the repository on Github. I could fix this by running the “git fetch —all”
and “git reset —hard origin/main” command in the update.sh file. After that, the standard git pull command worked again.
- [ ] While adding the dependencies to the “requirements.txt” file, I didn’t check what would be for example a current version of Flask. After adding Jinja to the list, I ran into compatibility errors between the two. I solved this by checking version compatibility and make the changes accordingly.
