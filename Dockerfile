# jupyter base image
FROM quay.io/jupyter/scipy-notebook:lab-4.1.5

# install python libraries available in conda
RUN mamba install --yes \
    'geopandas=0.14.3' \
    'jupyterlab-spellchecker=0.8.4' \
    'treelib=1.7.0' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# install pip only libraries
RUN pip install git+https://github.com/DiogenesAnalytics/blog_utils
