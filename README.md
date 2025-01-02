# Tech Challenge 02 - COM DOCKER

Este projeto extrai conteúdo HTML de uma URL especificada e faz o upload dos dados extraídos, em formato Parquet, para um bucket S3 da Amazon. O processo é projetado para ser acionado em uma data específica.

## Pré-requisitos

Certifique-se de ter o seguinte instalado:

- Python 3.x
- Biblioteca `boto3` para interações com a AWS
- Biblioteca `pandas` para manipulação de dados
- `beautifulsoup4` para parsing de HTML
- `selenium` para web scraping
- `pyarrow` para trabalhar com arquivos Parquet
- `awslambdaric` para o runtime do AWS Lambda

## Descrição

- **app.py**: Este é o script principal que coordena a extração do HTML e o upload para o S3.
- **util/scrap.py**: Contém a função `scrap_html` que extrai conteúdo HTML de uma URL especificada.
- **util/constantes.py**: Contém valores constantes como `url`, `access_key`, `secret_key` e `session_token`.
- **util/aws.py**: Contém a função `enviar_parquet_s3` para fazer o upload do arquivo Parquet para o S3.
- **requirements.txt**: Lista as bibliotecas Python necessárias.

## Como Executar

1. **Configurar Credenciais AWS**:
   Certifique-se de que suas credenciais AWS (`access_key`, `secret_key`, `session_token`) estão corretamente configuradas em `util/constantes.py`.

2. **Instalar Dependências**:
   Use o seguinte comando para instalar as bibliotecas necessárias:
   ```sh
   pip install -r requirements.txt
Executar o Script: Execute o script app.py:

sh
python app.py

