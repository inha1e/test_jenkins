FROM python:latest

WORKDIR /selenium/Downloads

RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -O ./chromedriver.zip

RUN unzip ./chromedriver.zip | \
        ln -s ./chromedriver /usr/local/bin/ | \
        wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub | \
        mkdir /etc/apt/keyrings

RUN gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub | \
        echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update

RUN apt-get install -y google-chrome-stable

RUN pip install selenium pytest

WORKDIR /selenium

COPY . .

CMD python test.py
