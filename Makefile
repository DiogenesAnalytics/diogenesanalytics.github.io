.PHONY: all check-docker check-image-jupyter check-image-tests check-images \
        check-deps-jupyter check-deps-tests check-all build-jupyter \
        build-tests jupyter execute convert sync jekyll build-site pause \
        address containers commit push publish list-containers stop-containers \
        restart-containers unsync clear-nb clear-output clear-jekyll clean \
        update-times reset print-config lint tests pytest isort black flake8 \
        mypy shell


# Usage:
# make                     # execute and convert all Jupyter notebooks
# make check-docker        # check docker and host dependencies
# make check-image-jupyter # check if the Jupyter Docker image exists
# make check-image-tests   # check if the Test Docker image exists
# make check-images        # check all docker images
# make check-deps-jupyter  # check Jupyter dependencies inside Docker
# make check-deps-tests    # check test dependencies inside Docker
# make check-all           # check all dependencies (Docker, Jupyter, Tests)
# make build-jupyter       # build jupyter Docker image
# make build-tests         # build test docker image
# make jupyter             # startup docker container running jupyter server
# make execute             # execute all jupyter notebooks (in place)
# make convert             # convert all jupyter notebooks (even if not changed)
# make sync                # copy all converted files to necessary directories
# make jekyll              # startup docker container running jekyll server
# make build-site          # build jekyll static site
# make pause               # pause PSECS (to pause between commands)
# make address             # get docker container address/port
# make containers          # launch all docker containers
# make commit              # git add/commit all synced files
# make push                # git push to remote branch
# make publish             # WARNING: convert, sync, commit, and push at once
# make list-containers     # list all running containers
# make stop-containers     # simply stops all running docker containers
# make restart-containers  # restart all containers
# make unsync              # remove all synced files
# make clear-nb            # simply clears jupyter notebook output
# make clear-output        # removes all converted files
# make clear-jekyll        # removes jekyll _site/ directory
# make clean               # combines all clearing commands into one
# make update-times        # update timestamps to now
# make reset               # WARNING: completely reverses all changes
# make print-config        # print info on variables used
# make lint                # run linters
# make tests               # run full testing suite
# make pytest              # run pytest in docker container
# make isort               # run isort in docker container
# make black               # run black in docker container
# make flake8              # run flake8 in docker container
# make mypy                # run mypy in docker container
# make shell               # create interactive shell in docker container


################################################################################
# GLOBALS                                                                      #
################################################################################

# make cli args
OFRMT := markdown
THEME := dark
TMPLT := jekyll_markdown
BASDR := _jupyter
PSTDR := _posts
OUTDR := ${BASDR}/converted
INTDR := ${BASDR}/notebooks
TMPDR := ${BASDR}/templates
DCTNR := $(notdir $(PWD))
LGLVL := WARN
FGEXT := _files
FGSDR := 'assets/images/{notebook_name}${FGEXT}'
GITBR := master
GITRM := origin
PSECS := 5

# extensions available
OEXT_html     = html
OEXT_latex    = tex
OEXT_pdf      = pdf
OEXT_webpdf   = pdf
OEXT_markdown = md
OEXT_rst      = rst
OEXT_script   = py
OEXT_notebook = ipynb
OEXT = ${OEXT_${OFRMT}}

# individual conversion flag variables
LGLFL = --log-level ${LGLVL}
OUTFL = --to ${OFRMT}
THMFL = --theme ${THEME}
TMPFL = --template ${TMPLT}
ODRFL = --output-dir ${OUTDR}
FIGDR = --NbConvertApp.output_files_dir=${FGSDR}
XTRDR = --TemplateExporter.extra_template_basedirs=${TMPDR}
RMTGS = --TagRemovePreprocessor.enabled=True
RMCEL = --TagRemovePreprocessor.remove_cell_tags remove_cell
RMNPT = --TagRemovePreprocessor.remove_input_tags remove_input
RMIPT = --TemplateExporter.exclude_input_prompt=True
RMOPT = --TemplateExporter.exclude_output_prompt=True
RMWSP = --RegexRemovePreprocessor.patterns '\s*\Z'

# check for conditional vars
ifdef NOTMPLT
  undefine TMPFL
endif
ifdef NOTHEME
  undefine THMFL
endif

# combined conversion flag variables
TMPFLGS = ${OUTFL} ${THMFL} ${TMPFL} ${ODRFL} ${FIGDR} ${XTRDR}
RMVFLGS = ${RMTGS} ${RMCEL} ${RMNPT} ${RMIPT} ${RMOPT} ${RMWSP}

# final conversion flag variable
CNVRSNFLGS = ${LGLFL} ${TMPFLGS} ${RMVFLGS}

# notebook-related variables
CURRENTDIR := $(PWD)
NOTEBOOKS  := $(shell find ${INTDR} -name "*.ipynb" -not -path "*/.ipynb_*/*")
OUTPUTFLS  := $(patsubst ${INTDR}/%.ipynb, ${PSTDR}/%.${OEXT}, ${NOTEBOOKS})

# dynamically retrieve the GitHub username, repository name, and branch
GITHUB_USER ?= $(shell dirname `git config --get remote.origin.url` | \
                 sed 's/\:/ /g' | awk '{print $$2}' | cut -d/ -f1 | \
                 tr '[:upper:]' '[:lower:]')
REPO_NAME ?= $(shell basename -s .git `git config --get remote.origin.url`)
GIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)

# docker-related variables
JKLCTNR = jekyll.${DCTNR}
JPTCTNR = jupyter.${DCTNR}
JKYLIMG = jekyll/jekyll:4.2.0
DCKRUSR = 1000:1000
DCKRSRC = /usr/local/src/$(REPO_NAME)
DCKRRUN = docker run --rm -v ${CURRENTDIR}:/home/jovyan -it
DCKRTST = docker run --rm --user ${DCKRUSR} -v ${CURRENTDIR}:${DCKRSRC} -it
DCKRTAG ?= $(GIT_BRANCH)
DCKR_PULL ?= true
DCKR_NOCACHE ?= false
DCKRIMG_BASE ?= ghcr.io/$(GITHUB_USER)/$(REPO_NAME):$(DCKRTAG)
DCKRIMG_JPYTR ?= ${DCKRIMG_BASE}_jupyter
DCKRIMG_TESTS ?= ${DCKRIMG_BASE}_testing

# Define the docker build command with optional --no-cache
define DOCKER_BUILD
	docker build -t $1 . --load --target $2 \
	  $(if $(filter true,$(DCKR_NOCACHE)),--no-cache)
endef

# Function to conditionally pull or build the docker image
define DOCKER_PULL_OR_BUILD
	$(if $(filter true,$(DCKR_PULL)), \
	  docker pull $1 || (echo "Pull failed. Building Docker image for $1..." && \
	  $(call DOCKER_BUILD,$1,$2)), $(call DOCKER_BUILD,$1,$2))
endef

# check for conditional vars to turn off docker
ifdef NODOCKER
  undefine DCKRRUN
  undefine DCKRTST
  undefine DCKRIMG
  undefine DCKRTAG
  undefine DCKRIMG_JPYTR
  undefine DCKRIMG_TESTS
  undefine DOCKER_BUILD
  undefine DOCKER_PULL_OR_BUILD
endif

# jupyter nbconvert vars
NBEXEC = jupyter nbconvert --to notebook --execute --inplace
NBCNVR = jupyter nbconvert ${CNVRSNFLGS}
NBCLER = jupyter nbconvert --clear-output --inplace

################################################################################
# COMMANDS                                                                     #
################################################################################

# define a rule to convert Jupyter notebooks to desired output format
$(PSTDR)/%.$(OEXT): $(INTDR)/%.ipynb
	${DCKRRUN} ${DCKRIMG_JPYTR} ${NBEXEC} $<
	${DCKRRUN} ${DCKRIMG_JPYTR} ${NBCNVR} $<

# define the default target
all: $(OUTPUTFLS)

# check docker and host dependencies
check-docker:
	@ echo "Checking Docker and host dependencies..."
	@ command -v docker > /dev/null || { echo "Docker is missing"; exit 1; }
	@ docker --version || { echo "Docker is not running or accessible"; exit 1; }
	@ echo "Docker is installed and running!"

# check if jupyter docker image exists
check-image-jupyter: check-docker
	@if ! docker images --format "{{.Repository}}:{{.Tag}}" | \
	    grep -q "^${DCKRIMG_JPYTR}$$"; then \
	  echo "Error: Docker image '${DCKRIMG_JPYTR}' is missing."; \
	  echo "Please build it using 'make build-jupyter'."; \
	  exit 1; \
	else \
	  echo "Docker image '${DCKRIMG_JPYTR}' exists."; \
	fi

# check if test docker image exists
check-image-tests: check-docker
	@if ! docker images --format "{{.Repository}}:{{.Tag}}" | \
	    grep -q "^${DCKRIMG_TESTS}$$"; then \
	  echo "Error: Docker image '${DCKRIMG_TESTS}' is missing."; \
	  echo "Please build it using 'make build-tests'."; \
	  exit 1; \
	else \
	  echo "Docker image '${DCKRIMG_TESTS}' exists."; \
	fi

# crouping docker image checks
check-docker-images: check-docker check-image-jupyter check-image-tests

# check jupyter dependencies inside docker
check-deps-jupyter: check-image-jupyter
	@ echo "Checking Jupyter dependencies inside Docker..."
	@ ${DCKRRUN} ${DCKRIMG_JPYTR} sh -c "\
	  command -v jupyter > /dev/null || (echo 'Jupyter is missing' && exit 1) && \
	  python3 -m pip show nbconvert > /dev/null || \
	  (echo 'Python package nbconvert is missing' && exit 1) && \
	  echo 'All Jupyter dependencies are present!' \
	"

# check testing dependencies inside docker
check-deps-tests: check-image-tests
	@ echo "Checking test dependencies inside Docker..."
	@ ${DCKRRUN} ${DCKRIMG_TESTS} sh -c "\
	  command -v bash > /dev/null || (echo 'bash is missing' && exit 1) && \
	  command -v find > /dev/null || (echo 'find is missing' && exit 1) && \
	  command -v git > /dev/null || (echo 'git is missing' && exit 1) && \
		command -v make > /dev/null || (echo 'make is missing' && exit 1) && \
	  command -v rsync > /dev/null || (echo 'rsync is missing' && exit 1) && \
	  command -v jupyter > /dev/null || (echo 'jupyter is missing' && exit 1) && \
	  command -v pytest > /dev/null || (echo 'pytest is missing' && exit 1) && \
	  command -v isort > /dev/null || (echo 'isort is missing' && exit 1) && \
	  command -v flake8 > /dev/null || (echo 'flake8 is missing' && exit 1) && \
	  command -v mypy > /dev/null || (echo 'mypy is missing' && exit 1) && \
	  command -v black > /dev/null || (echo 'black is missing' && exit 1) && \
	  command -v sbase > /dev/null || (echo 'sbase is missing' && exit 1) && \
	  echo 'All testing dependencies are present!' \
	"

# check all dependencies
check-all: check-docker-images check-deps-jupyter check-deps-tests
	@ echo "All dependencies have been checked successfully!"

# build jupyter docker image with conditional pull and build
build-jupyter:
	@ echo "Building Jupyter Docker image..."
	@ $(call DOCKER_PULL_OR_BUILD,${DCKRIMG_JPYTR},jupyter)

# build testing docker image with conditional pull and build
build-tests:
	@ echo "Building Test Docker image..."
	@ $(call DOCKER_PULL_OR_BUILD,${DCKRIMG_TESTS},testing)

# launch jupyter notebook development docker image
jupyter:
	@ if ! docker ps --format={{.Names}} | grep -q "${JPTCTNR}"; then \
	  echo "Launching Jupyter in Docker container -> ${JPTCTNR} ..."; \
	  docker run -d \
	             --rm \
	             --name ${JPTCTNR} \
	             -e PYTHONPATH=/home/jovyan/src \
	             -e JUPYTER_ENABLE_LAB=yes \
	             -p 8888 \
	             -v "${CURRENTDIR}":/home/jovyan \
	             ${DCKRIMG_JPYTR} && \
	  if ! grep -sq "${JPTCTNR}" "${CURRENTDIR}/.running_containers"; then \
	    echo "${JPTCTNR}" >> .running_containers; \
	  fi \
	else \
	  echo "Container already running: ${JPTCTNR}. Try setting DCTNR manually."; \
	fi

# execute all notebooks and store output inplace
execute:
	@ echo "Executing all Jupyter notebooks: ${NOTEBOOKS}"
	@ ${DCKRRUN} ${DCKRIMG_JPYTR} ${NBEXEC} ${NOTEBOOKS}

# convert all notebooks to HTML
convert:
	@ echo "Converting all Jupyter notebooks: ${NOTEBOOKS}"
	@ ${DCKRRUN} ${DCKRIMG_JPYTR} ${NBCNVR} ${NOTEBOOKS}

# sync all converted files to necessary locations in TEssay source
sync:
	@ if ls ${OUTDR} | grep -q ".*\.${OEXT}$$"; then \
	  echo "Moving all jupyter ${OFRMT} files to _posts/:"; \
	  rsync -havP ${OUTDR}/*.${OEXT} ${CURRENTDIR}/_posts/; \
	fi
	@ if [ -d "${OUTDR}/assets" ]; then \
	  echo "Moving all jupyter image files to /assets/images"; \
	  rsync -havP ${OUTDR}/assets/ ${CURRENTDIR}/assets; \
	fi

# launch jekyll local server docker image
jekyll:
	@ if ! docker ps --format={{.Names}} | grep -q "${JKLCTNR}"; then \
	  echo "Launching Jekyll in Docker container -> ${JKLCTNR} ..."; \
	  docker run -d \
	             --rm \
	             --name ${JKLCTNR} \
	             -v ${CURRENTDIR}:/srv/jekyll:Z \
	             -p 4000 \
	             ${JKYLIMG} \
	               jekyll serve && \
	  if ! grep -sq "${JKLCTNR}" "${CURRENTDIR}/.running_containers"; then \
	    echo "${JKLCTNR}" >> .running_containers; \
	  fi \
	else \
	  echo "Container already running: ${JKLCTNR}. Try setting DCTNR manually."; \
	fi

# build jekyll static site
build-site:
	@ echo "Building Jekyll static site ..."
	@ docker run -it \
	           --rm \
	           -v ${CURRENTDIR}:/srv/jekyll:Z \
	           -p 4000 \
	           jekyll/jekyll:4.2.0 \
	             jekyll build && \
	echo "Site successfully built!"

# simply wait for a certain amount of time
pause:
	@ echo "Sleeping ${PSECS} seconds ..."
	@ sleep ${PSECS}

# get containerized server address
address:
	@ if [ -f "${CURRENTDIR}/.running_containers" ]; then \
	while read container; do \
	  if echo "$${container}" | grep -q "${JPTCTNR}"; then \
	    echo "Jupyter server address: $$(docker logs $${container} 2>&1 | \
	          grep http://127.0.0.1 | tail -n 1 | \
	          sed s/:8888/:$$(docker port $${container} | \
	          grep '0.0.0.0:' | awk '{print $$3}' | sed 's/0.0.0.0://g')/g | \
	          tr -d '[:blank:]')"; \
	  elif echo "$${container}" | grep -q "${JKLCTNR}"; then \
	    echo "Jekyll server address: http://0.0.0.0:$$(docker port ${JKLCTNR} | \
	          grep '0.0.0.0:' | awk '{print $$3'} | sed 's/0.0.0.0://g')"; \
	  else \
	    echo "Could not find running container: $${container}." \
	         "Try running: make list-containers"; \
	  fi \
	done < "${CURRENTDIR}/.running_containers"; \
	else \
	  echo ".running_containers file not found. Is a Docker container running?"; \
	fi

# launch all docker containers
containers: jupyter jekyll pause address

# git add and git commit synced files
commit:
	@ echo "Adding and committing recently synced files to Git repository ..."
	@ while read item; do \
	  git add $$item; \
	done < ${BASDR}/.synced_history
	@ git commit -m "Adding new ${OFRMT} posts to repository."

# git push branch to remote
push:
	@ echo "Pushing Git commits to remote ${GITRM} on branch ${GITBR} ..."
	@ git push ${GITRM} ${GITBR}

# super command to convert, sync, commit, and push new jupyter posts
publish: all sync commit push

# list all running containers
list-containers:
	@ if [ -f "${CURRENTDIR}/.running_containers" ]; then \
	echo "Currently running containers:"; \
	while read container; do \
	  echo "-->  $${container}"; \
	done < "${CURRENTDIR}/.running_containers"; \
	else \
	  echo ".running_containers file not found. Is a Docker container running?"; \
	fi

# stop all containers
stop-containers:
	@ if [ -f ${CURRENTDIR}/.running_containers ]; then \
	  echo "Stopping Docker containers ..."; \
	  while read container; do \
	    echo "Container $$(docker stop $$container) stopped."; \
	  done < ${CURRENTDIR}/.running_containers; \
	  rm -f ${CURRENTDIR}/.running_containers; \
	else \
	  echo "${CURRENTDIR}/.running_containers file not found."; \
	fi

# restart all containers
restart-containers: stop-containers containers

# unsync all converted files back to original locations
unsync:
	@ echo "Removing all jupyter converted files from _posts/ and assets/ dirs:"
	@untracked_files="$$(git ls-files --others --exclude-standard)"; \
	posts=$$(echo "$${untracked_files}" | grep "_posts" | grep ".md"); \
	assets=$$(echo "$${untracked_files}" | grep "assets/images" | \
	          grep ".png"); \
	all_files=$$(printf "$${posts}\n$${assets}"); \
	for file in $$all_files; do \
	  if echo "$$file" | grep -q ".*\.${OEXT}$$"; then \
	    rm -f "$${file}"; \
	    echo "Removed -> $$file"; \
	  else \
	    rm -rf "$${file}"; \
	    echo "Removed -> $$file"; \
	  fi \
	done; \
	echo "Unsyncing complete."

# remove output from executed notebooks
clear-nb:
	@ echo "Clearing Jupyter notebook outputs for modified and untracked files..."
	@ modified_files="$$(git diff --name-only HEAD)"; \
	untracked_files="$$(git ls-files --others --exclude-standard)"; \
	all_files=$$(printf "$${modified_files}\n$${untracked_files}" | \
	             grep '\.ipynb$$'); \
	for file in $$all_files; do \
	    echo "Clearing output for $$file"; \
	    ${DCKRRUN} ${DCKRIMG_JPYTR} ${NBCLER} "$$file"; \
	done; \
	echo "Clearing complete."

# delete all converted files
clear-output:
	@ echo "Deleting all converted files."
	@ if [ -d "${CURRENTDIR}/${OUTDR}" ]; then \
	  rm -rf "${CURRENTDIR}/${OUTDR}"; \
	fi

# clean up jekyll _site/ dir
clear-jekyll:
	@ echo "Removing Jekyll static site directory."
	@ rm -rf ${CURRENTDIR}/_site

# cleanup everything
clean: clear-output clear-nb clear-jekyll

# update timestamps to now
update-times:
	touch _posts/*.${OEXT}

# reset to original state undoing all changes
reset: unsync clean

# print info on variables used
print-config:
	@ echo "GitHub User: $(GITHUB_USER)"
	@ echo "Repository Name: $(REPO_NAME)"
	@ echo "Git Branch: $(GIT_BRANCH)"
	@ echo "Docker Source Path: $(DCKRSRC)"
	@ echo "Docker Jupyter Image: $(DCKRIMG_JPYTR)"
	@ echo "Docker Testing Image: $(DCKRIMG_TESTS)"
	@ echo "Docker Tag: $(DCKRTAG)"
	@ echo "Current Directory: $(CURRENTDIR)"
	@ echo "Jupyter Docker Container: $(JPTCTNR)"
	@ echo "Jekyll Docker Container: $(JKLCTNR)"
	@ echo "Output Directory: $(OUTDR)"
	@ echo "Sync Directory: ${BASDR}/converted"
	@ echo "Pause Time (PSECS): $(PSECS)"

# run linters
lint: isort black flake8 mypy

# run full testing suite
tests: pytest lint

# run pytest in docker container
pytest:
	@ ${DCKRTST} ${DCKRIMG_TESTS} pytest

# run isort in docker container
isort:
	@ ${DCKRTST} ${DCKRIMG_TESTS} isort tests/

# run black in docker container
black:
	@ ${DCKRTST} ${DCKRIMG_TESTS} black tests/

# run flake8 in docker container
flake8:
	@ ${DCKRTST} ${DCKRIMG_TESTS} flake8 --config=tests/.flake8

# run mypy in docker container
mypy:
	@ ${DCKRTST} ${DCKRIMG_TESTS} mypy --ignore-missing-imports tests/

# create interactive shell in docker container
shell:
	@ ${DCKRTST} ${DCKRIMG_TESTS} bash || true
