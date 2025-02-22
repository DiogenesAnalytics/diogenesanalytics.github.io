[![docker](https://github.com/DiogenesAnalytics/blog_template/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/DiogenesAnalytics/blog_template/actions/workflows/docker-publish.yml)
[![tests](https://github.com/DiogenesAnalytics/blog_template/actions/workflows/tests.yml/badge.svg)](https://github.com/DiogenesAnalytics/blog_template/actions/workflows/tests.yml)

# Jekyll-Jupyter Blog Template
A template for building a blog, written in Jupyter Notebooks, and using Jekyll.

## Project Organization
```
├── _includes            <- Where page-specific CSS files are stored.
├── _jupyter
│   ├── notebooks        <- Jupyter notebooks for conversion are stored here.
│   └── templates        <- Where nbconvert templates are stored.
│
├── _layouts
│   ├── article.html     <- Jekyll template defining articles.
│   └── default.html     <- Jekyll "base" template used in all other templates.
│
├── _posts               <- Where Jekyll markdown posts are stored.
├── assets
│   ├── css              <- Where the "base" CSS file is stored.
│   └── images           <- Where image files are stored.
│
├── favicon              <- Where favicon files are stored.
├── pages
│   └── blog.html        <- Jekyll template defining the blog page.
|
├── tests
|   └── requirements.txt <- Dependencies for running tests.
|
├── .dockerignore        <- Ignore list for building Docker image.
├── .gitignore           <- Ignore list for Git repo.
├── _config.yml          <- The config file for Jekyll.
├── Dockerfile           <- Builds the Docker image used in the Makefile.
├── index.html           <- Jekyll template defining the home/index page.
├── Makefile             <- Makefile with commands like `make build-site`.
└── README.md            <- The top-level README for this project.
```

## Configuration
Here we will discuss how to *customize* the template for your use case.

### Background Image
There are only two keys of the Jekyll `_config.yml` file that you need to consider:
```yml
high_res_image: "/assets/images/YOUR_HIGH_RES_IMAGE"
low_res_image: "/assets/images/YOUR_LOW_RES_IMAGE"
```

These two *keys* represent the *"high resolution"* and *"low resolution"* versions
of your *background image* (respectively).

### Social Links
You can enable the display of your *social media* links by adding the following to the
`_config.yml` file:
```yml
social:
  x-twitter: "https://twitter.com/yourprofile"
  instagram: "https://instagram.com/yourprofile"
  youtube: "https://youtube.com/yourprofile"
```

This will toggle **on** the display of the social media icons in the header.

### Link Preview
In order for the *link preview* feature to work correctly, you must set the
following keys in your `_config.yml` file:
```yml
default_image: "/assets/images/diogenes_preview.q75.webp"
url: "https://yourwebsite.com"
```
The `default_image` key is the **default image** (for the whole *site*).

The `url` key defines the *domain name* and the *protocol* used (i.e. **https**).
It is important that you use both your website domain name *and* the protocol
as shown below:
```yml
url: "https://yourwebsite.com"
```

Optionally, you can set a *custom* **preview image** and **preview excerpt**.
You can set a *custom preview image* in the *Jekyll* syntax in the front of
an article or *Jupyter Notebook*:
```yml
---
title: "My Jekyll Post"
image: "/path/to/custom/preview/image"
---
```
When the **image** key is set in the *Jekyll YAML front matter* then it will
override the `default_image` set in the `_config.yml`.

For the **excerpt** (which is automatically generated by
default). This can be set *manually* in the *Jekyll YAML front matter*
(just like the preview image):
```yml
---
title: "My Jekyll Post"
image: "/path/to/custom/preview/image"
excerpt: "My custom excerpt that previews what the article is about"
---
```
*NOTE*: if the *excerpt* does not render correct automatically, you can always
set it manually in the *Jekyll YAML front matter*.

## Make
Here we will document the different `make` commands defined in the `Makefile`.
All *commands* (excluding the `all` command which is simply executed by
running `make`) are executed by the following format: `make [COMMAND]`. To see
the *contents* of a command that will be executed upon invocation of the
command, simply run `make -n [COMMAND]`.

### Commands
+ `all`: (*aka*: `make`) defaults to converting all UN-converted notebooks
+ `check-docker`: check Docker and host dependencies
+ `check-image-jupyter`: check if the Jupyter Docker image exists
+ `check-image-tests`: check if the Test Docker image exists
+ `check-images`: check all docker images
+ `check-workdir-tests`: confirm working dir is correct in tests image
+ `check-deps-jupyter`: check Jupyter dependencies inside Docker
+ `check-deps-tests`: check test dependencies inside Docker
+ `check-all`: check all dependencies (Docker, Jupyter, Tests)
+ `build-jupyter`: build Jupyter Docker image
+ `build-tests`: build test Docker image
+ `jupyter`: launches the Jupyter notebook development Docker image
+ `execute`: execute all Jupyter notebooks (in place)
+ `convert`: convert all Jupyter notebooks (even if not changed)
+ `check-renamed-images`: check for lingering images
+ `check-renamed-posts`: check for untracked posts
+ `check-renamed`: check all renamed posts/images
+ `clear-renamed-images`: clear lingering images
+ `clear-renamed-posts`: clear renamed posts and their image dirs
+ `clear-renamed`: clear all renamed posts/images
+ `sync`: copy all converted files to necessary directories
+ `sync-check`: sync and check converted files to necessary directories
+ `jekyll`: startup Docker container running Jekyll server
+ `build-site`: build Jekyll static site
+ `pause`: pause PSECS (to pause between commands)
+ `address`: get Docker container address/port
+ `containers`: launch all Docker containers
+ `check-repo-safety`: check if safe dir is setup
+ `checkk-git`: check if Git is installed
+ `commit`: git add/commit all synced files
+ `push`: git push to remote branch
+ `publish`: [ *WARNING* ] convert, sync, commit, and push all at once
+ `safe-repository`: command to mark the repository as safe
+ `list-containers`: list all running containers
+ `stop-containers`: simply stops all running Docker containers
+ `restart-containers`: restart all containers
+ `unsync`: remove all synced files
+ `clear-nb`: simply clears Jupyter notebook output
+ `clear-output`: removes all converted files
+ `clear-jekyll`: removes Jekyll _site/ directory
+ `clean`: combines all clearing commands into one
+ `update-times`: update timestamps to now
+ `reset`: [ *WARNING* ] reverses all changes
+ `print-config`: print info on variables used
+ `lint`: run linters (isort, black, flake8, mypy)
+ `tests`: run full testing suite (pytest, lint)
+ `pytest`: run pytest in Docker container
+ `isort`: run isort in Docker container
+ `black`: run black in Docker container
+ `flake8`: run flake8 in Docker container
+ `mypy`: run mypy in Docker container
+ `install-act`: install act command
+ `check-act`: check if act is installed
+ `run-act-tests`: run GitHub action tests locally
+ `shell`: create interactive shell in Docker container
