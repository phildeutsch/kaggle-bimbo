require(dplyr)

# Relationship between demand, sales and returns
sum(train$Demanda_uni_equil != pmax(train$Venta_uni_hoy - train$Dev_uni_proxima, 0))

# Demand = Sales - Returns, but can never be less than zero

