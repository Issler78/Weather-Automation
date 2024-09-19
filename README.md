# Automação Climática com API

Este projeto é uma automação feita com Python, que consiste basicamente em coletar dados meteorológicos (temperatura mínima, temperatura máxima, vento, possibilidade de chuva, etc) de uma API de clima (Weather API) e, após isso, mandar um email para um destinatário específico.
>[!TIP]
>Lembrando que, combinando esta automação com o Task Scheduler do Windows, o programa enviará o email todos os dias (ou em dias que você definir) em horários que podem ser definidos por você.

## Funcionalidades

- Coletar dados meteorológicos a partir de uma API
- Enviar email para um destinatário específico com os dados coletados

## Requisitos

- Ter uma conta no [Weather API](https://www.weatherapi.com/) para ter sua chave da API
- Python 3
- Instalar as Bibliotecas **Requests** e **Python-Dotenv**.

  No Windows e Linux:
  ```
  pip install requests python-dotenv
  ```

  No Mac:
  ```
  pip3 install requests python-dotenv
  ```

## Screenshots
<img src="https://github.com/user-attachments/assets/3dd0df32-f0d3-4b33-b935-f41e6f97570e" alt="Email recebido com os dados meteorológicos" width="300" />
