FROM public.ecr.aws/lambda/python:3.9.2022.12.14.07

RUN yum install freetype-devel amazon-linux-extras -y \
 && PYTHON=python2 amazon-linux-extras install epel -y \
 && yum install --enablerepo=epel libraqm -y

# COPY samonji-0.1.0-py3-none-any.whl .
# RUN pip3 install samonji-0.1.0-py3-none-any.whl --target ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip3 install -r requirements.txt -t ${LAMBDA_TASK_ROOT}

COPY pet.py store.py user.py ${LAMBDA_TASK_ROOT}
# COPY fonts ${LAMBDA_TASK_ROOT}/fonts
# COPY fonts /tmp/

CMD [ "app.hello_world" ]
