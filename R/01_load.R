require(data.table)

# Load csv files

clients = fread('raw/cliente_tabla.csv')
products = fread('raw/producto_tabla.csv')
town_state = fread('raw/town_state.csv')
test = fread('raw/test.csv')
train = fread('raw/train.csv')

# Get only the first client ID for each client
clients = clients %>% group_by(Cliente_ID) %>% summarize(NombreCliente = min(NombreCliente))

