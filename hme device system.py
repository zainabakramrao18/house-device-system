# Base device class
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is turned ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is turned OFF.")

    def get_status(self):
        return f"{self.name} - {'ON' if self.is_on else 'OFF'}"


# Light class with brightness control
class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 0

    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} brightness set to {self.brightness}")

    def get_status(self):
        return super().get_status() + f", Brightness: {self.brightness}"


# Fan class with speed control
class Fan(Device):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        print(f"{self.name} speed set to {self.speed}")

    def get_status(self):
        return super().get_status() + f", Speed: {self.speed}"


# Security Camera with motion detection
class SecurityCamera(Device):
    def __init__(self, name):
        super().__init__(name)
        self.recording = False

    def start_recording(self):
        if self.is_on:
            self.recording = True
            print(f"{self.name} started recording.")

    def stop_recording(self):
        self.recording = False
        print(f"{self.name} stopped recording.")

    def get_status(self):
        recording_status = "Recording" if self.recording else "Idle"
        return super().get_status() + f", Status: {recording_status}"


# Main smart home system class
class SmartHomeSystem:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added device: {device.name}")

    def remove_device(self, device_name):
        self.devices = [d for d in self.devices if d.name != device_name]
        print(f"Removed device: {device_name}")

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

    def show_all_status(self):
        print("\nDevice Status Report:")
        for device in self.devices:
            print(device.get_status())


# Example usage
if __name__ == "__main__":
    home = SmartHomeSystem()

    # Create devices
    living_light = Light("Living Room Light")
    bedroom_fan = Fan("Bedroom Fan")
    front_camera = SecurityCamera("Front Door Camera")

    # Add devices
    home.add_device(living_light)
    home.add_device(bedroom_fan)
    home.add_device(front_camera)

    # Turn on and control devices
    living_light.turn_on()
    living_light.set_brightness(70)

    bedroom_fan.turn_on()
    bedroom_fan.set_speed(3)

    front_camera.turn_on()
    front_camera.start_recording()

    # Show current status
    home.show_all_status()

    # Turn off all devices
    home.turn_off_all_devices()

    # Remove a device
    home.remove_device("Bedroom Fan")

    # Final status report
    home.show_all_status()
