require(data.table)
require(stringr)

# Options
SAVE_PATH = 'R/data/'
LOAD_PATH = 'raw/'
LOAD_FROM_IMAGE = TRUE

###############################################################################

time_start = Sys.time()
if (LOAD_FROM_IMAGE) {
  cat(str_c(Sys.time(), " Loading images..."))
  clients = readRDS(str_c(SAVE_PATH, "clients.rds"))
  products = readRDS(str_c(SAVE_PATH, "products.rds"))
  town_state = readRDS(str_c(SAVE_PATH, "town_state.rds"))
  test = readRDS(str_c(SAVE_PATH, "test.rds"))
  train = readRDS(str_c(SAVE_PATH, "train.rds"))
  cat("done.\n")
} else {
  # Load csv files
  cat(str_c(Sys.time(), " Loading csv files..."))
  clients = fread('raw/cliente_tabla.csv')
  products = fread('raw/producto_tabla.csv')
  town_state = fread('raw/town_state.csv')
  test = fread('raw/test.csv')
  train = fread('raw/train.csv')
  cat("done.\n")
  
  # Get only the first client ID for each client
  clients = clients %>% group_by(Cliente_ID) %>% summarize(NombreCliente = min(NombreCliente))
  
  # Save to rds files
  saveRDS(clients, str_c(SAVE_PATH, "clients.rds"), compress=FALSE)
  saveRDS(products, str_c(SAVE_PATH, "products.rds"), compress=FALSE)
  saveRDS(town_state, str_c(SAVE_PATH, "town_state.rds"), compress=FALSE)
  saveRDS(test, str_c(SAVE_PATH, "test.rds"), compress=FALSE)
  saveRDS(train, str_c(SAVE_PATH, "train.rds"), compress=FALSE)
}

time_end = Sys.time()
cat(str_c("Total time: ", round(difftime(time_end, time_start, units = "mins"),1), " mins.\n"))

# Clean up
cat(str_c(Sys.time(), " Clean up..."))
rm(list=setdiff(ls(), c("clients", "products", "town_state", "test", "train")))
gc()
cat("done.\n")

    