import time
import random

class PacketTracerAutomation:
    def __init__(self):
        # Initialize your automation class
        self.devices = {}

    def add_device(self, device_name, device_type):
        # Add a device to the simulation
        if device_name in self.devices:
            print(f"Device '{device_name}' already exists.")
            return
        self.devices[device_name] = {"type": device_type, "config": {}}
        print(f"Device '{device_name}' of type '{device_type}' added.")

    def configure_device(self, device_name, config):
        # Configure a device in Cisco Packet Tracer
        if device_name not in self.devices:
            print(f"Device '{device_name}' does not exist.")
            return
        self.devices[device_name]["config"] = config
        print(f"Configured device '{device_name}' with:\n{config}")

    def connect_devices(self, device1, device2, interface1=None, interface2=None):
        # Connect two devices in Cisco Packet Tracer
        if device1 not in self.devices or device2 not in self.devices:
            print("Both devices must exist in the simulation.")
            return
        if interface1 is None:
            interface1 = self._generate_random_interface()
        if interface2 is None:
            interface2 = self._generate_random_interface()
        print(f"Connected devices '{device1}' and '{device2}' via interfaces '{interface1}' and '{interface2}'.")

    def run_simulation(self):
        # Run the simulation in Cisco Packet Tracer
        print("Starting simulation...")
        time.sleep(random.randint(3, 5))
        print("Simulation complete.")

    def show_topology(self):
        # Display the network topology
        print("Current network topology:")
        for device, details in self.devices.items():
            print(f"Device: {device}, Type: {details['type']}, Config: {details['config']}")

    def _generate_random_interface(self):
        # Generate a random interface name
        prefix = random.choice(["GigabitEthernet", "FastEthernet", "TenGigabitEthernet"])
        number = random.randint(1, 24)
        return f"{prefix}{number}"

# Example usage:
if __name__ == "__main__":
    # Create an instance of the PacketTracerAutomation class
    pt_automation = PacketTracerAutomation()

    # Add devices to the simulation
    pt_automation.add_device("Router1", "Router")
    pt_automation.add_device("Switch1", "Switch")

    # Configure devices
    pt_automation.configure_device("Router1", "interface FastEthernet0/0\nip address 192.168.1.1 255.255.255.0")
    pt_automation.configure_device("Switch1", "interface FastEthernet0/1\nswitchport mode access")

    # Connect devices
    pt_automation.connect_devices("Router1", "Switch1")

    # Run simulation
    pt_automation.run_simulation()

    # Show network topology
    pt_automation.show_topology()
