import pandas as pd

# Créditos Arquivo (mac-vendors-export.csv): https://maclookup.app/downloads/csv-database
def classify(list_of_macs):
    df = pd.read_csv('static/mac-vendors-export.csv')
    index = 0
    for mac in list_of_macs:
        mac = mac.replace('-', ':')
        last_index = 8
        df_classifier = df[df['Mac Prefix'].str.startswith(mac[0:last_index])]
        while len(df_classifier) > 1:
            last_index +=1
            df_classifier = df[df['Mac Prefix'].str.startswith(mac[0:last_index])]

        brand = ''
        if df_classifier is not None:
            try:
                brand = df_classifier.iloc[-1]['Vendor Name']
            except:
                pass

        if brand == '':
            brand = 'Marca relacionada ao endereço MAC não encontrada.'

        list_of_macs[index] = ( mac, brand ) 
        index += 1

    return list_of_macs