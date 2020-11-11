FROM wls12-cluster:latest
LABEL maintainer="edouard.lenglart@gmail.com"
LABEL weblogic_version="12.2.1.4"

COPY --chown=oracle:oracle resources/* /var/opt/oracle/wlst/