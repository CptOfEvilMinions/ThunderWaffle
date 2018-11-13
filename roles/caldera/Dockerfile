FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install python3-pip python3-dev git wget -y

RUN mkdir /opt/caldera
RUN git clone https://github.com/mitre/caldera.git /opt/caldera

WORKDIR /opt/caldera/caldera
RUN pip3 install --upgrade pip
RUN sed -i 's#aiohttp==2.3.2#aiohttp==2.3.8#g' requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir -p ../dep/crater/crater
RUN wget https://github.com/mitre/caldera-crater/releases/download/v0.1.0/CraterMainWin8up.exe -O ../dep/crater/crater/CraterMain.exe

EXPOSE 8888

CMD ["python3","caldera.py","--database.host","mongo"]