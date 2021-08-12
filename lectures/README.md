## DSI_Lectures

This repo contains all of the topic lectures for the Galvanize 12-week Data Science Immersive Program. Each campus has its own branch. In general the folder structure should follow the curriculum repo structure by day.

This is a large repository; cloning it will take over 2GB (as of June 2021). To speed up cloning and limit the storage space used on your computer (at the expense of not having immediate access to older versions of files) you should make a shallow clone with only most recent commit, like this:

`$ git clone --depth 1 --no-single-branch https://github.com/GalvanizeDataScience/lectures.git`

Or for those using SSH authentication:

`$ git clone --depth 1 --no-single-branch git@github.com:GalvanizeDataScience/lectures.git`

Then the branch associated with the campus lectures you wish to view can be retrieved with:

`$ git checkout branch-of-interest`
