#Soal 2
class Model(object): 
  services = { 
      'email': {'number': 1000, 'price': 2,}, 
      'sms': {'number': 1000, 'price': 10,}, 
      'voice': {'number': 1000, 'price': 15,}, 
  } 

#Pengembangan Kode Soal 1 menjadi Kode Soal 2 
class View(object): 
  def list_services(self, services): 
    print("Services Provided:") 
    for svc in services: 
      print(svc,'') 
 
  def list_pricing(self, services):
    print("Pricing for Services:")  
    for svc in services: 
      print("For", Model.services[svc]['number'], 
            svc, "message you pay $", 
            Model.services[svc]['price'])
         
  def list_services2(self, services): 
    print("Layanan yang disediakan:") 
    for svc in services: 
      print(svc,'') 
 
  def list_pricing2(self, services):
    print("Tarif tiap layanan:")  
    for svc in services: 
      print("Untuk", Model.services[svc]['number'], 
            svc, "anda membayar $", 
            Model.services[svc]['price'])  
       
class Controller(object): 
  def __init__(self): 
    self.model = Model() 
    self.view = View() 
 
  def get_services(self): 
    services = self.model.services.keys() 
    if Bahasa == "1":
      return(self.view.list_services(services))
    elif Bahasa == "2":
      return(self.view.list_services2(services)) 
    else:
      print("Error, choose the language number!")
 
  def get_pricing(self): 
    services = self.model.services.keys() 
    if Bahasa == "1":
      return(self.view.list_pricing(services))
    elif Bahasa == "2":
      return(self.view.list_pricing2(services))
    print("Error, choose the language number!")
 
#Instansiasi objek 
controller = Controller()
Bahasa = input("What language do you choose? [1]English [2]Indonesia: ") 
controller.get_services() 
controller.get_pricing() 
