from flask import Flask, request, jsonify
from user_management.jumpbox_connections import JumpboxConnectionManager
from user_management.devices import DeviceManager
from reporting.report_generator import ReportGenerator
from config.config_manager import ConfigManager
from monitoring.traffic_monitor import TrafficMonitor

app = Flask(__name__)

# Initialize managers
config_manager = ConfigManager()
jumpbox_manager = JumpboxConnectionManager()
device_manager = DeviceManager()
report_generator = ReportGenerator()
traffic_monitor = TrafficMonitor()

@app.route('/jumpbox', methods=['POST'])
def add_jumpbox():
    data = request.get_json()
    jumpbox_manager.add_connection(data['name'], data['details'])
    return jsonify({'message': 'Jumpbox added successfully'}), 201

@app.route('/device', methods=['POST'])
def add_device():
    data = request.get_json()
    device_manager.add_device(data['device_id'], data['device_info'])
    return jsonify({'message': 'Device added successfully'}), 201

@app.route('/report', methods=['GET'])
def generate_report():
    report_data = {'Jumpbox': jumpbox_manager.connections, 'Devices': device_manager.devices}
    report_generator.generate_xlsx_report(report_data, 'report.xlsx')
    report_generator.generate_pdf_report(report_data, 'report.pdf')
    return jsonify({'message': 'Report generated successfully'}), 200

@app.route('/traffic', methods=['GET'])
def monitor_traffic():
    traffic_data = traffic_monitor.monitor_traffic()
    return jsonify({'traffic_data': traffic_data}), 200

if __name__ == '__main__':
    app.run(debug=True)