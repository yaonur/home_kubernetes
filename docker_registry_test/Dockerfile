#FROM localhost:30000/collectorv3/collector
FROM python
RUN mkdir "/var/lib/so2"
ENV SO2_DIR /var/lib/so2
ENV SCRIPT_DIR $SO2_DIR/test/docker_registry_test
WORKDIR $SCRIPT_DIR
ENV PYTHONPATH $SCRIPT_DIR
COPY . $SCRIPT_DIR
#RUN pip install -r $SCRIPT_DIR/requirements.txt

CMD python3 $SCRIPT_DIR/test.py