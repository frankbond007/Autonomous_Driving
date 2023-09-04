import carla
import time

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)

    world = client.get_world()

    blueprint_library = world.get_blueprint_library()
    vehicle_blueprint = blueprint_library.find('vehicle.tesla.model3')
    vehicle_blueprint.set_attribute('color', '255,255,255')

    spawn_point = world.get_map().get_spawn_points()[0]

    vehicle = world.spawn_actor(vehicle_blueprint, spawn_point)

    vehicle.apply_control(carla.VehicleControl(throttle=0.5))

    time.sleep(10)

    vehicle.destroy()

if __name__ == '__main__':
    main()
