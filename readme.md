# AlgoBot
Lee los mensajes de un espacio de trabajo de Slack. Si interpreta que alguien dice Windows, le responde al mensaje aclarando que no se utiliza ese SO en la cátedra.

## Preparación entorno Slack
Debe crearse una App en api.slack.com e instalarse en el espacio de trabajo que se necesite. Luego mediante  `/invite @nombrebot`, lo añadimos a los canales que deseemos que esté checkeando.

## Instalación
Se necesita python3.

```bash
pip3 install python-dotenv
pip3 install slackclient
pip3 install flask
pip3 install slackeventsapi
```
## Claves
Las claves que se necesitan son:
- SIGNING_SECRET, clave dada por Slack en la info básica de la app.
- SLACK_TOKEN, clave dada por Slack en la parte de autenticaciones de la plataforma de apps de Slack.