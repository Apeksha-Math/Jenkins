import pyodbc
from configparser import ConfigParser
from threading import Lock
import datetime

class DatabaseManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseManager, cls).__new__(cls)
                cls._instance._connection = None
                cls._instance._cursor = None
                cls._instance.connect()
            return cls._instance

    def connect(self):
        if self._connection is None:
            config = ConfigParser()
            config.read('mdvr_config.ini')  # Adjust the file path as needed
            driver = config.get('Database', 'driver')
            server = config.get('Database', 'server')
            database = config.get('Database', 'database')
            username = config.get('Database', 'username')
            password = config.get('Database', 'password')

            connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
            self._connection = pyodbc.connect(connection_string, autocommit=True)
            self._cursor = self._connection.cursor()

    def insert_record(self, unit_no, vehicle_no, location_type, device_date_time, direction_in_degree, satellite, speed, lat, lon, x_acceleration,
        y_acceleration, z_acceleration, tilt, impact, fuel_consumption, balance_fuel, hd_status, hd_size, hd_balance, ibutton_to_send, messageType, ignition, gsm_signal,
        polling_mode, ha, hb, panic, fuel_bar, over_speed, analog, seat_belt, previous_value, ec, tp, SD_Type, SD_Status, version,
        device_Network_Type, alert_datetime, immobilizer,IN1,IN2):
        
        
        query = '''EXEC InsertIntoMdvrgpsandalarmdata @unit_no = ?, @vehicle_no = ?, @location_type = ?, @track_time = ?, @direction_in_degree = ?, @satellite = ?, @speed = ?, @lat = ?, @lon = ?, @x_acceleration = ?,
            @y_acceleration = ?, @z_acceleration = ?, @tilt = ?, @impact = ?, @fuel_consumption = ?, @balance_fuel = ?, @hd_status = ?, @hd_size = ?, @hd_balance = ?, @ibutton1 = ?, @message_type = ?, @ignition = ?, @gsm_signal = ?,
            @polling_mode = ?, @ha = ?, @hb = ?, @panic = ?, @fuel_bar = ?, @over_speed = ?, @analog = ?, @seat_belt = ?, @prev_value = ?,
            @ec = ?, @tp = ?, @SD_Type = ?, @SD_Status = ?, @version = ?, @Network_Type = ?, @alert_datetime = ?, @immobilizer = ?, @IN1 = ?, @IN2 = ?'''

        # Assuming you have the parameters defined earlier in your code
        params = (unit_no, vehicle_no, location_type, device_date_time, direction_in_degree, satellite, speed, lat, lon, x_acceleration,
                y_acceleration, z_acceleration, tilt, impact, fuel_consumption, balance_fuel, hd_status, hd_size, hd_balance, ibutton_to_send, messageType, ignition, gsm_signal,
                polling_mode, ha, hb, panic, fuel_bar, over_speed, analog, seat_belt, previous_value, ec, tp, SD_Type, SD_Status, version,
                device_Network_Type, alert_datetime, immobilizer, IN1, IN2)

        self._cursor.execute(query, params)



# Example usage:
if __name__ == "__main__":
    db_manager = DatabaseManager()
    unit_no = "91006"
    alert_datetime = datetime.datetime.now()
    polling_mode = "abnormal start"
    SD_Type = "0"
    SD_Status = "loss"
    vehicle_no = unit_no
    location_type = 0
    device_date_time = datetime.datetime.now()
    direction_in_degree = 0
    satellite = 0
    speed = 0
    lat = 0
    lon = 0
    x_acceleration = 0.0
    y_acceleration = 0.0
    z_acceleration = 0.0
    tilt = 0.0
    impact = 0.0
    fuel_consumption = 0
    balance_fuel = 0
    hd_status = "testing"
    hd_size = 65200
    hd_balance = 0
    ibutton_to_send = 0
    messageType = "0000"
    ignition = 0
    gsm_signal = 0
    ha = 0
    hb = 0
    panic = 0
    fuel_bar = 0
    over_speed = 0
    analog = 0
    seat_belt = 0
    previous_value = 0
    ec = 0
    tp = 0
    version = "testing"
    device_Network_Type = "1G"
    immobilizer = 0
    IN1= 0
    IN2= 0

    db_manager.insert_record(unit_no, vehicle_no, location_type, device_date_time, direction_in_degree, satellite, speed, lat, lon, x_acceleration,
        y_acceleration, z_acceleration, tilt, impact, fuel_consumption, balance_fuel, hd_status, hd_size, hd_balance, ibutton_to_send, messageType, ignition, gsm_signal,
        polling_mode, ha, hb, panic, fuel_bar, over_speed, analog, seat_belt, previous_value, ec, tp, SD_Type, SD_Status, version,
        device_Network_Type, alert_datetime, immobilizer,IN1,IN2)
