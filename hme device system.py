# smart_home.py

"""
Smart Home Automation System
This script defines a modular system to control smart devices like lights, fans, and security cameras.
Each device class inherits from a base 'Device' class.
"""

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
        self.brightness = 0  # range: 0 to 100

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {self.brightness}%")
        else:
            print("Brightness level must be between 0 and 100.")

    def get_status(self):
        return super().get_status() + f", Brightness: {self.brightness}%"


# Fan class with speed control
class Fan(Device):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0  # range: 0 to 5

    def set_speed(self, speed):
        if 0 <= speed <= 5:
            self.speed = speed
            print(f"{self.name} speed set to {self.speed}")
        else:
            print("Fan speed must be between 0 and 5.")

    def get_status(self):
        return super().get_status() + f", Speed: {self.speed}"


# Security Camera class with motion detection and recording
class SecurityCamera(Device):
    def __init__(self, name):
        super().__init__(name)
        self.recording = False

    def start_recording(self):
        if self.is_on:
            self.recording = True
            print(f"{self.name} started recording.")
        else:
            print(f"{self.name} must be ON to record.")

    def stop_recording(self):
        self.recording = False
        print(f"{self.name} stopped recording.")

    def get_status(self):
        recording_status = "Recording" if self.recording else "Idle"
        return super().get_status() + f", Status: {recording_status}"


# Main smart home controller
class SmartHomeSystem:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added device: {device.name}")

    def remove_device(self, device_name):
        before_count = len(self.devices)
        self.devices = [d for d in self.devices if d.name != device_name]
        after_count = len(self.devices)
        if before_count == after_count:
            print(f"No device named '{device_name}' found.")
        else:
            print(f"Removed device: {device_name}")

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

    def show_all_status(self):
        print("\n📋 Device Status Report:")
        for device in self.devices:
            print(device.get_status())


# Demo: only runs if file is executed directly
if __name__ == "__main__":
    home = SmartHomeSystem()

    # Create smart devices
    light = Light("Living Room Light")
    fan = Fan("Bedroom Fan")
    camera = SecurityCamera("Front Door Camera")

    # Add devices to the system
    home.add_device(light)
    home.add_device(fan)
    home.add_device(camera)

    # Control devices
    light.turn_on()
    light.set_brightness(80)

    fan.turn_on()
    fan.set_speed(3)

    camera.turn_on()
    camera.start_recording()

    # Show status
    home.show_all_status()

    # Turn off everything
    home.turn_off_all_devices()

    # Remove a device
    home.remove_device("Bedroom Fan")

    # Final status
    home.show_all_status()
