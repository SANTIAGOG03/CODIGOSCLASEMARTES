import requests

#CODIGO SANTIAGO GUERRERO

#mediante esta funcion se obtendra el dns de la empresa que se registre mediante la api de ipinfo
def obtenerIpDedeDominio(dominio):
    try:
        print(f"--------- Dominio -> {dominio} -----------")
        url = f"https://networkcalc.com/api/dns/lookup/{dominio}"
        resultadoBusqueda = requests.get(url)
        datos = resultadoBusqueda.json()

        if datos.get('records') and datos['records'].get('A'):
            for record in datos['records']['A']:
                ip = record['address']
                url_ipinfo = f"https://ipinfo.io/{ip}?token=74bc917a25b741"
                resultadoRegion = requests.get(url_ipinfo)
                datos_region = resultadoRegion.json()
                region = datos_region.get('region', 'No disponible')
                print(f"La región de la IP -> {ip} es {region}")
        else:
            print(f"No se encontraron registros A para el dominio {dominio}")
    except requests.RequestException as e:
        print(f"Error al obtener la IP o la región para el dominio {dominio}: {e}")

#mediante el uso de esta funcion y esta api optendremos los emails que contengan la palabra clave que se registra en este caso la de la empresa
def obtenerEmail(dominio):
    try:
        url = f"https://api.hunter.io/v2/domain-search?domain={dominio}&api_key=344ff07dbe78869fe56eba9c0f1ebc3bf225fb08"
        resultadosEmail = requests.get(url)
        datos_email = resultadosEmail.json()

        if datos_email.get("data") and datos_email["data"].get("emails"):
            for correo in datos_email["data"]["emails"]:
                print(f"Correo: {correo['value']}")
        else:
            print(f"No se encontraron correos electrónicos para el dominio {dominio}")
    except requests.RequestException as e:
        print(f"Error al obtener los correos electrónicos para el dominio {dominio}: {e}")


# Lista de dominios de empresas famosas en Colombia
dominios_empresas_colombianas = [
    "ecopetrol.com.co",
    "grupoavvillas.com.co",
    "bancolombia.com",
    "santander.com.co",
    "grupoargos.com.co",
    "nexenta.com",
    "grupoexito.com",
    "celsia.com",
    "caracoltv.com",
    "rcn.com.co",
    "postobon.com.co",
    "avianca.com",
    "sodimac.com.co",
    "bancafianc.com",
    "d1.com.co",
    "supranational.com",
    "tigo.com.co",
    "entelchile.net",
    "colpatria.com.co",
    "carreras.com.co",
    "panamericana.com.co",
    "falabella.com.co",
    "centauro.com.co",
    "samsclub.com.co",
    "carulla.com",
    "mintransporte.gov.co",
    "mueblesdico.com",
    "colfondos.com",
    "pepsi.com.co",
    "mercedesbenz.com.co",
    "renault.com.co",
    "chevrolet.com.co",
    "honda.com.co",
]
#cambiar por el url para obtener los datos de la pagina y la empresa que hayan en internet
for dominio in dominios_empresas_colombianas:
    obtenerIpDedeDominio("honda.com.co")
    obtenerEmail("honda.com.co")
