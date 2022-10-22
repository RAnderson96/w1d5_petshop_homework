# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dict):
    return dict["name"]

def get_total_cash(dict):
    return dict["admin"]["total_cash"]

def add_or_remove_cash(dict, cash_val):
    dict["admin"]["total_cash"] = get_total_cash(dict) + cash_val
    return dict["admin"]["total_cash"]

def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]

def increase_pets_sold(dict,val):
    dict["admin"]["pets_sold"] = get_pets_sold(dict) + val
    return dict["admin"]["pets_sold"]

def get_stock_count(dict):
    return len(dict["pets"])

def get_pets_by_breed(dict, pet):
    val1 = []
    for val in dict["pets"]:
        if val["breed"] == pet:
            val1.append(val)
    return val1
    
def find_pet_by_name(dict, name):
    for val in dict["pets"]:
        if val["name"] == name:
            return val
    return None

def remove_pet_by_name(dict, name):
    dict["pets"].remove(find_pet_by_name(dict,name))


def add_pet_to_stock(dict, new_pet):
    dict["pets"].append(new_pet)
  
# cash = get_customer_cash(self.customers[0])

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] = get_customer_cash(customer) - cash 
    return customer["cash"] 

def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"] = [new_pet]

def customer_can_afford_pet(customer, new_pet):
    if get_customer_cash(customer) >= new_pet["price"]:
        return True
    return False

def sell_pet_to_customer(dict, pet, customer):
    if pet == None:
        return None 
        
    pet_cost = pet["price"]
    if customer_can_afford_pet(customer,pet):
        remove_customer_cash(customer,pet_cost)
        add_pet_to_customer(customer,pet)
        add_or_remove_cash(dict,pet_cost)
        remove_pet_by_name(dict,pet["name"])
        increase_pets_sold(dict,1)
    