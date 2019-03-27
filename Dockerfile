FROM continuumio/anaconda3
RUN mkdir /script/
COPY web2cmd.py /script/
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
