FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install joblib==1.5.1
RUN pip install numpy==2.2.3
RUN pip install pandas==2.3.0
RUN pip install rdkit==2024.9.5
RUN pip install scikit_learn==1.6.1

WORKDIR /repo
COPY . /repo
