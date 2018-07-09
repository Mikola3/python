# Python Flask app on Azure App Service Web

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service Web.

This repository can directly be deployed to Azure App Service.

For more information, please see the [Python on App Service Quickstart docs](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python).

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Usage
export FLASK_APP=main.py
flask run --host=192.168.56.15
192.168.56.15 - ip хоста, с которого запускается скрипт.
Данный ip должен быть в одной подсети с Artifactory.

http://192.168.56.15:5000/ - здесь видны все файлы
Добавляем этот ip в качестве удаленной репозитории
Файлы отображаются, но не скачиваются. Причина была в том, что надо было полностью отключить проксю в Артифактори.

Схема работы: локальный Артифактори -> локальный Flask -> внешний storage на Azure.

flask run --host=192.168.56.15 & - сервис запущен в бекграунде, но логи идут в режиме real-time.

ps - видим процесс, запущенный в бекграунде.
