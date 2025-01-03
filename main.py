from user_management.jumpbox_connections import JumpboxConnectionManager, JumpboxDetails
from user_management.devices import DeviceManager, DeviceInfo
from reporting.report_generator import ReportGenerator

def main():
    # Initialize managers
    jumpbox_manager = JumpboxConnectionManager()
    device_manager = DeviceManager()
    report_generator = ReportGenerator()

    # Example usage of JumpboxConnectionManager
    jumpbox_details = JumpboxDetails(hostname="192.168.1.1", username="admin", password="password", port=22)
    jumpbox_manager.add_connection("Jumpbox1", jumpbox_details)
    print(jumpbox_manager)

    # Example usage of DeviceManager
    device_info = DeviceInfo(type="Router", ipAddress="192.168.1.2", status="Active")
    device_manager.add_device("Device1", device_info)
    print(device_manager)

    # Example usage of ReportGenerator
    report_data = {"Jumpbox": jumpbox_manager.connections, "Devices": device_manager.devices}
    report_generator.generate_xlsx_report(report_data, "report.xlsx")
    report_generator.generate_pdf_report(report_data, "report.pdf")

if __name__ == "__main__":
    main()