class Car:
	def __init__(self,carId,color,fuelStatus,RepairStatus,brand,numberOfseats):
		self.carId=carId
		self.color=color 
		self.fuelStatus=10
		self.RepairStatus=RepairStatus
		self.brand=brand
		self.numberOfseats=numberOfseats

class CarFactoryService:
	carList = []

	def __init__(self):
		self.carList.append(Car(1,'red',10,'True','Subaru','7'))
		self.carList.append(Car(2,'black',5,'False','Audi','2'))
		self.carList.append(Car(3,'silver',0,'True','Mitsubishi','10'))

	
	def CreatNewCar(self,carId,color,fuelStatus,RepairStatus,brand,numberOfseats):
		creatNCar = []

		car1=Car(4,'white',10,'False','mazda','5')
		creatNCar.append(car1)
		return car1

	def UpdateCarColor(self,color,carId):
		for car in self.carList:
			if(car.carId==carId):
				car.color=color
				return car

	def UpdateCarSeats(self,numberOfseats,carId):
		for car in self.carList:
			if(car.carId==carId):
				car.numberOfseats=numberOfseats
				return car


	def driveAcar(self,carId,fuelStatus):
		if self.fuelStatus == 0:
			print("please refuel your car")
		else:
			self.fuelStatus = fuelStatus-1
			print('you can drive')

	def refuelAcar(self,cardId,fuelStatus):
		if self.fuelStatus == 10:
			print('your tank is full')

		else:
			self.fuelStatus = 10
			print('refueling the car')
	  




	def repairAcar(self,carId,RepairStatus):
		for car in self.carList:
			if(car.carId==carId):
				car.RepairStatus=RepairStatus
				break
