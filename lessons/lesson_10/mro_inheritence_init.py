from time import process_time_ns


class LandTransport:

    def __init__(self, land_wheels, land_steering_wheel):
        self.land_wheels = land_wheels
        self.land_steering_wheel = land_steering_wheel

    def drive(self):
        print("Driving on a Land")

    def honk(self):
        print("Land Transport is honking!")

class WaterTransport:

    def __init__(self, water_sail, water_propeller):
        self.water_sail = water_sail
        self.water_propeller = water_propeller

    def drive(self):
        print("Driving on a Water")

    def honk(self):
        print("Water Transport is honking!")

class AirTransport:

    def __init__(self, air_turbines, air_wings):
        self.air_turbines = air_turbines
        self.air_wings = air_wings

    def drive(self):
        print("Driving on a Air")

    def honk(self):
        print("Air Transport is honking!")

class AmphibiousTransport(LandTransport, WaterTransport):

    def __init__(self, land_wheels, land_steering_wheel, water_sail, water_propeller, amphibious_version):
        LandTransport.__init__(self, land_wheels, land_steering_wheel)
        WaterTransport.__init__(self, water_sail, water_propeller)
        self.amphibious_version = amphibious_version

    def drive(self):
        LandTransport.drive(self)
        WaterTransport.drive(self)

class AirWaterTransport(AirTransport, WaterTransport):

    def __init__(self, air_turbines, air_wings, water_sail, water_propeller, air_water_version):
        AirTransport.__init__(self, air_turbines, air_wings)
        WaterTransport.__init__(self, water_sail, water_propeller)
        self.air_water_version = air_water_version

    def drive(self):
        AirTransport.drive(self)
        WaterTransport.drive(self)

class HybridTransport(AmphibiousTransport, AirWaterTransport):

    def __init__(self, land_wheels, land_steering_wheel, water_sail, water_propeller, amphibious_version, air_turbines, air_wings, air_water_version, hybrid_version, hybrid_model):
        AmphibiousTransport.__init__(self, land_wheels, land_steering_wheel, water_sail, water_propeller, amphibious_version)
        AirWaterTransport.__init__(self, air_turbines, air_wings, water_sail, water_propeller, air_water_version)
        self.hybrid_version = hybrid_version
        self.hybrid_model = hybrid_model


# amphibious = AmphibiousTransport(land_wheels=4, land_steering_wheel=4, water_sail=2, water_propeller=2, amphibious_version="A1")
# amphibious.drive()
#
# air_water_transport = AirWaterTransport(air_turbines=1, air_wings=2, water_sail=1, water_propeller=4, air_water_version="AW1.2")


hybrid = HybridTransport(land_wheels=4,
                         land_steering_wheel=4,
                         water_sail=2,
                         water_propeller=2,
                         amphibious_version="A1",
                         air_turbines=1,
                         air_wings=2,
                         air_water_version="AW1.2",
                         hybrid_version="H1",
                         hybrid_model="Cruiser")


print(HybridTransport.__mro__)
hybrid.drive()
hybrid.honk()