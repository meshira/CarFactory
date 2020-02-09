import pytest
import carfactory


CarFactory_Service=carfactory.CarFactoryService()

def test_UpdateCarColor():
	car=CarFactory_Service.UpdateCarColor('red', 1)

	assert car.color == 'red', "test faild"



def test_CreatNewCar():
	car=CarFactory_Service.CreatNewCar(4,'white',10,'False','mazda','5')

	assert car.brand == 'mazda' , 'test failed'

	#assert car.brand == 'ferrari' , 'test pass'

	assert car.color == 'white' , 'test failed'

	#assert car.color == 'pink' , 'test pass'

def test_CreatNewCar_false():
	car=CarFactory_Service.CreatNewCar(4,'white',10,'False','mazda','5')

	assert car.brand == 'mazda' , 'test pass'

	assert car.color == 'white' , 'test pass'






def test_driveAcar():
	car=CarFactory_Service.driveAcar(1,10)

	assert car.fuelStatus == 10 ,'test failed, you can drive'

	assert car.fuelStatus == 0 , 'test pass, please reful your car ' 


def test_repairAcar():
	car=CarFactory_Service.repairAcar(1,'True')

	assert car.RepairStatus == 'True' , 'test failed'

	assert car.RepairStatus == 'False' , 'test pass'



	car=CarFactory_Service.repairAcar(2,'False')

	assert car.RepairStatus == 'False' , 'test failed'

	assert car.RepairStatus == 'True' , 'test pass'


def test_refuelAcar():
	car1=Subaru.refuelAcar(10)

	assert car1 == 10 , 'test failed , your tank is full'

	assert Subaru == 0 , 'test pass , refueling the car'





