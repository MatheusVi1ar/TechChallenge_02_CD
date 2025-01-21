from datetime import datetime, timedelta
import util.scrap as scrap
import util.constantes as constantes
import util.aws as aws

def main():
    try:
        datenow = (datetime.now().astimezone() - timedelta(hours=3, minutes=0)).strftime('%Y%m%d')

        # Extract HTML
        try:
            parquet_buffer, datenow = scrap.scrap_html(constantes.url, datenow)
        except Exception as e:
            msg = f"Error extracting HTML: {e}"
            print(msg)
            return(msg)

        # Upload Parquet file to S3
        try:
            aws.enviar_parquet_s3(  parquet_buffer, 
                                    datenow, 
                                    constantes.aws_access_key_id, 
                                    constantes.aws_secret_access_key, 
                                    constantes.aws_session_token)
        except Exception as e:
            msg = f"Error uploading to S3: {e}"
            print(msg)
            return(msg)

    except Exception as e:
        msg = f"Unexpected error: {e}"
        print(msg)
        return(msg)
    return("Success")

if __name__ == '__main__':
    main()

def handler(event, context):
    return main()