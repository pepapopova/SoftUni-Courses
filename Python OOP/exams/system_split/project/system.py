from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)
        # VARIANT 2
        # try:
        #     hardware = [h for h in System._hardware if h.name == hardware_name][0]
        #     software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        #     hardware.install(software)
        #     System._software.append(software)
        # except IndexError:
        #     return "Hardware does not exist"
        # except Exception as ex:
        #     return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__find_hardware_by_name(hardware_name)
        software = System.__find_software_by_name(software_name)
        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis" + '\n' + f"Hardware Components: {len(System._hardware)}" + '\n'
        result += f"Software Components: {len(System._software)}" + '\n'
        result += f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])}" + " / "
        result += f"{sum([h.memory for h in System._hardware])}" + "\n"
        result += f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])}" + " / "
        result += f"{sum([h.capacity for h in System._hardware])}"
        return result


    @staticmethod
    def system_split():
        final_result = []
        for hardware in System._hardware:
            result = f"Hardware Component - {hardware.name}" + '\n'
            result += f"Express Software Components: {len([s.software_type for s in hardware.software_components if s.software_type == 'Express'])}" + '\n'
            result += f"Light Software Components: {len([s.software_type for s in hardware.software_components if s.software_type == 'Light'])}" + '\n'
            total_memory_installed_components = sum([s.memory_consumption for s in hardware.software_components])
            total_memory_hardware = hardware.memory
            result += f"Memory Usage: {total_memory_installed_components} / {total_memory_hardware}" + '\n'
            total_capacity_installed_software = sum([s.capacity_consumption for s in hardware.software_components])
            total_capacity_hardware = hardware.capacity
            result += f"Capacity Usage: {total_capacity_installed_software} / {total_capacity_hardware}" + '\n'
            result += f"Type: {hardware.hardware_type}" + '\n'
            software_components = ", ".join([s.name for s in hardware.software_components]) if len(hardware.software_components) > 0 else 'None'
            result += f"Software Components: {software_components}"
            final_result.append(result)
        return '\n'.join(final_result)

    @staticmethod
    def __find_hardware_by_name(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def __find_software_by_name(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    
