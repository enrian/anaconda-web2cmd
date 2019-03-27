FROM continuumio/anaconda3
RUN mkdir /script/
COPY web2cmd.py /script/
CMD ['python2', '/script/web2cmd.py']
